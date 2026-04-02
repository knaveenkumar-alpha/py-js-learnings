# Snowflake Interview Questions and Answers

## 1. What is Snowflake, and how is it different from traditional databases?
**Answer:**  
Snowflake is a cloud-native, fully managed data warehouse that separates compute and storage, enabling, scalable, concurrent processing. 
Unlike traditional databases, it offers features like auto-scaling, time travel, zero-copy cloning, and supports semi-structured data natively.

## 2. Explain Snowflake architecture.
**Answer:**  
a. Storage Layer: Centralized storage for structured and semi-structured data.
b. Compute Layer: Virtual Warehouses for executing queries independently.
c. Cloud Service Layer: Handles authentication, metadata management, and query optimization.

## 3. What are Virtual Warehouses in Snowflake?
**Answer:**  
Virtual Warehouses are clusters of compute resources in Snowflake used to execute queries. They are isolated, can be scaled independently, 
and paused/resumed on demand. Multiple warehouses can access the same data simultaneously without contention.

## 4. How does caching work in Snowflake?
**Answer:**  
Three levels: Result cache (24h), Metadata cache, and Data cache.
Snowflake uses three levels of caching:
*Result Cache:* Stores query results for 24 hours.
*Metadata Cache:* Stores table structure and statistics.
*Data Cache:* In-memory cache for data read by a warehouse.

## 5. What is Time Travel in Snowflake?
**Answer:**  
Allows querying previous data states (up to 90 days). Useful for undo and recovery.
Time Travel allows you to access data from a previous state (up to 1 - 90 days depending on your account). 
Useful for undoing deletions, recovering dropped tables, or auditing.
e.g. SELECT * FROM my_table AT (TIMESTAMP => '2024-05-04 12:00:00');

## 6. What is Zero-Copy Cloning?
**Answer:**  
Creates instant clones without duplicating data.
Zero-Copy Cloning allows you to create clones of databases, schemas, or tables instantly without duplicating the data.
Useful for testing and backup scenarios.
e.g. CREATE TABLE cloned_table CLONE original_table;

## 7. What are Streams and Tasks?
**Answer:**  
Streams track table changes; Tasks schedule SQL execution.
***Streams*** track changes (inserts, updates, deletes) in a table — useful for CDC (Change Data Capture)
***Tasks*** schedule SQL operations (e.g. running a transformation every hour).
Used together to build automated pipelines.

## 8. How do you optimize query performance?
**Answer:**  
Use clustering, caching, materialized views, and query refactoring.
- Use proper **clustering keys** for large tables.
- Minimize data scanned (e.g., avoid `SELECT *`).
- Use **materialized views** for frequently accessed aggregated data.
- Take advantage of **result caching**.
- Avoid unnecessary joins or subqueries.

## 9. How do you implement row-level security?
**Answer:**  
Using row access policies or secure views.
**CREATE OR REPLACE ROW ACCESS POLICY policy_name AS (user_role STRING) RETURNS BOOLEAN ->
    CURRENT_ROLE() = user_role;**

## 10. How do you load data into Snowflake?
**Answer:**  
Using COPY INTO from stages, or Snowpipe for real-time.
- Use `COPY INTO` to load data from internal or external stages (like S3, Azure Blob).
- For real-time loads, use **Snowpipe**.
- Supports formats like CSV, JSON, Parquet.
e.g. COPY INTO my_table FROM @my_stage FILE_FORMAT = (TYPE = 'CSV');

## 11. Difference between transient and permanent tables?
**Answer:**  
Transient: no fail-safe, shorter time travel. Permanent: default with full features.
- **Permanent Table:** Default, supports time travel and fail-safe.
- **Transient Table:** No fail-safe, limited time travel, used for temporary storage to reduce cost.

## 12. What is a clustering key?
**Answer:**  
Defines physical data order to optimize large table queries.
Clustering keys define how data is physically organized within a table to optimize query performance on large datasets. 
Use them when queries frequently filter on certain columns (e.g., date, customer_id).

## 13. What is a materialized view?
**Answer:**  
Pre-computed query results, faster reads, but requires refresh.
A Materialized view  stores pre-computed query result, improving performance for complex aggregations. 
Unlike standard views, it’s refreshed periodically and consumes storage.

## 14. How to handle semi-structured data?
**Answer:**  
Use VARIANT type, dot/bracket notation, FLATTEN().
Use VARIANT data type to load JSON, XML, or Avro. Access elements with dot or bracket notation:
e.g. SELECT data:customer.name FROM my_json_table;

## 15. How is data sharing done?
**Answer:**  
Using secure shares—no data copy needed.
Snowflake allows secure data sharing without copying data using Shares. Consumers can query shared data directly from 
the provider’s account without loading it into their own storage.
