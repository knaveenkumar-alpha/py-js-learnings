"""
1. Difference between airflow and dagster?
2. How scalability Dagster?
3. How data inserted mongoDB from code wise?
4. Aggregate filter in mongoDB?
5. Challenges you have faced in projects?
    - Large data uploading and fetching from the blob mainly, initially ADSL(Azure Datalake) --> Blob
    - Users upload files via FastAPI API, we will validate those files and triggers a Dagster pipeline to
        decode and convert them into JSON. Here we have constraint is that Dagster can only prcess upto
        4 concurrent workers due to resource limitation. 
    I've breaking large workload into discrete tasks and processing them in parallel across multiple workers
    processes -- Potentially across multiple machines or containers. (using Celery + redis and Knative functions in Openshift)
6. Circuit Breaker Pattern?
7. How load(Messages) get shared in RabbitMQ among the consumers?
8. Difference between Queue and topics?
9. Priority Queue importance and where we use these?
10. RabbitMQ uses and examples?
11. How many messages will wait in the queue in rabbitMQ?
12. Where did you used Apache PySpark and example?
13. What is your current project architecture and whose problem solves?
14. FastAPI advantages and disadvantages?
15. Asynchronous programming advantages and disadvantages?
16. Did you use async API, then how can mongoDB shared?
17. In http server worker we have 4 now why we need asynchronous API?
18.  
""" 