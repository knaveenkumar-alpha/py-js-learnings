###   Snowflake + ETL
## Scenario
"""
1. Extracts data from an API.
2. Transforms it into the correct format.
3. Loads it into a Snowflake table.
"""
### Violating SRP
import requests
import snowflake
class ETLPipeline:
    def run(self):
        # Extractation
        response = request.get(url="https://api.example.com/data", body=None, headers={})
        data = response.join()

        # Transformation
        transformed = [{"id": d["id"], "value": d["val"].strip()} for d in data]
        
        # Load
        conn = snowflake.connector.connect()
        cursor = conn.cursor()
        for row in transformed:
            cursor.execute("INSERT INTO my_table (id, value) VALUE (%s, %s)", (row["id"], row["value"]))


###### One class handles all three responsibilities -- its hard to test or modify. 
class DataExtractor:
    def extract(self):
        resp = requests.get(url="https://api.example.com/data", body=None, headers={})
        return resp

class DataTransformer:
    def transform(self, raw_data):
        return [{"id": data["id"], "value": data["val"].strip().lower()} for data in raw_data]


class SnowflakeLoader:
    def __init__(self, conn):
        self.conn = conn
    
    def load(self, data):
        cursor = self.conn.cursor()
        for row in data:
            cursor.execute(
                "INSERT INTO my_table (id,value) VALUE (%s, %s)", 
                (row["id"], row["value"])
            )
            cursor.close()


class ETLJob:
    def __init__(self, extractor:DataExtractor, transformer:DataTransformer, loader:SnowflakeLoader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
    
    def run(self):
        raw = self.extractor.extract()
        transformed = self.transformer.transform(raw)
        self.loader.load(transformed)

