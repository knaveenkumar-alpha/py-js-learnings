# Interface Segregation Principle (ISP) in Python with Example

Here's a Practical, real world example of the **Interface Segregation Principle (ISP)** in data engineering context, specifically with data ingestion pipelines using Snowflake and Azure Data Factory (ADF)

---

## Scenario:
You are building a **modular ingestion framework** in python to handle various types of data source: **Files, API, and Databases**.
Each source has different needs, e.g., files don't require authentication like API's:

```python

class DataSource:
    def read(self):
        pass
    def authenticate(self):
        pass

```
This violates ISP because **not all data sources need** authenticate() (e.g., CSV files on Azure Blob).

# ISP-Compliant Design
Split interfaces so each class only implements what it needs.
```python
from abc import ABC, abstractmethod

class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class Authenticator(ABC):
    @abstractmethod
    def authenticate(self):
        pass

```
# 🔧 Implementations

```python
class CSVFileReader(Reader):
    def read(self):
        print("Reading CSV from Azure Blob")

class APIReader(Reader, Authenticator):
    def authenticate(self):
        print("Authenticating API access token")
    
    def read(self):
        print("Reading data from API endpoint")

class DatabaseReader(Reader, Authenticator):
    def authenticate(self):
        print("Connecting to database with credentials")

    def read(self):
        print("Reading data from API endpoint")
```
# 🧪 Usage in Pipeline

```python

def ingest_data(source: Reader):
    if isinstance(source, Authenticator):
        source.authenticate()
    source.read()

ingest_data(CSVFileReader())
ingest_data(APIReader())
ingest_data(DatabaseReader())

```
# Benefits:
1. **CSVFileReader** doesn't need to implement *authenticate()* unnecessarily.
2. New data sources (e.g., Kafka, Avro, etc.,) can implement only what they need.
3. Clean, scalable design for ADF or Airflow Orchestration with Python.

