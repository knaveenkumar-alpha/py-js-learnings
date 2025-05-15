# 🧠 PySpark Interview Questions and Answers

---

## 1. What is PySpark?
**Answer:** PySpark is the Python API for Apache Spark, enabling scalable data processing with Python on distributed clusters.

---

## 2. Difference between RDD and DataFrame?
**Answer:**  
- **RDD**: Low-level, functional APIs, no schema  
- **DataFrame**: High-level abstraction, optimized using Catalyst and Tungsten

---

## 3. What is Catalyst Optimizer?
**Answer:** It is Spark SQL’s query optimizer which generates efficient execution plans for DataFrames and SQL queries.

---

## 4. What are transformations and actions?
**Answer:**  
- **Transformations**: Lazy operations (e.g., `map`, `filter`)  
- **Actions**: Trigger execution (e.g., `collect`, `count`)

---

## 5. How does Spark handle fault tolerance?
**Answer:** Through lineage of RDDs. Lost partitions are recomputed using transformation history.

---

## 6. Explain narrow vs wide transformations.
**Answer:**  
- **Narrow**: Each partition of parent used by one child (e.g., `map`)  
- **Wide**: Data shuffled across partitions (e.g., `groupBy`)

---

## 7. What is Broadcast variable?
**Answer:** A read-only variable cached on all nodes to avoid data transfer during joins.

---

## 8. Explain accumulator in Spark.
**Answer:** A write-only variable used to aggregate info across executors (e.g., counters).

---

## 9. Explain schema inference.
**Answer:** Spark can auto-detect data schema during load using `inferSchema=True`.

---

## 10. How do you optimize Spark jobs?
**Answer:** Caching, broadcast joins, partitioning, avoiding wide transformations, using DataFrames instead of RDDs.

---

# 🗂️ Advanced Topics

- Structured Streaming  
- Delta Lake  
- Machine Learning with MLlib  
- Integration with Hive, Kafka  

---

# 📘 Summary

PySpark is ideal for big data analytics, enabling scalable, fault-tolerant processing with Python. Its integration with the Spark ecosystem makes it powerful for ETL, ML, and real-time data processing.