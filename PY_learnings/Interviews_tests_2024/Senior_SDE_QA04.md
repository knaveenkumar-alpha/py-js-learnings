# Senior Software Developer and Lead Interview Questions (Part 4)

## Advanced Python OOP and Design Patterns
1. **Q: How do you implement the Factory Method pattern in Python?**  
   **A:** The Factory Method pattern defines an interface for creating objects, letting subclasses decide which class to instantiate. Example:  
   ```python
   class Vehicle:
       def drive(self):
           pass
   class Car(Vehicle):
       def drive(self):
           return "Driving a car"
   class Bike(Vehicle):
       def drive(self):
           return "Riding a bike"
   class VehicleFactory:
       def create_vehicle(self):
           pass
   class CarFactory(VehicleFactory):
       def create_vehicle(self):
           return Car()
   class BikeFactory(VehicleFactory):
       def create_vehicle(self):
           return Bike()
   factory = CarFactory()
   vehicle = factory.create_vehicle()
   print(vehicle.drive())  # Driving a car
   ```

2. **Q: Explain the Observer pattern in Python and its use case.**  
   **A:** The Observer pattern allows objects (observers) to be notified of changes in another object (subject). Useful for event-driven systems. Example:  
   ```python
   class Subject:
       def __init__(self):
           self._observers = []
       def attach(self, observer):
           self._observers.append(observer)
       def notify(self, message):
           for observer in self._observers:
               observer.update(message)
   class Observer:
       def update(self, message):
           print(f"Received: {message}")
   subject = Subject()
   observer = Observer()
   subject.attach(observer)
   subject.notify("Event occurred")  # Received: Event occurred
   ```

3. **Q: How do you implement the Strategy pattern in Python?**  
   **A:** The Strategy pattern defines interchangeable algorithms. Example:  
   ```python
   class Strategy:
       def execute(self, data):
           pass
   class AddStrategy(Strategy):
       def execute(self, data):
           return sum(data)
   class MultiplyStrategy(Strategy):
       def execute(self, data):
           result = 1
           for x in data: result *= x
           return result
   class Context:
       def __init__(self, strategy):
           self.strategy = strategy
       def set_strategy(self, strategy):
           self.strategy = strategy
       def execute(self, data):
           return self.strategy.execute(data)
   context = Context(AddStrategy())
   print(context.execute([1, 2, 3]))  # 6
   context.set_strategy(MultiplyStrategy())
   print(context.execute([1, 2, 3]))  # 6
   ```

4. **Q: How do you use `__getattribute__` to control attribute access dynamically?**  
   **A:** Override `__getattribute__` to intercept all attribute access. Example:  
   ```python
   class DynamicAccess:
       def __init__(self):
           self._data = {'x': 42}
       def __getattribute__(self, name):
           data = super().__getattribute__('_data')
           if name in data:
               return data[name]
           raise AttributeError(f"No attribute {name}")
   obj = DynamicAccess()
   print(obj.x)  # 42
   ```

5. **Q: How do you implement a chain of responsibility pattern in Python?**  
   **A:** Pass a request along a chain of handlers. Example:  
   ```python
   class Handler:
       def __init__(self, successor=None):
           self.successor = successor
       def handle(self, request):
           if self.successor:
               return self.successor.handle(request)
           return None
   class ConcreteHandler1(Handler):
       def handle(self, request):
           if request < 10:
               return f"Handler1 processed {request}"
           return super().handle(request)
   class ConcreteHandler2(Handler):
       def handle(self, request):
           if request < 20:
               return f"Handler2 processed {request}"
           return super().handle(request)
   handler = ConcreteHandler1(ConcreteHandler2())
   print(handler.handle(15))  # Handler2 processed 15
   ```

## SQL
6. **Q: Write a SQL query to find the top 5 customers by total spend in the last year.**  
   **A:**  
   ```sql
   SELECT 
       c.customer_id,
       c.name,
       SUM(o.amount) as total_spend
   FROM customers c
   JOIN orders o ON c.customer_id = o.customer_id
   WHERE o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 1 YEAR)
   GROUP BY c.customer_id, c.name
   ORDER BY total_spend DESC
   LIMIT 5;
   ```

7. **Q: Write a SQL query to find employees who joined in the last 3 months and have no sales.**  
   **A:**  
   ```sql
   SELECT e.employee_id, e.name
   FROM employees e
   LEFT JOIN sales s ON e.employee_id = s.employee_id
   WHERE e.join_date >= DATE_SUB(CURRENT_DATE, INTERVAL 3 MONTH)
     AND s.sale_id IS NULL;
   ```

8. **Q: Write a SQL query to calculate the average order value per product category.**  
   **A:**  
   ```sql
   SELECT 
       p.category,
       AVG(o.amount) as avg_order_value
   FROM products p
   JOIN order_items oi ON p.product_id = oi.product_id
   JOIN orders o ON oi.order_id = o.order_id
   GROUP BY p.category;
   ```

9. **Q: Write a SQL query to find the most frequent buyer for each product.**  
   **A:**  
   ```sql
   SELECT 
       p.product_id,
       c.customer_id,
       c.name,
       COUNT(o.order_id) as purchase_count
   FROM products p
   JOIN order_items oi ON p.product_id = oi.product_id
   JOIN orders o ON oi.order_id = o.order_id
   JOIN customers c ON o.customer_id = c.customer_id
   GROUP BY p.product_id, c.customer_id, c.name
   HAVING COUNT(o.order_id) = (
       SELECT MAX(cnt)
       FROM (
           SELECT COUNT(o2.order_id) as cnt
           FROM order_items oi2
           JOIN orders o2 ON oi2.order_id = o2.order_id
           WHERE oi2.product_id = p.product_id
           GROUP BY o2.customer_id
       ) sub
   );
   ```

10. **Q: Write a SQL query to find gaps in a sequence of order IDs.**  
    **A:**  
    ```sql
    SELECT 
        curr.order_id + 1 AS start_gap,
        MIN(nxt.order_id) - 1 AS end_gap
    FROM orders curr
    LEFT JOIN orders nxt ON nxt.order_id > curr.order_id
    GROUP BY curr.order_id
    HAVING MIN(nxt.order_id) > curr.order_id + 1;
    ```

## FastAPI
11. **Q: How do you implement background tasks in FastAPI?**  
    **A:** Use `BackgroundTasks`. Example:  
    ```python
    from fastapi import FastAPI, BackgroundTasks
    app = FastAPI()
    async def log_task(message):
        print(f"Logging: {message}")
    @app.post("/send")
    async def send_message(message: str, background_tasks: BackgroundTasks):
        background_tasks.add_task(log_task, message)
        return {"status": "Task scheduled"}
    ```

12. **Q: How do you handle file uploads in FastAPI?**  
    **A:** Use `UploadFile`. Example:  
    ```python
    from fastapi import FastAPI, File, UploadFile
    app = FastAPI()
    @app.post("/upload")
    async def upload_file(file: UploadFile = File(...)):
        contents = await file.read()
        return {"filename": file.filename, "size": len(contents)}
    ```

13. **Q: How do you implement pagination in FastAPI?**  
    **A:** Use query parameters and slicing. Example:  
    ```python
    from fastapi import FastAPI
    app = FastAPI()
    items = list(range(100))
    @app.get("/items")
    async def get_items(page: int = 1, page_size: int = 10):
        start = (page - 1) * page_size
        end = start + page_size
        return items[start:end]
    ```

14. **Q: How do you integrate FastAPI with Redis for caching?**  
    **A:** Use `aioredis`. Example:  
    ```python
    from fastapi import FastAPI
    import aioredis
    app = FastAPI()
    redis = aioredis.from_url("redis://localhost")
    @app.get("/data")
    async def get_data(key: str):
        cached = await redis.get(key)
        if cached:
            return {"data": cached.decode()}
        data = "expensive_computation"
        await redis.set(key, data, ex=3600)
        return {"data": data}
    ```

15. **Q: How do you implement custom middleware for request logging in FastAPI?**  
    **A:**  
    ```python
    from fastapi import FastAPI
    import time
    app = FastAPI()
    @app.middleware("http")
    async def log_requests(request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f"Request: {request.url} took {duration:.2f}s")
        return response
    ```

## Apache Airflow
16. **Q: How do you implement dynamic task generation in Airflow?**  
    **A:** Use a loop to create tasks dynamically. Example:  
    ```python
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from datetime import datetime
    def task_func(i):
        print(f"Task {i}")
    with DAG('dynamic_dag', start_date=datetime(2025, 1, 1)) as dag:
        tasks = [PythonOperator(task_id=f'task_{i}', python_callable=lambda x=i: task_func(x)) for i in range(3)]
        tasks[0] >> tasks[1] >> tasks[2]
    ```

17. **Q: How do you handle task retries in Airflow?**  
    **A:** Set `retries` and `retry_delay` in the task. Example:  
    ```python
    from airflow.operators.python import PythonOperator
    task = PythonOperator(
        task_id='retry_task',
        python_callable=lambda: print("Task"),
        retries=3,
        retry_delay=timedelta(minutes=5),
        dag=dag
    )
    ```

18. **Q: How do you integrate Airflow with a REST API?**  
    **A:** Use `SimpleHttpOperator`. Example:  
    ```python
    from airflow.operators.http import SimpleHttpOperator
    task = SimpleHttpOperator(
        task_id='call_api',
        http_conn_id='my_api',
        endpoint='/data',
        method='GET',
        dag=dag
    )
    ```

19. **Q: How do you manage Airflow connections securely?**  
    **A:** Store credentials in Airflow Connections via the UI or CLI, encrypted in the Metadata Database. Example CLI:  
    ```bash
    airflow connections add 'my_db' --conn-type 'postgres' --conn-host 'localhost' --conn-login 'user' --conn-password 'pass'
    ```

20. **Q: How do you implement a custom Airflow operator?**  
    **A:** Extend `BaseOperator`. Example:  
    ```python
    from airflow.models import BaseOperator
    class CustomOperator(BaseOperator):
        def __init__(self, param, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.param = param
        def execute(self, context):
            print(f"Executing with {self.param}")
    ```

## Azure Functions
21. **Q: How do you implement a queue-triggered Azure Function?**  
    **A:** Use a Queue trigger. Example `function.json`:  
    ```json
    {
        "scriptFile": "__init__.py",
        "bindings": [
            {
                "name": "msg",
                "type": "queueTrigger",
                "direction": "in",
                "queueName": "myqueue",
                "connection": "AzureWebJobsStorage"
            }
        ]
    }
    ```  
    `__init__.py`:  
    ```python
    import azure.functions as func
    def main(msg: func.QueueMessage) -> None:
        print(f"Queue message: {msg.get_body().decode()}")
    ```

22. **Q: How do you integrate Azure Functions with Event Hubs?**  
    **A:** Use an Event Hub trigger. Example `function.json`:  
    ```json
    {
        "scriptFile": "__init__.py",
        "bindings": [
            {
                "name": "event",
                "type": "eventHubTrigger",
                "direction": "in",
                "eventHubName": "myeventhub",
                "connection": "EventHubConnection"
            }
        ]
    }
    ```  
    `__init__.py`:  
    ```python
    import azure.functions as func
    def main(event: func.EventHubEvent):
        print(f"Event: {event.get_body().decode()}")
    ```

23. **Q: How do you implement durable functions for long-running workflows?**  
    **A:** Use `azure-functions-durable`. Example:  
    ```python
    import azure.durable_functions as df
    def orchestrator_function(context: df.DurableOrchestrationContext):
        result = yield context.call_activity("ProcessData", "input")
        return result
    ```

24. **Q: How do you handle secrets in Azure Functions?**  
    **A:** Use Azure Key Vault. Example:  
    ```python
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient
    def main(req: func.HttpRequest) -> func.HttpResponse:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url="https://myvault.vault.azure.net", credential=credential)
        secret = client.get_secret("my-secret")
        return func.HttpResponse(f"Secret: {secret.value}")
    ```

25. **Q: How do you optimize Azure Functions for cold start performance?**  
    **A:** Use Premium Plan, keep functions lightweight, and minimize dependencies. Pre-warm instances with scheduled triggers.

## Data Structures and Algorithms
26. **Q: Implement a function to find the shortest path in a grid with obstacles.**  
    **A:** Use BFS. Example:  
    ```python
    from collections import deque
    def shortest_path(grid, start, end):
        if not grid or grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
            return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])
        visited = {start}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == end:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                    queue.append((nx, ny, dist + 1))
                    visited.add((nx, ny))
        return -1
    ```

27. **Q: Write a function to find the longest valid parentheses sequence.**  
    **A:**  
    ```python
    def longest_valid_parentheses(s):
        stack = [-1]
        max_len = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len
    print(longest_valid_parentheses("(()())"))  # 6
    ```

28. **Q: Implement a function to find the minimum cost path in a matrix.**  
    **A:**  
    ```python
    def min_cost_path(matrix):
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = matrix[0][0]
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + matrix[i][j])
        return dp[rows-1][cols-1]
    print(min_cost_path([[1, 2, 3], [4, 8, 2], [1, 5, 3]]))  # 12
    ```

29. **Q: Write a function to check if a directed graph has a valid topological sort.**  
    **A:**  
    ```python
    from collections import deque
    def can_finish(num_courses, prerequisites):
        graph = [[] for _ in range(num_courses)]
        indegree = [0] * num_courses
        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        queue = deque([i for i in range(num_courses) if indegree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == num_courses
    print(can_finish(2, [[1, 0]]))  # True
    ```

30. **Q: Implement a function to find the maximum profit from stock prices with at most k transactions.**  
    **A:**  
    ```python
    def max_profit(k, prices):
        if not prices or k == 0:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i-1][j-1] - prices[j])
        return dp[k][n-1]
    print(max_profit(2, [3, 2, 6, 5, 0, 3]))  # 7
    ```

## System Design and Testing
31. **Q: How would you design a distributed logging system for a Python application?**  
    **A:** Use Fluentd or Logstash for log aggregation, store logs in Elasticsearch, and visualize with Kibana. Implement Python’s `logging` module with a custom handler to send logs to Fluentd. Scale with Kubernetes and monitor with Azure Monitor.

32. **Q: How do you implement unit testing for a FastAPI application?**  
    **A:** Use `pytest` and `TestClient`. Example:  
    ```python
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    @app.get("/items/{id}")
    async def get_item(id: int):
        return {"id": id}
    client = TestClient(app)
    def test_get_item():
        response = client.get("/items/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1}
    ```

33. **Q: How do you test Airflow DAGs?**  
    **A:** Use `pytest` with `pytest-airflow`. Example:  
    ```python
    from airflow.models import DagBag
    def test_dag_integrity():
        dag_bag = DagBag()
        assert not dag_bag.import_errors, "DAG import errors"
        dag = dag_bag.get_dag('my_dag')
        assert dag is not None
        assert len(dag.tasks) > 0
    ```

34. **Q: How do you implement integration testing for Azure Functions?**  
    **A:** Mock dependencies and use `func start` locally. Example:  
    ```python
    import azure.functions as func
    def main(req: func.HttpRequest) -> func.HttpResponse:
        return func.HttpResponse("Test")
    # Test with: func start and HTTP client
    ```

35. **Q: How do you design a system to handle high-throughput API requests?**  
    **A:** Use FastAPI for the API, Redis for caching, Kafka for queuing, and Kubernetes for scaling. Implement rate limiting and monitor with Prometheus.

## Leadership and Behavioral Questions
36. **Q: How do you lead a team through a major system migration?**  
    **A:** Plan phases, assign roles based on expertise, and use incremental migration with rollback plans. I led a migration from Flask to FastAPI, reducing latency by 25%, by running parallel systems and testing extensively.

37. **Q: Describe a time you had to manage stakeholder expectations.**  
    **A:** A client demanded an unrealistic feature timeline. I presented a technical breakdown, proposed a phased delivery, and secured approval, delivering the core feature on time.

38. **Q: How do you ensure your team delivers high-quality code under pressure?**  
    **A:** Enforce automated tests, use linters, and conduct quick code reviews. In a tight deadline, I implemented CI checks to catch issues early, maintaining quality.

39. **Q: How do you handle a team member resistant to adopting new tools?**  
    **A:** Understand their concerns, demonstrate tool benefits with a POC, and provide training. I convinced a team to adopt Airflow by showing its scheduling benefits.

40. **Q: Describe a time you improved system reliability.**  
    **A:** I implemented circuit breakers in a FastAPI app using `pybreaker`, reducing downtime by 30% during external service failures.

## Additional Technical Questions
41. **Q: How do you implement a custom Airflow sensor?**  
    **A:** Extend `BaseSensorOperator`. Example:  
    ```python
    from airflow.sensors.base import BaseSensorOperator
    class CustomSensor(BaseSensorOperator):
        def poke(self, context):
            return some_condition()
    ```

42. **Q: How do you handle large file processing in FastAPI?**  
    **A:** Stream file chunks. Example:  
    ```python
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse
    app = FastAPI()
    async def file_stream():
        with open("large_file.txt", "rb") as f:
            while chunk := f.read(1024):
                yield chunk
    @app.get("/file")
    async def stream_file():
        return StreamingResponse(file_stream(), media_type="text/plain")
    ```

43. **Q: How do you optimize a SQL query for a large join operation?**  
    **A:** Use indexes on join columns and avoid unnecessary columns. Example:  
    ```sql
    CREATE INDEX idx_order_customer ON orders(customer_id);
    SELECT c.name, o.order_date
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_date > '2025-01-01';
    ```

44. **Q: How do you implement retry logic in Airflow tasks?**  
    **A:** Use `task_retries`. Example:  
    ```python
    task = PythonOperator(
        task_id='retry_task',
        python_callable=lambda: print("Task"),
        retries=3,
        retry_delay=timedelta(minutes=5),
        dag=dag
    )
    ```

45. **Q: How do you integrate FastAPI with GraphQL?**  
    **A:** Use `strawberry` or `ariadne`. Example with `strawberry`:  
    ```python
    import strawberry
    from fastapi import FastAPI
    from strawberry.fastapi import GraphQLRouter
    @strawberry.type
    class Query:
        @strawberry.field
        def hello(self) -> str:
            return "Hello, GraphQL!"
    schema = strawberry.Schema(query=Query)
    app = FastAPI()
    app.include_router(GraphQLRouter(schema), prefix="/graphql")
    ```

46. **Q: How do you implement a custom Azure Function binding?**  
    **A:** Create a custom binding extension using `azure-functions`. Example requires advanced setup; refer to Azure documentation for specifics.

47. **Q: How do you monitor FastAPI performance in production?**  
    **A:** Use Prometheus and Grafana with `prometheus-fastapi-instrumentator`. Example:  
    ```python
    from fastapi import FastAPI
    from prometheus_fastapi_instrumentator import Instrumentator
    app = FastAPI()
    Instrumentator().instrument(app).expose(app)
    ```

48. **Q: How do you handle data versioning in Airflow?**  
    **A:** Use `DAG` versioning with `dag_id` suffixes or store versioned data in a database. Example:  
    ```python
    dag = DAG('my_dag_v1', start_date=datetime(2025, 1, 1))
    ```

49. **Q: How do you implement a circuit breaker in FastAPI?**  
    **A:** Use `pybreaker`. Example:  
    ```python
    from fastapi import FastAPI
    from pybreaker import CircuitBreaker
    app = FastAPI()
    breaker = CircuitBreaker(fail_max=3, reset_timeout=60)
    @app.get("/external")
    @breaker
    async def call_external():
        return {"data": "external response"}
    ```

50. **Q: How do you ensure data consistency in a distributed system using Azure Functions?**  
    **A:** Use Durable Functions for orchestration and Cosmos DB for transactional consistency. Implement retries and idempotency for reliability.
