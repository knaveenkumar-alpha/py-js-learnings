import os
import sys
from pathlib import Path
from unittest.mock import Mock

import pytest

pytest.importorskip("pyspark")

from src import spark_transformation as transformation
from src.claim_etl_job import write_output


@pytest.fixture(scope="session")
def spark():
    from pyspark.sql import SparkSession

    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    hadoop_home = Path(__file__).resolve().parents[1] / ".hadoop"
    hadoop_bin = hadoop_home / "bin"
    if os.name == "nt" and (hadoop_bin / "winutils.exe").exists():
        os.environ["HADOOP_HOME"] = str(hadoop_home)
        os.environ["PATH"] = f"{hadoop_bin}{os.pathsep}{os.environ['PATH']}"
    session = (
        SparkSession.builder.master("local[1]")
        .appName("claim-etl-tests")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )
    yield session
    session.stop()


def test_hashify_md4_uses_digest(monkeypatch):
    response = Mock()
    response.json.return_value = {"Digest": "digest-123"}
    get = Mock(return_value=response)
    monkeypatch.setattr(transformation.requests, "get", get)
    transformation._hashify_md4.cache_clear()

    assert transformation._hashify_md4("CL_123") == "digest-123"

    get.assert_called_once_with(
        transformation.HASHIFY_MD4_URL,
        params={"value": "CL_123"},
        timeout=10,
    )
    response.raise_for_status.assert_called_once_with()


def test_transform_claims_schema_and_values(spark, monkeypatch):
    claims = spark.range(2).select(
        transformation.F.when(transformation.F.col("id") == 0, "CL_123")
        .otherwise("RX_9")
        .alias("claim_id"),
        transformation.F.when(transformation.F.col("id") == 0, "PH_1")
        .otherwise("PH_2")
        .alias("policyholder_id"),
        transformation.F.when(transformation.F.col("id") == 0, "East")
        .otherwise("West")
        .alias("region"),
        transformation.F.when(transformation.F.col("id") == 0, 4500.0)
        .otherwise(100.0)
        .alias("claim_amount"),
        transformation.F.when(transformation.F.col("id") == 0, "2024-01-15")
        .otherwise("2024-02-20")
        .alias("claim_date"),
    )
    policyholders = spark.range(2).select(
        transformation.F.when(transformation.F.col("id") == 0, "PH_1")
        .otherwise("PH_2")
        .alias("policyholder_id"),
        transformation.F.when(transformation.F.col("id") == 0, "Alex")
        .otherwise("Sam")
        .alias("policyholder_name"),
    )
    hashes = {"CL_123": "hash-123", "RX_9": "hash-9"}
    monkeypatch.setattr(transformation, "_hashify_md4", lambda claim_id: hashes[claim_id])

    result = transformation.transform_claims(claims, policyholders)

    assert result.filter(
        (transformation.F.col("claim_id") == "CL_123")
        & (transformation.F.col("policyholder_name") == "Alex")
        & (transformation.F.col("claim_type") == "Coinsurance")
        & (transformation.F.col("claim_priority") == "Urgent")
        & (transformation.F.col("claim_period") == "2024-01")
        & (transformation.F.col("source_system_id") == "123")
        & (transformation.F.col("hash_id") == "hash-123")
    ).count() == 1
    assert result.filter(
        (transformation.F.col("claim_id") == "RX_9")
        & (transformation.F.col("claim_type") == "Reinsurance")
        & (transformation.F.col("claim_priority") == "Normal")
        & (transformation.F.col("hash_id") == "hash-9")
    ).count() == 1

    schema = {field.name: field.dataType.simpleString() for field in result.schema}
    assert schema["claim_id"] == "string"
    assert schema["claim_amount"] == "float"
    assert schema["source_system_id"] == "string"
    assert schema["hash_id"] == "string"


def test_write_output_creates_required_csv(spark, tmp_path):
    result = spark.range(1).select(
        transformation.F.lit("CL_123").alias("claim_id"),
        transformation.F.lit("Alex").alias("policyholder_name"),
        transformation.F.lit("East").alias("region"),
        transformation.F.lit("Coinsurance").alias("claim_type"),
        transformation.F.lit("Normal").alias("claim_priority"),
        transformation.F.lit(100.0).cast("float").alias("claim_amount"),
        transformation.F.lit("2024-01").alias("claim_period"),
        transformation.F.lit("123").alias("source_system_id"),
        transformation.F.lit("digest-123").alias("hash_id"),
    )
    output = tmp_path / "processed_claims.csv"

    write_output(result, str(output))

    lines = output.read_text(encoding="utf-8").splitlines()
    assert lines[0] == (
        "claim_id,policyholder_name,region,claim_type,claim_priority,"
        "claim_amount,claim_period,source_system_id,hash_id"
    )
    assert lines[1] == "CL_123,Alex,East,Coinsurance,Normal,100.0,2024-01,123,digest-123"
    assert sorted(path.name for path in tmp_path.iterdir()) == ["processed_claims.csv"]