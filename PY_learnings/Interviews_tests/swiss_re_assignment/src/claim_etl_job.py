"""Databricks job entry point for the claims ETL."""

import argparse
import os
import shutil
import sys
from pathlib import Path

from pyspark.sql import SparkSession

try:
    from src.spark_transformation import read_claims, read_policyholders, transform_claims
except ModuleNotFoundError:
    from spark_transformation import read_claims, read_policyholders, transform_claims


def parse_args() -> argparse.Namespace:
    """Parse input and output paths for the command-line job entry point."""
    parser = argparse.ArgumentParser(description="Transform claims into a CSV file.")
    parser.add_argument("--claims-input", required=True, help="CSV path or table:<catalog.schema.table>")
    parser.add_argument("--policyholders-input", required=True, help="CSV path or table:<catalog.schema.table>")
    parser.add_argument("--output", required=True, help="Output CSV file path")
    return parser.parse_args()


def write_output(result_df, output: str) -> None:
    """Write one headered CSV file at ``output``.

    Spark writes CSV data as a directory of part files. The temporary
    directory below is collapsed into the exact filename required by the
    submission contract after Spark finishes its distributed write.
    """
    output_path = Path(output)
    temp_path = output_path.with_name(f".{output_path.name}.spark_tmp")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if temp_path.exists():
        shutil.rmtree(temp_path)
    if output_path.exists():
        output_path.unlink()

    result_df.coalesce(1).write.mode("overwrite").option("header", True).csv(
        str(temp_path)
    )
    part_files = list(temp_path.glob("part-*.csv"))
    if len(part_files) != 1:
        shutil.rmtree(temp_path, ignore_errors=True)
        raise RuntimeError(f"Expected one Spark CSV part file, found {len(part_files)}")
    part_file = part_files[0]
    shutil.move(str(part_file), str(output_path))
    shutil.rmtree(temp_path, ignore_errors=True)


def create_spark_session() -> SparkSession:
    """Create a local-compatible Spark session for the ETL job.

    Delta support is retained for Databricks compatibility and local input
    table reads. The final submission output is written as CSV.
    """
    os.environ.setdefault("PYSPARK_PYTHON", sys.executable)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", sys.executable)
    local_hadoop_home = Path(__file__).resolve().parents[1] / ".hadoop"
    hadoop_bin = local_hadoop_home / "bin"
    if os.name == "nt" and (hadoop_bin / "winutils.exe").exists():
        os.environ.setdefault("HADOOP_HOME", str(local_hadoop_home))
        os.environ["PATH"] = f"{hadoop_bin}{os.pathsep}{os.environ['PATH']}"
    builder = SparkSession.builder.appName("claim-etl")
    try:
        from delta import configure_spark_with_delta_pip
    except ImportError:
        return builder.getOrCreate()

    builder = configure_spark_with_delta_pip(builder)
    return builder.config(
        "spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension"
    ).config(
        "spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    ).getOrCreate()


def main() -> None:
    """Run the claims read, transform, and CSV-write workflow."""
    args = parse_args()
    spark = create_spark_session()
    try:
        claims_df = read_claims(spark, args.claims_input)
        policyholders_df = read_policyholders(spark, args.policyholders_input)
        result_df = transform_claims(claims_df, policyholders_df)
        write_output(result_df, args.output)
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
