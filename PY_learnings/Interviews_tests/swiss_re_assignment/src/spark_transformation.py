"""Spark transformations for the claims ETL job."""

from functools import lru_cache

import requests
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import StringType, StructField, StructType

CLAIM_TYPE_MAPPING = {"CL": "Coinsurance", "RX": "Reinsurance"}
URGENT_THRESHOLD = 4000
HASHIFY_MD4_URL = "https://api.hashify.net/hash/md4/hex"


@lru_cache(maxsize=4096)
def _hashify_md4(claim_id: str) -> str:
    """Request and return Hashify's MD4 digest for one claim ID.

    The bounded cache prevents duplicate requests when the input contains the
    same claim ID more than once during a single driver run.
    """
    response = requests.get(
        HASHIFY_MD4_URL,
        params={"value": claim_id},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["Digest"]


def _build_hash_dataframe(claims_df: DataFrame) -> DataFrame:
    """Build a Spark lookup DataFrame for distinct non-null claim IDs.

    Hashify is an external HTTP service, so the requests are intentionally
    made on the driver before the hashes are joined back to the distributed
    claims DataFrame. Spark-native literals avoid creating a Python-backed
    DataFrame and keep the join free of a row-level UDF.
    """
    claim_id_rows = (
        claims_df.select("_claim_id")
        .where(F.col("_claim_id").isNotNull())
        .distinct()
        .collect()
    )
    hash_rows = [
        (row["_claim_id"], _hashify_md4(row["_claim_id"]))
        for row in claim_id_rows
    ]
    hash_schema = StructType(
        [
            StructField("hash_claim_id", StringType(), nullable=False),
            StructField("hash_id", StringType(), nullable=True),
        ]
    )

    if not hash_rows:
        return claims_df.sparkSession.range(0).select(
            F.lit(None).cast(hash_schema[0].dataType).alias("hash_claim_id"),
            F.lit(None).cast(hash_schema[1].dataType).alias("hash_id"),
        )

    # Use Spark literals rather than createDataFrame(list), which starts a
    # Python worker and is fragile in local Windows Spark environments.
    row_indexes = (F.col("id") + 1).cast("int")
    return claims_df.sparkSession.range(len(hash_rows)).select(
        F.element_at(
            F.array(*[F.lit(row[0]) for row in hash_rows]), row_indexes
        ).alias("hash_claim_id"),
        F.element_at(
            F.array(*[F.lit(row[1]) for row in hash_rows]), row_indexes
        ).alias("hash_id"),
    )


def transform_claims(claims_df: DataFrame, policyholders_df: DataFrame) -> DataFrame:
    """Join policyholder data and apply the required claim transformations."""
    claims = claims_df.withColumn("_claim_id", F.col("claim_id").cast("string"))
    policyholders = policyholders_df.select("policyholder_id", "policyholder_name")
    hash_df = _build_hash_dataframe(claims)

    merged_df = (
        claims.join(policyholders, on="policyholder_id", how="left")
        .join(hash_df, F.col("_claim_id") == F.col("hash_claim_id"), how="left")
    )

    claim_id = F.col("_claim_id")
    claim_amount = F.col("claim_amount").cast("float")
    claim_date = F.to_date(F.col("claim_date"))
    claim_prefix = F.upper(F.split(claim_id, "_").getItem(0))

    claim_type_map = F.create_map(
        *[F.lit(item) for pair in CLAIM_TYPE_MAPPING.items() for item in pair]
    )

    return merged_df.select(
        claim_id.alias("claim_id"),
        F.col("policyholder_name"),
        F.col("region"),
        F.coalesce(claim_type_map[claim_prefix], F.lit("Unknown")).alias("claim_type"),
        F.when(claim_amount > URGENT_THRESHOLD, F.lit("Urgent")).otherwise(F.lit("Normal")).alias("claim_priority"),
        claim_amount.alias("claim_amount"),
        F.coalesce(F.date_format(claim_date, "yyyy-MM"), F.lit("Unknown")).alias("claim_period"),
        F.regexp_extract(claim_id, r"(\d+)\s*$", 1).alias("source_system_id"),
        F.col("hash_id"),
    )


def read_claims(spark, claims_input: str) -> DataFrame:
    """Read claims from a CSV path or a registered Spark table."""
    if claims_input.startswith("table:"):
        return spark.table(claims_input.removeprefix("table:"))
    return spark.read.option("header", True).option("inferSchema", True).csv(claims_input)


def read_policyholders(spark, policyholders_input: str) -> DataFrame:
    """Read policyholders from a CSV path or a registered Spark table."""
    if policyholders_input.startswith("table:"):
        return spark.table(policyholders_input.removeprefix("table:"))
    return spark.read.option("header", True).option("inferSchema", True).csv(policyholders_input)
