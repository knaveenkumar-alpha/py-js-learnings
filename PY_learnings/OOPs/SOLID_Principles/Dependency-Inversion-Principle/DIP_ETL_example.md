
# Practical Example of Dependency Inversion Principle (DIP) in Python

This example demonstrates the Dependency Inversion Principle (DIP) in the context of a **data pipeline** that supports loading data into **Snowflake** or **S3**.

---

## 🔧 Problem Without DIP

If your pipeline code depends directly on classes like `SnowflakeLoader`, it becomes tightly coupled and hard to test or replace.

---

## ✅ Applying DIP

We separate high-level pipeline logic from low-level data destination details using abstractions.

---

## Step 1: Define an abstraction

```python
from abc import ABC, abstractmethod

class DataLoader(ABC):
    @abstractmethod
    def load_data(self, data):
        pass
```

---

## Step 2: Implement concrete loaders

```python
class SnowflakeLoader(DataLoader):
    def load_data(self, data):
        print(f"Loading data into Snowflake: {data}")

class S3Loader(DataLoader):
    def load_data(self, data):
        print(f"Uploading data to S3: {data}")
```

---

## Step 3: High-level pipeline depends on abstraction

```python
class ETLPipeline:
    def __init__(self, loader: DataLoader):
        self.loader = loader

    def run(self, data):
        print("Extracting and transforming data...")
        self.loader.load_data(data)
```

---

## Step 4: Usage Example

```python
# Pipeline using Snowflake
snowflake_pipeline = ETLPipeline(SnowflakeLoader())
snowflake_pipeline.run("customer_data.csv")

# Pipeline using S3
s3_pipeline = ETLPipeline(S3Loader())
s3_pipeline.run("logs_data.json")
```

---

## ✅ Benefits

- Decouples pipeline logic from specific data sinks.
- Easy to extend (e.g., add AzureBlobLoader).
- Easier to test with mock loaders.
