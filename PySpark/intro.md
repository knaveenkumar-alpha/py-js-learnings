# PySpark Overview and Interview QA markdown content

pyspark_overview_md = """
# ⚡ PySpark Complete Overview

---

## 📌 Introduction

**PySpark** is the Python API for Apache Spark — an open-source, distributed computing system. It allows for scalable big data processing using Python, enabling parallel computations on large datasets.

---

## 🏗️ Architecture

- **Driver Program**: Runs the `main()` function, coordinates execution.
- **Cluster Manager**: (YARN, Mesos, or Standalone) allocates resources.
- **Executors**: Perform data processing tasks.
- **RDD / DataFrame DAG**: Directed Acyclic Graph represents logical plan.

![Spark Architecture](https://spark.apache.org/docs/latest/img/cluster-overview.png)

---

## ⭐ Key Features

- Fast in-memory computation
- Distributed processing with fault tolerance
- Supports SQL, streaming, ML, and graph processing
- Seamless integration with HDFS, S3, Hive, JDBC, etc.

---

## 🔧 Core Concepts

### 1. RDD (Resilient Distributed Dataset)

```python
from pyspark import SparkContext
sc = SparkContext()
rdd = sc.parallelize([1, 2, 3, 4])
rdd.map(lambda x: x * 2).collect()

### 2. DataFrame API
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.select("name", "age").show()

### 3. Spark SQL
```python
df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people WHERE age > 30").show()

### 4. UDF's(User Defined Functions)
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def double_age(age):
    return age * 2

double_udf = udf(double_age, IntegerType())
df.withColumn("double_age", double_udf(df.age)).show()

### 5. Handling Nulls
```python
df.fillna(0).show()
df.dropna().show()
