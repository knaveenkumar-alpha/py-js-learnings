# Snowflake Interview Preparation Guide (3 Years Experience)

## ✅ Core Areas to Prepare

### 1. Snowflake Architecture
- Cloud services layer, compute layer, storage layer
- Separation of storage and compute
- Virtual warehouses and scalability

**Example Question:**  
_Explain Snowflake’s architecture and how it differs from traditional databases?_  
**Answer:**  
Snowflake uses a multi-cluster shared data architecture. It separates storage, compute, and services, allowing independent scaling and better concurrency.

### 2. Data Loading and Unloading
- COPY INTO command
- File formats: CSV, JSON, Parquet
- Staging, Snowpipe

**Example Question:**  
_How do you load data into Snowflake from S3?_  
**Answer:**  
Use the `COPY INTO` command with an external stage linked to S3. For real-time loading, use Snowpipe.

### 3. SQL & Query Performance
- Clustering keys
- Result caching, metadata caching
- Query profiling

**Example Question:**  
_What techniques have you used to optimize slow queries?_  
**Answer:**  
Clustering keys, efficient caching, and query refactoring.

### 4. Time Travel & Fail-safe
- Time Travel: undo deletes, restore dropped tables
- Fail-safe: disaster recovery

**Example Question:**  
_What’s the difference between Time Travel and Fail-safe?_  
**Answer:**  
Time Travel allows access to previous data versions; Fail-safe is internal to Snowflake for recovery.

### 5. Access Control & Security
- Role-based access control
- Data masking, row-level security

**Example Question:**  
_How do you enforce row-level security?_  
**Answer:**  
Using secure views or row access policies with session/user context.

## 🗂️ Additional Topics
- Streams & Tasks
- Zero-copy cloning
- Materialized views
- Semi-structured data handling
