""" 
OCP in Data Pipeline: Snowflake Loader Example

Build a pipeline where new data sources (CSV, JSON, Parquet, etc..) can be
supported without modifying existing loader code -- Just by adding new classes.

"""
#### Without OCP
class Dataloader:
    def load(self, file_type, file_path):
        if file_type == 'csv':
            # CSV loading logic
            pass
        elif file_type == 'json':
            # JSON loading logic
            pass
        elif file_type == 'parquet':
            # parquet loading logic
            pass


# ===============> Every new format requires modifying this class --- violates OCP

##### With OCP: Extendable Snowflake Loader
from abc import ABC, abstractmethod

class LoaderStrategy(ABC):
    @abstractmethod
    def load_to_snowflake(self, file_path, conn):
        pass


class CSVLoader(LoaderStrategy):
    def load_to_snowflake(self, file_path, conn):
        print(f"Loading CSV file {file_path} to Snowflake....")
        # Snowflake copy command for CSV
        # conn.cursor().execute("COPY INTO")


class JSONLoader(LoaderStrategy):
    def load_to_snowflake(self, file_path, conn):
        print(f"Loading JSON File {file_path} to Snowflake...")
        # Snowflake copy command for JSON. 


class ParquetLoader(LoaderStrategy):
    def load_to_snowflake(self, file_path, conn):
        print(f"Loading Parquet file {file_path} to Snowflake...")
        # Snowflake copy command for Parquet


class DataPipeline:
    def __init__(self, loader:LoaderStrategy):
        self.loader = loader
    
    def run(self, file_path, conn):
        self.loader.load_to_snowflake(file_path, conn)


####### USAGE EXAMPLE ########
# Dummy snowflake connection
conn = "snowflake_connection_placeholder"

pipeline = DataPipeline(CSVLoader())
pipeline.run("data/customers.csv", conn)

pipeline = DataPipeline(JSONLoader())
pipeline.run("data/events.json", conn)

""" 
📌 Real-World Application in ADF:

1. In Azure Data Factory, your Custom Activity or Azure Function can use this structure.
2. You can trigger different loader strategies based on metadata stored in a control table 
(e.g., file type column).
"""

""" 
✅ OCP Benefits in This Scenario:

1. Add new loaders (e.g., AvroLoader) by creating a new class — no existing logic is touched.
2. Keeps logic modular, reusable, and testable.
3. Integrates cleanly into ADF pipelines or Airflow DAGs.
"""