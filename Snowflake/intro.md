# ❄️ Snowflake Data Warehouse: Complete Introduction

---

## 📌 Introduction

**Snowflake** is a cloud-based data warehouse platform that enables scalable data storage, processing, and analytics. Unlike traditional data warehouses, Snowflake separates **compute** from **storage**, allowing flexible, cost-effective scaling and concurrency.

It is built for the cloud and supports:
- Structured and semi-structured data
- Concurrent workloads
- Secure data sharing

---

## 🏗️ Snowflake Architecture

Snowflake has a **multi-cluster shared data architecture** with three layers:

### 1. **Storage Layer**
Stores structured and semi-structured data in a centralized repository.

### 2. **Compute Layer**
Consists of **Virtual Warehouses** — independent compute clusters that perform queries and transformations.

### 3. **Cloud Services Layer**
Handles authentication, access control, metadata, query parsing, and optimization.

![Snowflake Architecture](https://raw.githubusercontent.com/snowflake-labs/sfguide/main/images/snowflake-architecture.png)

---

## ⭐ Key Features

- **Separation of compute and storage**
- **Automatic scaling** and **multi-cluster compute**
- **Zero-copy cloning**
- **Time Travel** (access past data versions)
- **Data sharing** without data movement
- **Support for semi-structured data** (JSON, XML, Avro)
- **High concurrency** with multiple virtual warehouses

---

## 📘 Core Concepts with Example

### 🔹 Creating a Database and Table

```sql
CREATE DATABASE sales_db;
USE DATABASE sales_db;

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount FLOAT
);
```

---

### 🔹 Loading Data

```sql
COPY INTO orders
FROM @my_s3_stage/orders/
FILE_FORMAT = (TYPE = 'CSV', FIELD_OPTIONALLY_ENCLOSED_BY='"');
```

---

### 🔹 Querying Data

```sql
SELECT customer_id, SUM(amount) as total_spent
FROM orders
GROUP BY customer_id;
```

---

### 🔹 Time Travel

Query a table as it was in the past:

```sql
SELECT * FROM orders AT (TIMESTAMP => '2024-06-01 10:00:00');
```

---

### 🔹 Zero-Copy Cloning

```sql
CREATE TABLE orders_clone CLONE orders;
```

---

### 🔹 Streams and Tasks (for CDC and Scheduling)

```sql
-- Create a stream to capture changes
CREATE OR REPLACE STREAM orders_stream ON TABLE orders;

-- Create a task to process the changes
CREATE OR REPLACE TASK process_stream
  WAREHOUSE = compute_wh
  SCHEDULE = '5 MINUTE'
AS
INSERT INTO audit_table SELECT * FROM orders_stream;
```

---

## 🔐 Security

- **Role-Based Access Control (RBAC)**
- **Column- and row-level security**
- **Data encryption at rest and in transit**

---

## 📦 Semi-Structured Data

```sql
CREATE TABLE json_data (
    raw VARIANT
);

INSERT INTO json_data VALUES
(PARSE_JSON('{"customer": {"id": 123, "name": "John"}}'));

SELECT raw:customer.name FROM json_data;
```

---

## 🧠 Summary

Snowflake provides:
- Powerful compute + elastic scaling
- Secure and governed access to data
- Native support for multiple data formats
- Flexibility for modern data engineering and analytics