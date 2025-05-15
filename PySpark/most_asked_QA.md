Here are **20 most commonly asked PySpark interview questions and answers**, covering beginner to advanced levels — perfect for interview preparation:

---

### 🔹 1. **What is PySpark?**

**Answer:** PySpark is the Python API for Apache Spark, allowing Python developers to write scalable big data processing applications using the Spark framework.

---

### 🔹 2. **Difference between RDD, DataFrame, and Dataset?**

**Answer:**

* **RDD**: Low-level API with no schema.
* **DataFrame**: High-level API with schema and optimizations.
* **Dataset**: Available only in Scala/Java; combines advantages of RDDs and DataFrames.

---

### 🔹 3. **What is a Transformation in Spark?**

**Answer:** Transformations are lazy operations (like `map`, `filter`) that define a new RDD/DataFrame but don't execute immediately.

---

### 🔹 4. **What is an Action in Spark?**

**Answer:** Actions (like `collect`, `count`, `take`) trigger the actual execution of transformations on the cluster.

---

### 🔹 5. **Explain Lazy Evaluation in Spark.**

**Answer:** Spark delays execution until an action is called. This allows optimization of the entire data flow for better performance.

---

### 🔹 6. **How does Spark ensure fault tolerance?**

**Answer:** Spark uses **RDD lineage** to recompute lost data partitions due to failures.

---

### 🔹 7. **Difference between narrow and wide transformations?**

**Answer:**

* **Narrow**: Data from a single partition is used (e.g., `map`).
* **Wide**: Data is shuffled across partitions (e.g., `groupBy`).

---

### 🔹 8. **What is a SparkSession?**

**Answer:** Entry point to use DataFrame and SQL APIs in PySpark.

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("App").getOrCreate()
```

---

### 🔹 9. **What is Catalyst Optimizer?**

**Answer:** It's the query optimization engine in Spark SQL that improves execution plans.

---

### 🔹 10. **What is Tungsten Project?**

**Answer:** Spark's initiative to improve the memory and execution efficiency of physical plans.

---

### 🔹 11. **What are Broadcast Variables?**

**Answer:** Shared, read-only variables cached on each worker to avoid shuffling during joins.

---

### 🔹 12. **What are Accumulators?**

**Answer:** Write-only variables used for aggregating information (e.g., counters) across workers.

---

### 🔹 13. **How can we improve performance in Spark?**

**Answer:**

* Use caching
* Avoid wide transformations
* Broadcast small tables
* Use DataFrames over RDDs
* Partitioning and predicate pushdown

---

### 🔹 14. **What is a Partition in Spark?**

**Answer:** A logical chunk of data; Spark processes each partition in parallel.

---

### 🔹 15. **How do you handle null values in DataFrames?**

**Answer:**

```python
df.dropna()
df.fillna({'column': 0})
```

---

### 🔹 16. **What is the use of `persist()` and `cache()`?**

**Answer:** Both store intermediate RDDs. `cache()` stores in memory only; `persist()` can store in memory and/or disk.

---

### 🔹 17. **What is a Window function in PySpark?**

**Answer:** Allows row-wise operations across a defined frame of data.

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import rank
window = Window.partitionBy("dept").orderBy("salary")
df.withColumn("rank", rank().over(window)).show()
```

---

### 🔹 18. **What is PySpark UDF?**

**Answer:** A User Defined Function lets you apply custom logic to columns in DataFrames.

---

### 🔹 19. **Difference between Hive and Spark SQL?**

**Answer:**

* Hive: Batch-processing, uses MapReduce.
* Spark SQL: Faster, uses in-memory computation with Catalyst Optimizer.

---

### 🔹 20. **How does PySpark integrate with other tools?**

**Answer:** PySpark integrates with Hive, Kafka, HBase, Cassandra, JDBC sources, and ML libraries like MLlib.