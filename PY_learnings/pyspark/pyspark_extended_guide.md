
# 📘 PySpark: Notebook Example, Comparison with pandas/Dask, and Setup Guide

---

## 🚀 1. Notebook-Based PySpark Project Example

### Project: Analyze Web Server Logs

**Goal**: Count requests per IP from web server logs using PySpark DataFrame.

#### 🔹 Sample Log Format:
```
192.168.0.1 - - [01/Apr/2025:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1024
```

#### 🔹 PySpark Code (Notebook Style):

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col

# Create Spark Session
spark = SparkSession.builder.appName("LogAnalysis").getOrCreate()

# Load log data
logs = spark.read.text("access.log")

# Extract IPs
logs_df = logs.select(regexp_extract("value", r'(^[\d.]+)', 1).alias("ip"))

# Count by IP
ip_count = logs_df.groupBy("ip").count().orderBy("count", ascending=False)

# Show top 10 IPs
ip_count.show(10)
```

#### 🔹 Extensions:
- Plot with matplotlib or seaborn.
- Join with GeoIP database to map IPs to countries.
- Export to Parquet or CSV.

---

## 🆚 2. PySpark vs Pandas vs Dask

| Feature               | pandas              | Dask                     | PySpark                     |
|-----------------------|---------------------|--------------------------|-----------------------------|
| Scale                 | In-memory only      | Out-of-core (multi-core) | Cluster-scale, distributed |
| Performance           | Great for small data| Parallel with limits     | Optimized for big data     |
| API                   | Pythonic            | Similar to pandas        | SQL-like + DataFrame/RDD   |
| Cluster Integration   | ❌                  | ✅ (threads/processes)    | ✅ (YARN, Mesos, Kubernetes)|
| ML/SQL Support        | Via sklearn, etc.   | Yes                      | Native (MLlib, SQL)        |
| Use Case              | Small, local tasks  | Mid-scale tasks          | Enterprise-scale workflows |

---

## 🖥️ 3. Run PySpark on Local or Cloud

### 🔹 Local Setup

1. **Install Java**:
   ```bash
   sudo apt install openjdk-11-jdk
   ```

2. **Install Spark**:
   - Download Spark from https://spark.apache.org/downloads
   - Unzip and add to PATH

3. **Install PySpark**:
   ```bash
   pip install pyspark
   ```

4. **Run in Python or Jupyter**:
   ```python
   from pyspark.sql import SparkSession
   spark = SparkSession.builder.appName("LocalApp").getOrCreate()
   ```

---

### 🔹 Cloud Setup

#### ✅ Databricks (Recommended)
- Managed Spark service.
- Free community edition available.
- Use notebooks + clusters with auto-scaling.

#### ✅ AWS EMR
- Launch cluster from console or CLI.
- Submit PySpark jobs via script or JupyterHub.

#### ✅ GCP Dataproc / Azure HDInsight
- Similar to AWS EMR.
- Fully integrated with their respective cloud storage systems.

---

## 🛠️ Resources

- [PySpark Docs](https://spark.apache.org/docs/latest/api/python/)
- [Databricks Notebooks](https://community.cloud.databricks.com/)
- [Awesome PySpark GitHub](https://github.com/awesome-spark/awesome-spark)

---

Let me know if you'd like:
- A sample notebook file
- Dockerized PySpark setup
- Step-by-step Databricks tutorial
