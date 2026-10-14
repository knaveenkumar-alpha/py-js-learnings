## Data Engineering Interview Questions and Answers

### 1. What is liquid clustering? Explain with example code.

Liquid clustering is a Databricks Delta Lake data-layout technique. It organizes data around selected clustering columns to make common filters read less data. Unlike traditional partitioning, it does not create a fixed directory hierarchy, and clustering keys can be adjusted as query patterns change. Use it for large tables where queries commonly filter on chosen columns.

```sql
CREATE TABLE orders (
  order_id BIGINT,
  customer_id BIGINT,
  order_date DATE,
  amount DECIMAL(12, 2)
)
USING DELTA
CLUSTER BY (customer_id, order_date);

OPTIMIZE orders;

SELECT * FROM orders
WHERE customer_id = 42 AND order_date >= DATE '2026-01-01';
```

Choose clustering columns from actual query patterns. Liquid clustering is not the same as partitioning; confirm runtime and table-feature support in your Databricks environment.

### 2. What is DBR in Databricks? Explain with an example.

DBR (Databricks Runtime) is the software environment used by a Databricks cluster or SQL warehouse to run workloads. It includes Apache Spark plus Databricks optimizations, compatible libraries, and runtime components. Runtime versions specify the Spark and language versions; some variants, such as ML Runtime, include additional libraries, while Photon-enabled runtimes can accelerate supported workloads.

For example, select a supported Databricks Runtime version when creating a cluster, then run a Spark job on it:

```python
print(spark.version)  # Spark version included in the selected DBR

orders = spark.read.format("delta").load("/tables/orders")
orders.filter("order_date >= DATE '2026-01-01'").groupBy("customer_id").count().show()
```

Choose a runtime compatible with your libraries and required features, and test upgrades before changing production workloads.

### 2. What is schema evaluation? Explain with example.

Schema evaluation means checking incoming data against an expected contract: field names, data types, and required/nullability rules. It helps catch missing, unexpected, or incompatible fields before data is written. It is distinct from schema evolution, which deliberately changes the target schema.

```python
from pyspark.sql.types import StructType, StructField, LongType, StringType

expected = StructType([
	StructField("order_id", LongType(), nullable=False),
	StructField("customer", StringType(), nullable=True),
])

incoming = spark.read.json("/data/incoming/orders")
expected_types = {f.name: f.dataType for f in expected.fields}
actual_types = {f.name: f.dataType for f in incoming.schema.fields}

missing = set(expected_types) - set(actual_types)
unexpected = set(actual_types) - set(expected_types)
wrong_types = {
	name: (expected_types[name], actual_types[name])
	for name in expected_types.keys() & actual_types.keys()
	if expected_types[name] != actual_types[name]
}

if missing or wrong_types:
	raise ValueError(f"Schema mismatch: missing={missing}, wrong_types={wrong_types}")
# Decide whether unexpected fields should be rejected, quarantined, or accepted.
```

In production, log changes and quarantine invalid data rather than silently dropping or coercing fields.

### 3. What is partition pruning? Explain with example.

Partition pruning is Spark's ability to skip table partitions that cannot match a filter on a partition column. If a Delta table is partitioned by `event_date`, filtering for a date range can avoid reading all other dates.

```python
events = spark.read.format("delta").load("/tables/events")
recent = events.filter(
	"event_date >= '2026-06-01' AND event_date < '2026-07-01'"
)
recent.explain("formatted")  # Inspect the scan and partition filters
```

Keep predicates usable on the partition column; applying a function to it may prevent pruning. Partitioning works best with commonly filtered, reasonably low-cardinality columns. Excessive partitions can create many small files.

### 4. What is the Spark Catalyst Optimizer? Explain with example code.

Catalyst is Spark SQL's query optimizer. It analyzes SQL/DataFrame expressions, builds and optimizes logical plans, selects a physical plan, and can generate optimized code. Common optimizations include predicate pushdown, column pruning, and constant folding.

```python
from pyspark.sql.functions import col

result = (spark.read.parquet("/data/sales")
		  .filter(col("country") == "US")
		  .select("customer_id", "amount")
		  .groupBy("customer_id")
		  .sum("amount"))

result.explain("formatted")  # Review the physical plan and scan filters
```

Expressing transformations as Spark SQL/DataFrame operations lets Spark optimize them. Inspect the plan to confirm what Spark will actually execute.

### 5. Five pipelines share a schema, and one pipeline now has five extra columns. What should we do?

First determine whether the columns are intentional and approved. Compare their names, types, meaning, and quality with the data contract, and check downstream consumers.

- If they are valid additions, update and version the canonical schema in a backward-compatible way. Make fields nullable or define defaults as appropriate, then update tests and notify consumers.
- If they belong only to that source, retain them in the source/raw layer and map the data to the common schema. Preserve source-specific attributes separately if needed.
- If they are unexpected, reject or quarantine the batch and alert the source owner; do not silently change a shared table.
- Use schema validation to detect future drift and coordinate incompatible changes such as renames or type changes.

For an approved Delta schema change, a write can use `.option("mergeSchema", "true")`. Do not enable schema evolution indiscriminately, because unintended fields could enter a shared table.

### 6. What is data skew? Explain with example.

Data skew occurs when data or work is distributed unevenly across Spark partitions. For example, if most transactions have a small number of very common customer IDs, a join or aggregation for those keys can leave a few tasks much larger than the rest. Those straggler tasks slow the entire stage.

```python
from pyspark.sql.functions import col

# Check whether a few keys dominate the data.
transactions.groupBy("customer_id").count().orderBy(col("count").desc()).show(10)

# A join on a heavily skewed key can produce straggler tasks.
joined = transactions.join(customers, "customer_id")
```

Possible remedies include enabling Adaptive Query Execution (AQE) skew-join handling, broadcasting a genuinely small dimension table, pre-aggregating when valid, or salting hot keys. Salting splits a hot key into buckets and requires matching logic on the other side, so measure first.

### 7. What is the difference between `repartition` and `coalesce`?

`repartition(n)` reshuffles data and can increase or decrease the partition count; use it when you need more even distribution. `coalesce(n)` generally reduces partitions with less data movement, often before writing output. Check resulting partition sizes to avoid creating skew or oversized files.

```python
balanced = df.repartition(200, "customer_id")
smaller_output = balanced.coalesce(40)
```

### 8. What are narrow and wide transformations?

A narrow transformation, such as `select` or `filter`, can compute output partitions from a limited set of input partitions. A wide transformation, such as `groupBy`, `distinct`, or many joins, redistributes data across partitions and causes a shuffle. Shuffles use network, disk, and serialization resources.

### 9. What is a shuffle, and how can you reduce its cost?

A shuffle redistributes records between executors, commonly by key, so operations such as grouping and joining can bring related records together. Avoid unnecessary shuffles, filter and select early, pre-aggregate when correct, choose suitable partition counts, and inspect the Spark UI and execution plan to identify expensive stages.

### 10. What is a broadcast join, and when should you use it?

A broadcast join sends a small table to each executor so Spark can join it with a large table without shuffling both sides. Use it only when the smaller table safely fits in executor memory.

```python
from pyspark.sql.functions import broadcast

result = large_fact.join(broadcast(small_dimension), "dimension_id")
```

### 11. What is batch processing versus streaming?

Batch processing handles a bounded set of data, usually on a schedule. Streaming processes continuously arriving data, often in micro-batches, and must account for event time, late arrivals, checkpoints, and recovery. Choose based on latency, cost, and correctness requirements.

### 12. What are event time, processing time, and watermarking?

Event time is when an event occurred; processing time is when the system handled it. A watermark defines how long a streaming query tracks late events for event-time operations and when it can finalize old windows and clean state. It is a lateness policy, not a guarantee that later events cannot arrive.

### 13. What is an idempotent pipeline?

An idempotent pipeline can be retried or rerun without creating duplicate or inconsistent results. Common techniques include stable business keys, deterministic transformations, deduplication, transactional writes, and merge/upsert logic. Test retries after partial failures as well as full reprocessing.

### 14. What is medallion architecture?

The medallion pattern organizes data into layers: Bronze stores ingested data with minimal changes, Silver cleans and standardizes it, and Gold contains business-ready models or aggregates. The layers support traceability and reuse, but each still needs quality checks and clear ownership.

### 15. What is ETL versus ELT?

ETL means Extract, Transform, Load: transform data before loading it into the target. ELT means Extract, Load, Transform: load data first and transform it in the destination platform. The choice depends on security, latency, cost, and platform capabilities.

### 16. How do you handle bad records?

Validate required fields, types, ranges, and business rules. Separate valid and invalid records, store invalid records with error reasons in a quarantine location, alert on thresholds, and make records replayable after correction. Avoid silently dropping data.

### 17. How do you troubleshoot a slow Spark job?

Start with evidence: inspect the Spark UI, stage and task times, shuffle size, spill, input volume, and `explain("formatted")` output. Then address the measured bottleneck—for example, filter earlier, improve a join, handle skew, tune partition counts, or compact small files. Benchmark against representative data.

### 18. What is the small-files problem?

Many tiny files increase metadata listing and task scheduling overhead and can reduce scan efficiency. Avoid excessive output partitions, choose sensible write sizes, and compact files when supported (for example, Delta `OPTIMIZE`). Follow the platform's maintenance and concurrency practices.

### 19. What is CDC, and how do you apply it?

Change Data Capture (CDC) represents inserts, updates, and deletes from a source. Apply changes using a stable key and reliable ordering field, deduplicate repeated events, and handle deletes explicitly. Idempotent merge/upsert logic makes replay safer.

### 20. How do you ensure data quality and pipeline reliability?

Use explicit schemas and versioned contracts; validate completeness, uniqueness, ranges, and business rules where relevant. Monitor freshness and volume, keep audit metadata and lineage, alert on agreed thresholds, and test recovery and replay behavior.

### 21. Recommend new friends who share interest in at least two private events

Assumption: `going` and `maybe` both count as showing interest; `not_going` does not. Friendship is treated as undirected: a pair is already friends if either orientation has status `friends`. The result lists each pair once.

```sql
WITH interested AS (
	-- One row per user/event, even if duplicate RSVP records exist.
	SELECT DISTINCT user_id, event_id
	FROM event_rsvp
	WHERE event_type = 'private'
	  AND attendance_status IN ('going', 'maybe')
), shared_events AS (
	SELECT
		a.user_id AS user_1_id,
		b.user_id AS user_2_id,
		COUNT(*) AS shared_private_event_count
	FROM interested AS a
	JOIN interested AS b
	  ON a.event_id = b.event_id
	 AND a.user_id < b.user_id
	GROUP BY a.user_id, b.user_id
	HAVING COUNT(*) >= 2
)
SELECT s.user_1_id, s.user_2_id, s.shared_private_event_count
FROM shared_events AS s
WHERE NOT EXISTS (
	SELECT 1
	FROM friendship_status AS f
	WHERE f.status = 'friends'
	  AND (
		  (f.user_1_id = s.user_1_id AND f.user_2_id = s.user_2_id)
		  OR
		  (f.user_1_id = s.user_2_id AND f.user_2_id = s.user_1_id)
	  )
)
ORDER BY s.shared_private_event_count DESC, s.user_1_id, s.user_2_id;
```

**How the query works:**

1. `interested` filters to private events and the two RSVP statuses that represent interest. `DISTINCT` ensures an event is counted only once per user.
2. The self-join matches two users who have an RSVP for the same event. `a.user_id < b.user_id` rules out matching a user to themself and avoids returning both `(222, 333)` and `(333, 222)`.
3. `GROUP BY` counts common events per pair. `HAVING` filters groups to pairs with at least two shared events.
4. `NOT EXISTS` is an anti-join: it removes pairs already marked as friends, checking both ID orders. Rows marked `not_friends` do not exclude a pair.

For the supplied data, the result is `(222, 333, 2)`: they share private events 789 and 234. User 111 is `not_going` to event 234, and users 111 and 222 already have a `friends` status.

If “interest” means confirmed attendance only, use `attendance_status = 'going'` instead. With that stricter rule, no sample pair shares two private events.

**Related SQL concepts to practice:** self-joins, CTEs, filtering before aggregation, `GROUP BY`/`HAVING`, deduplication, anti-joins (`NOT EXISTS`), and canonical ordering of undirected pairs. For production queries, clarify whether friendships are directional, whether only the latest RSVP per user/event counts, how canceled events are handled, and whether to cap recommendations per user. For larger tables, consider indexing or organizing data by `event_id` and inspect the execution plan.

## What is DBR in databricks  and explain me with examples?