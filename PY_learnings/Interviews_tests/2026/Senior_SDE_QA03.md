# EPAM Senior Software Developer and Lead Interview Questions (Part 3)

## Advanced Python OOP Concepts
1. **Q: What is the difference between a class method, static method, and instance method in Python?**  
   **A:** Instance methods take `self` and operate on an instance’s attributes. Class methods take `cls` and operate on the class itself, decorated with `@classmethod`. Static methods, decorated with `@staticmethod`, don’t take `self` or `cls` and behave like regular functions but are scoped to the class. Example:  
   ```python
   class MyClass:
       @classmethod
       def class_method(cls):
           return f"Class: {cls.__name__}"
       @staticmethod
       def static_method():
           return "Static"
       def instance_method(self):
           return "Instance"
   obj = MyClass()
   print(obj.instance_method())  # Instance
   print(MyClass.class_method())  # Class: MyClass
   print(MyClass.static_method())  # Static
   ```

2. **Q: How do you implement multiple inheritance in Python, and what is the Method Resolution Order (MRO)?**  
   **A:** Multiple inheritance allows a class to inherit from multiple parent classes. Python uses the C3 linearization algorithm for MRO to determine the order in which base classes are searched. Example:  
   ```python
   class A:
       def method(self):
           print("A")
   class B:
       def method(self):
           print("B")
   class C(A, B):
       pass
   print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
   C().method()  # A
   ```

3. **Q: What is a mixin in Python, and how is it used?**  
   **A:** A mixin is a class designed to provide methods to other classes via inheritance, without being instantiated itself. Example:  
   ```python
   class LoggingMixin:
       def log(self, message):
           print(f"Log: {message}")
   class MyClass(LoggingMixin):
       def do_something(self):
           self.log("Doing something")
   obj = MyClass()
   obj.do_something()  # Log: Doing something
   ```

4. **Q: How can you enforce a singleton pattern in Python?**  
   **A:** Use a class attribute to store the single instance and override `__new__`. Example:  
   ```python
   class Singleton:
       _instance = None
       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
           return cls._instance
   s1 = Singleton()
   s2 = Singleton()
   print(s1 is s2)  # True
   ```

5. **Q: Explain the use of `__slots__` in Python.**  
   **A:** `__slots__` restricts the attributes a class can have, reducing memory usage by avoiding a `__dict__`. Example:  
   ```python
   class Point:
       __slots__ = ['x', 'y']
       def __init__(self, x, y):
           self.x = x
           self.y = y
   p = Point(1, 2)
   # p.z = 3  # AttributeError: 'Point' object has no attribute 'z'
   ```

6. **Q: How do you implement a custom property using descriptors?**  
   **A:** Define a descriptor class with `__get__` and `__set__`. Example:  
   ```python
   class Property:
       def __init__(self, name):
           self.name = f"_{name}"
       def __get__(self, obj, owner):
           return getattr(obj, self.name)
       def __set__(self, obj, value):
           setattr(obj, self.name, value)
   class MyClass:
       x = Property('x')
   obj = MyClass()
   obj.x = 42
   print(obj.x)  # 42
   ```

7. **Q: What is the purpose of the `@abstractmethod` decorator in Python?**  
   **A:** It marks a method as abstract, requiring subclasses to implement it. Used with the `abc` module. Example:  
   ```python
   from abc import ABC, abstractmethod
   class Animal(ABC):
       @abstractmethod
       def speak(self):
           pass
   class Dog(Animal):
       def speak(self):
           return "Woof"
   ```

8. **Q: How do you override the default behavior of an operator in Python?**  
   **A:** Implement special methods like `__add__`, `__eq__`, etc. Example:  
   ```python
   class Vector:
       def __init__(self, x, y):
           self.x = x
           self.y = y
       def __add__(self, other):
           return Vector(self.x + other.x, self.y + other.y)
   v1 = Vector(1, 2)
   v2 = Vector(3, 4)
   v3 = v1 + v2
   print(v3.x, v3.y)  # 4 6
   ```

9. **Q: Explain the difference between `__call__` and `__init__` in Python.**  
   **A:** `__init__` initializes an instance, while `__call__` makes an instance callable like a function. Example:  
   ```python
   class Callable:
       def __init__(self, value):
           self.value = value
       def __call__(self, x):
           return self.value + x
   obj = Callable(10)
   print(obj(5))  # 15
   ```

10. **Q: How do you implement a custom context manager without using `contextlib`?**  
    **A:** Define `__enter__` and `__exit__` methods. Example:  
    ```python
    class Resource:
        def __enter__(self):
            print("Resource acquired")
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Resource released")
    with Resource() as r:
        print("Using resource")
    ```

## SQL
11. **Q: Write a SQL query to find duplicate records in a table.**  
    **A:**  
    ```sql
    SELECT name, COUNT(*) as count
    FROM employees
    GROUP BY name
    HAVING COUNT(*) > 1;
    ```

12. **Q: Write a SQL query to find the second highest salary without using LIMIT.**  
    **A:**  
    ```sql
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (SELECT MAX(salary) FROM employees);
    ```

13. **Q: Write a SQL query to calculate the running total of sales per customer.**  
    **A:**  
    ```sql
    SELECT 
        customer_id,
        order_date,
        amount,
        SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) as running_total
    FROM sales;
    ```

14. **Q: Write a SQL query to find employees who earn more than their managers.**  
    **A:**  
    ```sql
    SELECT e1.name
    FROM employees e1
    JOIN employees e2 ON e1.manager_id = e2.employee_id
    WHERE e1.salary > e2.salary;
    ```

15. **Q: Write a SQL query to rank employees by salary within each department.**  
    **A:**  
    ```sql
    SELECT 
        name,
        department_id,
        salary,
        RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as salary_rank
    FROM employees;
    ```

16. **Q: Write a SQL query to find the top 3 products by sales in each region.**  
    **A:**  
    ```sql
    SELECT *
    FROM (
        SELECT 
            region,
            product,
            SUM(sales) as total_sales,
            RANK() OVER (PARTITION BY region ORDER BY SUM(sales) DESC) as rnk
        FROM sales
        GROUP BY region, product
    ) t
    WHERE rnk <= 3;
    ```

17. **Q: Write a SQL query to find the longest consecutive login streak for each user.**  
    **A:**  
    ```sql
    WITH login_groups AS (
        SELECT 
            user_id,
            login_date,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) -
            ROW_NUMBER() OVER (PARTITION BY user_id, DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) DAY) ORDER BY login_date) as group_id
        FROM logins
    )
    SELECT 
        user_id,
        MAX(COUNT(*)) as longest_streak
    FROM login_groups
    GROUP BY user_id, group_id;
    ```

18. **Q: Write a SQL query to pivot data from rows to columns (e.g., sales by month).**  
    **A:**  
    ```sql
    SELECT 
        product,
        SUM(CASE WHEN MONTH(sale_date) = 1 THEN amount ELSE 0 END) as jan,
        SUM(CASE WHEN MONTH(sale_date) = 2 THEN amount ELSE 0 END) as feb
    FROM sales
    GROUP BY product;
    ```

19. **Q: Write a SQL query to find customers who have not placed orders in the last 6 months.**  
    **A:**  
    ```sql
    SELECT c.customer_id, c.name
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
        AND o.order_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    WHERE o.order_id IS NULL;
    ```

20. **Q: Write a SQL query to find the average time between orders for each customer.**  
    **A:**  
    ```sql
    SELECT 
        customer_id,
        AVG(DATEDIFF(next_order_date, order_date)) as avg_days
    FROM (
        SELECT 
            customer_id,
            order_date,
            LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) as next_order_date
        FROM orders
    ) t
    WHERE next_order_date IS NOT NULL
    GROUP BY customer_id;
    ```

## FastAPI
21. **Q: How do you create a basic FastAPI application?**  
    **A:**  
    ```python
    from fastapi import FastAPI
    app = FastAPI()
    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}
    # Run with: uvicorn main:app --reload
    ```

22. **Q: How do you handle query parameters in FastAPI?**  
    **A:** Use function parameters with type hints. Example:  
    ```python
    from fastapi import FastAPI
    app = FastAPI()
    @app.get("/items/")
    async def read_items(skip: int = 0, limit: int = 10):
        return {"skip": skip, "limit": limit}
    ```

23. **Q: How do you implement dependency injection in FastAPI?**  
    **A:** Use `Depends` to inject dependencies. Example:  
    ```python
    from fastapi import FastAPI, Depends
    app = FastAPI()
    async def get_user():
        return {"user_id": 1}
    @app.get("/profile")
    async def profile(user: dict = Depends(get_user)):
        return {"user": user}
    ```

24. **Q: How do you validate request data in FastAPI?**  
    **A:** Use Pydantic models. Example:  
    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel
    app = FastAPI()
    class Item(BaseModel):
        name: str
        price: float
    @app.post("/items/")
    async def create_item(item: Item):
        return item
    ```

25. **Q: How do you handle errors in FastAPI?**  
    **A:** Use custom exception handlers. Example:  
    ```python
    from fastapi import FastAPI, HTTPException
    app = FastAPI()
    @app.exception_handler(HTTPException)
    async def custom_exception_handler(request, exc):
        return {"error": str(exc)}
    @app.get("/items/{id}")
    async def read_item(id: int):
        if id > 100:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"id": id}
    ```

26. **Q: How do you implement authentication in FastAPI?**  
    **A:** Use OAuth2 or JWT with dependencies. Example:  
    ```python
    from fastapi import FastAPI, Depends, HTTPException
    from fastapi.security import OAuth2PasswordBearer
    app = FastAPI()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    async def verify_token(token: str = Depends(oauth2_scheme)):
        if token != "valid-token":
            raise HTTPException(status_code=401, detail="Invalid token")
        return token
    @app.get("/secure")
    async def secure_endpoint(token: str = Depends(verify_token)):
        return {"token": token}
    ```

27. **Q: How do you add middleware in FastAPI?**  
    **A:** Use `@app.middleware`. Example:  
    ```python
    from fastapi import FastAPI
    app = FastAPI()
    @app.middleware("http")
    async def add_custom_header(request, call_next):
        response = await call_next(request)
        response.headers["X-Custom"] = "Value"
        return response
    ```

28. **Q: How do you integrate a database with FastAPI?**  
    **A:** Use an ORM like SQLAlchemy with async support. Example:  
    ```python
    from fastapi import FastAPI
    from sqlalchemy.ext.asyncio import AsyncSession
    app = FastAPI()
    async def get_db():
        async with AsyncSession(engine) as session:
            yield session
    @app.get("/users")
    async def read_users(db: AsyncSession = Depends(get_db)):
        return await db.execute("SELECT * FROM users")
    ```

29. **Q: How do you implement WebSocket in FastAPI?**  
    **A:** Use the `WebSocket` class. Example:  
    ```python
    from fastapi import FastAPI, WebSocket
    app = FastAPI()
    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        await websocket.send_text("Hello")
        await websocket.close()
    ```

30. **Q: How do you test a FastAPI application?**  
    **A:** Use `TestClient` from `fastapi.testclient`. Example:  
    ```python
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    app = FastAPI()
    @app.get("/")
    async def root():
        return {"message": "Hello"}
    client = TestClient(app)
    def test_root():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello"}
    ```

## Apache Airflow
31. **Q: What is Apache Airflow, and what are its core components?**  
   **A:** Apache Airflow is a workflow orchestration tool for scheduling and managing data pipelines. Core components include DAGs (Directed Acyclic Graphs), Tasks, Operators, Schedulers, Executors, and the Metadata Database.

32. **Q: How do you define a DAG in Apache Airflow?**  
   **A:** Use the `DAG` class with tasks defined using operators. Example:  
   ```python
   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from datetime import datetime
   def print_hello():
       print("Hello, Airflow!")
   with DAG('hello_dag', start_date=datetime(2025, 1, 1), schedule_interval='@daily') as dag:
       task = PythonOperator(task_id='print_hello', python_callable=print_hello)
   ```

33. **Q: How do you handle task dependencies in Airflow?**  
   **A:** Use `>>` or `set_upstream`/`set_downstream`. Example:  
   ```python
   task1 = PythonOperator(task_id='task1', python_callable=func1, dag=dag)
   task2 = PythonOperator(task_id='task2', python_callable=func2, dag=dag)
   task1 >> task2
   ```

34. **Q: What is an Airflow Operator, and name a few types.**  
   **A:** Operators define tasks in a DAG. Types include `PythonOperator`, `BashOperator`, `SqlOperator`, and `HttpOperator`.

35. **Q: How do you trigger a DAG manually in Airflow?**  
   **A:** Use the CLI: `airflow dags trigger -d <dag_id>` or via the Airflow UI.

36. **Q: How do you use XComs in Airflow to share data between tasks?**  
   **A:** Use `xcom_push` and `xcom_pull`. Example:  
   ```python
   def push_data(ti):
       ti.xcom_push(key='value', value=42)
   def pull_data(ti):
       value = ti.xcom_pull(key='value')
       print(value)
   ```

37. **Q: How do you implement branching in Airflow?**  
   **A:** Use `BranchPythonOperator`. Example:  
   ```python
   from airflow.operators.python import BranchPythonOperator
   def branch_func():
       return 'task_a' if some_condition else 'task_b'
   branch_task = BranchPythonOperator(task_id='branch', python_callable=branch_func, dag=dag)
   ```

38. **Q: How do you monitor and debug Airflow DAGs?**  
   **A:** Use the Airflow UI to check task logs, status, and dependencies. Enable logging (`logging.INFO`) and use `airflow logs <dag_id> <task_id>` for debugging.

39. **Q: How do you scale Airflow for large workflows?**  
   **A:** Use CeleryExecutor with Redis/RabbitMQ, scale workers, and optimize the Metadata Database (e.g., PostgreSQL) with indexing.

40. **Q: How do you integrate Airflow with external systems like AWS S3?**  
   **A:** Use `S3Hook` or `S3FileSensor`. Example:  
   ```python
   from airflow.providers.amazon.aws.operators.s3 import S3FileSensor
   s3_sensor = S3FileSensor(task_id='check_s3', bucket_name='my-bucket', bucket_key='file.csv', dag=dag)
   ```

## Azure Functions
41. **Q: What are Azure Functions, and when would you use them?**  
   **A:** Azure Functions is a serverless compute service for running event-driven code. Use cases include data processing, API endpoints, and scheduled tasks.

42. **Q: How do you create a Python Azure Function?**  
   **A:** Use the Azure Functions Core Tools. Example `function.json`:  
   ```json
   {
       "scriptFile": "__init__.py",
       "bindings": [
           {
               "authLevel": "anonymous",
               "type": "httpTrigger",
               "direction": "in",
               "name": "req",
               "methods": ["get"]
           },
           {
               "type": "http",
               "direction": "out",
               "name": "$return"
           }
       ]
   }
   ```  
   `__init__.py`:  
   ```python
   import azure.functions as func
   def main(req: func.HttpRequest) -> func.HttpResponse:
       return func.HttpResponse("Hello, Azure!")
   ```

43. **Q: How do you trigger an Azure Function with a timer?**  
   **A:** Use a timer trigger. Example `function.json`:  
   ```json
   {
       "scriptFile": "__init__.py",
       "bindings": [
           {
               "name": "timer",
               "type": "timerTrigger",
               "direction": "in",
               "schedule": "0 */5 * * * *"
           }
       ]
   }
   ```  
   `__init__.py`:  
   ```python
   import azure.functions as func
   def main(timer: func.TimerRequest) -> None:
       print("Timer triggered")
   ```

44. **Q: How do you integrate Azure Functions with Azure Blob Storage?**  
   **A:** Use a Blob trigger or input/output bindings. Example `function.json`:  
   ```json
   {
       "scriptFile": "__init__.py",
       "bindings": [
           {
               "name": "inputblob",
               "type": "blobTrigger",
               "direction": "in",
               "path": "input/{name}",
               "connection": "AzureWebJobsStorage"
           }
       ]
   }
   ```  
   `__init__.py`:  
   ```python
   import azure.functions as func
   def main(inputblob: func.InputStream):
       print(f"Blob: {inputblob.name}")
   ```

45. **Q: How do you secure an Azure Function?**  
   **A:** Use function keys, Azure AD authentication, or API Management. Example with function key:  
   ```python
   import azure.functions as func
   def main(req: func.HttpRequest) -> func.HttpResponse:
       if not req.headers.get("x-functions-key"):
           return func.HttpResponse("Unauthorized", status_code=401)
       return func.HttpResponse("Authorized")
   ```

46. **Q: How do you handle errors in Azure Functions?**  
   **A:** Use try-except blocks and return appropriate HTTP responses. Example:  
   ```python
   import azure.functions as func
   def main(req: func.HttpRequest) -> func.HttpResponse:
       try:
           data = req.get_json()
           return func.HttpResponse("Success")
       except ValueError:
           return func.HttpResponse("Invalid JSON", status_code=400)
   ```

47. **Q: How do you scale Azure Functions?**  
   **A:** Azure Functions scales automatically with the Consumption Plan. For high throughput, use Premium Plan or Dedicated App Service Plan and configure auto-scaling rules.

48. **Q: How do you test an Azure Function locally?**  
   **A:** Use Azure Functions Core Tools: `func start`. Write unit tests with `unittest` or `pytest`. Example:  
   ```python
   import azure.functions as func
   def main(req: func.HttpRequest) -> func.HttpResponse:
       return func.HttpResponse("Test")
   # Test with: func start
   ```

49. **Q: How do you integrate Azure Functions with Azure Cosmos DB?**  
   **A:** Use Cosmos DB bindings. Example `function.json`:  
   ```json
   {
       "scriptFile": "__init__.py",
       "bindings": [
           {
               "name": "doc",
               "type": "cosmosDB",
               "direction": "out",
               "databaseName": "mydb",
               "collectionName": "mycollection",
               "connectionStringSetting": "CosmosDBConnection"
           }
       ]
   }
   ```  
   `__init__.py`:  
   ```python
   import azure.functions as func
   def main(req: func.HttpRequest, doc: func.Out[func.Document]):
       doc.set(func.Document.from_dict({"id": "1", "data": "test"}))
   ```

50. **Q: How do you monitor Azure Functions?**  
   **A:** Use Azure Monitor and Application Insights to track metrics, logs, and performance. Enable insights in `host.json`:  
   ```json
   {
       "version": "2.0",
       "extensionBundle": {
           "id": "Microsoft.Azure.Functions.ExtensionBundle",
           "version": "[2.*, 3.0.0)"
       },
       "logging": {
           "applicationInsights": {
               "samplingSettings": {
                   "isEnabled": true
               }
           }
       }
   }
   ```

## Data Structures and Algorithms
51. **Q: Implement a function to find the lowest common ancestor in a binary tree.**  
    **A:**  
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def lowest_common_ancestor(root, p, q):
        if not root or root == p or root == q:
            return root
        left = lowest_common_ancestor(root.left, p, q)
        right = lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        return left or right
    ```

52. **Q: Write a function to implement a queue using two stacks.**  
    **A:**  
    ```python
    class Queue:
        def __init__(self):
            self.stack1 = []
            self.stack2 = []
        def enqueue(self, x):
            self.stack1.append(x)
        def dequeue(self):
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop() if self.stack2 else None
    ```

53. **Q: Implement a function to find the shortest subarray with a given sum.**  
    **A:**  
    ```python
    def shortest_subarray(nums, target):
        n = len(nums)
        min_length = n + 1
        curr_sum = 0
        left = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_length if min_length <= n else -1
    print(shortest_subarray([1, 4, 2, 3, 5], 9))  # 2
    ```

54. **Q: Write a function to check if a graph is bipartite.**  
    **A:**  
    ```python
    from collections import deque
    def is_bipartite(graph):
        colors = {}
        for node in graph:
            if node not in colors:
                colors[node] = 0
                queue = deque([node])
                while queue:
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in colors:
                            colors[neighbor] = 1 - colors[curr]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[curr]:
                            return False
        return True
    ```

55. **Q: Implement a function to find the longest increasing subsequence.**  
    **A:**  
    ```python
    def length_of_lis(nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    ```

56. **Q: Write a function to implement a binary search tree iterator.**  
    **A:**  
    ```python
    class BSTIterator:
        def __init__(self, root):
            self.stack = []
            self._push_left(root)
        def _push_left(self, node):
            while node:
                self.stack.append(node)
                node = node.left
        def next(self):
            node = self.stack.pop()
            self._push_left(node.right)
            return node.val
        def hasNext(self):
            return len(self.stack) > 0
    ```

57. **Q: Implement a function to find the maximum product subarray.**  
    **A:**  
    ```python
    def max_product(nums):
        max_prod = min_prod = result = nums[0]
        for num in nums[1:]:
            temp_max = max(num, max_prod * num, min_prod * num)
            min_prod = min(num, max_prod * num, min_prod * num)
            max_prod = temp_max
            result = max(result, max_prod)
        return result
    print(max_product([-2, 0, -1]))  # 0
    ```

58. **Q: Write a function to detect if a string has valid parentheses.**  
    **A:**  
    ```python
    def is_valid(s):
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or (char == ')' and stack[-1] != '(') or \
                   (char == '}' and stack[-1] != '{') or \
                   (char == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack
    print(is_valid("()[]{}"))  # True
    ```

59. **Q: Implement a function to find the k closest points to the origin.**  
    **A:**  
    ```python
    from heapq import heappush, heappop
    def k_closest(points, k):
        heap = []
        for x, y in points:
            dist = x*x + y*y
            heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heappop(heap)
        return [[x, y] for _, x, y in heap]
    print(k_closest([[1, 3], [-2, 2]], 1))  # [[-2, 2]]
    ```

60. **Q: Write a function to implement a sliding window maximum.**  
    **A:**  
    ```python
    from collections import deque
    def max_sliding_window(nums, k):
        result = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    ```

## System Design and Leadership
61. **Q: How would you design a real-time analytics dashboard?**  
    **A:** Use FastAPI for the API, Apache Airflow for ETL pipelines, and Azure Functions for event-driven processing. Store data in a time-series database (e.g., InfluxDB), cache with Redis, and visualize with Grafana. Scale with Kubernetes and monitor with Azure Monitor.

62. **Q: How do you lead a team to adopt a new technology like FastAPI?**  
    **A:** Conduct a POC to demonstrate benefits, provide training sessions, create reusable templates, and integrate with CI/CD pipelines. Assign mentors to junior developers and track adoption through code reviews and metrics.

63. **Q: How do you handle conflicts between team members on architectural decisions?**  
    **A:** Facilitate discussions to understand both sides, evaluate options with prototypes or benchmarks, and align decisions with project goals. Document the rationale and ensure consensus or escalation if needed.

64. **Q: How do you ensure a Python project is production-ready?**  
    **A:** Implement unit tests (`pytest`), static analysis (`flake8`), CI/CD pipelines (GitHub Actions), and monitoring (Prometheus). Use Docker for consistent environments and validate performance with load testing.

65. **Q: How would you design a fault-tolerant microservices architecture?**  
    **A:** Use FastAPI for services, Kafka for event streaming, and Kubernetes for orchestration. Implement circuit breakers, retries, and fallback mechanisms. Monitor with Azure Application Insights and ensure data consistency with eventual consistency models.

66. **Q: How do you mentor a team to improve code quality?**  
    **A:** Enforce coding standards (PEP 8), conduct regular code reviews, introduce tools like `black` and `isort`, and promote test-driven development. Share best practices through workshops and pair programming.

67. **Q: How do you optimize an Airflow DAG for performance?**  
    **A:** Minimize task dependencies, use `SubDagOperator` for modularity, optimize task execution with `Pool` for resource limits, and tune the scheduler with appropriate configurations.

68. **Q: How do you manage technical debt in a long-running project?**  
    **A:** Prioritize debt based on impact, allocate refactoring sprints, use tools like SonarQube, and document debt in a backlog. Communicate trade-offs to stakeholders to balance feature delivery and maintenance.

69. **Q: How do you implement CI/CD for a FastAPI application on Azure?**  
    **A:** Use GitHub Actions to build, test, and deploy to Azure App Service. Example workflow:  
    ```yaml
    name: Deploy FastAPI
    on: [push]
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: pip install -r requirements.txt
          - name: Run tests
            run: pytest
          - name: Deploy to Azure
            uses: azure/webapps-deploy@v2
            with:
              app-name: my-fastapi-app
              slot-name: production
              publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
    ```

70. **Q: How do you ensure compliance with data privacy regulations in a Python application?**  
    **A:** Encrypt sensitive data (e.g., `cryptography` library), implement role-based access control, log access with `logging`, and anonymize data for analytics. Use Azure Key Vault for secrets management.

## Coding Challenges
71. **Q: Write a function to find the longest common prefix in a list of strings.**  
    **A:**  
    ```python
    def longest_common_prefix(strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
        return shortest
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    ```

72. **Q: Implement a function to group strings by their character frequency.**  
    **A:**  
    ```python
    from collections import Counter
    def group_by_frequency(strs):
        groups = {}
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            groups[key] = groups.get(key, []) + [s]
        return list(groups.values())
    print(group_by_frequency(["cat", "act", "dog"]))  # [['cat', 'act'], ['dog']]
    ```

73. **Q: Write a function to find the median of a stream of numbers.**  
    **A:**  
    ```python
    from heapq import heappush, heappop
    class MedianFinder:
        def __init__(self):
            self.small = []  # max heap
            self.large = []  # min heap
        def add_num(self, num):
            heappush(self.small, -num)
            heappush(self.large, -heappop(self.small))
            if len(self.large) > len(self.small):
                heappush(self.small, -heappop(self.large))
        def find_median(self):
            if len(self.small) > len(self.large):
                return -self.small[0]
            return (-self.small[0] + self.large[0]) / 2
    ```

74. **Q: Implement a function to find the kth smallest element in a BST.**  
    **A:**  
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def kth_smallest(root, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        return inorder(root)[k-1]
    ```

75. **Q: Write a function to implement a priority queue.**  
    **A:**  
    ```python
    from heapq import heappush, heappop
    class PriorityQueue:
        def __init__(self):
            self.heap = []
        def push(self, priority, item):
            heappush(self.heap, (priority, item))
        def pop(self):
            return heappop(self.heap)[1] if self.heap else None
    ```

76. **Q: Implement a function to reverse a string in-place.**  
    **A:**  
    ```python
    def reverse_string(s):
        s[:] = s[::-1]
        return s
    print(reverse_string(['h', 'e', 'l', 'l', 'o']))  # ['o', 'l', 'l', 'e', 'h']
    ```

77. **Q: Write a function to find the maximum depth of a binary tree.**  
    **A:**  
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def max_depth(root):
        if not root:
            return 0
        return max(max_depth(root.left), max_depth(root.right)) + 1
    ```

78. **Q: Implement a function to check if a string is a valid palindrome ignoring non-alphanumeric characters.**  
    **A:**  
    ```python
    def is_valid_palindrome(s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
    ```

79. **Q: Write a function to merge intervals.**  
    **A:**  
    ```python
    def merge_intervals(intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
    ```

80. **Q: Implement a function to find the top k frequent words.**  
    **A:**  
    ```python
    from collections import Counter
    from heapq import heappush, heappop
    def top_k_frequent_words(words, k):
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heappush(heap, (-freq, word))
        return [heappop(heap)[1] for _ in range(k)]
    print(top_k_frequent_words(["i", "love", "i", "love", "coding"], 2))  # ["i", "love"]
    ```

## Behavioral and Leadership Questions
81. **Q: How do you handle a situation where a critical deadline is at risk?**  
    **A:** Assess the scope, identify blockers, and prioritize tasks. Communicate with stakeholders to renegotiate timelines or resources, and delegate tasks to balance workload. In a past project, I restructured tasks and added temporary resources to meet a deadline.

82. **Q: Describe a time you improved a process in your team.**  
    **A:** I introduced automated testing with `pytest` in a legacy project, reducing manual testing time by 40%. I trained the team and integrated tests into the CI/CD pipeline, improving delivery speed.

83. **Q: How do you balance technical excellence with business priorities?**  
    **A:** Align technical decisions with business goals, using metrics to justify investments in quality. For example, I advocated for refactoring a critical module, demonstrating a 20% performance gain that improved user satisfaction.

84. **Q: How do you foster collaboration in a distributed team?**  
    **A:** Use tools like Slack and JIRA for communication, schedule regular syncs, and promote pair programming. I led a distributed team by setting clear goals and using retrospectives to address communication gaps.

85. **Q: Describe a time you resolved a performance issue in production.**  
    **A:** A slow API was identified using New Relic. I optimized database queries with indexing and caching, reducing response time from 2s to 200ms, and communicated the fix to stakeholders.

86. **Q: How do you onboard a new developer to a complex codebase?**  
    **A:** Provide documentation, assign a mentor, and start with small tasks. I created a wiki for a Python project and paired new hires with seniors, reducing onboarding time by 30%.

87. **Q: How do you handle scope creep in a project?**  
    **A:** Document requirements, use change control processes, and communicate impacts to stakeholders. In a past project, I negotiated to defer non-critical features to the next sprint, keeping the timeline intact.

88. **Q: How do you ensure your team stays updated with new technologies?**  
    **A:** Organize tech talks, allocate time for learning, and encourage certifications. I led a team to adopt FastAPI by conducting workshops and integrating it into a pilot project.

89. **Q: Describe a time you had to push back on unrealistic requirements.**  
    **A:** A client requested a feature in an impossible timeline. I presented a technical analysis showing risks and proposed a phased approach, which was accepted, ensuring quality delivery.

90. **Q: How do you measure the success of a technical project?**  
    **A:** Use KPIs like performance metrics, user satisfaction, and delivery timelines. In a recent project, I tracked API latency and error rates, achieving a 99.9% uptime target.

## Additional Technical Questions
91. **Q: How do you implement rate limiting in Airflow?**  
    **A:** Use task pools to limit concurrent tasks. Example:  
    ```python
    from airflow import DAG
    from airflow.operators.dummy import DummyOperator
    dag = DAG('rate_limit_dag', start_date=datetime(2025, 1, 1))
    with dag:
        task = DummyOperator(task_id='task', pool='limited_pool')
    # Set pool in airflow.cfg: [pools] limited_pool = 2
    ```

92. **Q: How do you handle large datasets in FastAPI?**  
    **A:** Use streaming responses and async I/O. Example:  
    ```python
    from fastapi import FastAPI
    from fastapi.responses import StreamingResponse
    app = FastAPI()
    async def data_stream():
        for i in range(1000000):
            yield f"Data {i}\n"
    @app.get("/stream")
    async def stream_data():
        return StreamingResponse(data_stream(), media_type="text/plain")
    ```

93. **Q: How do you optimize SQL queries for large datasets?**  
    **A:** Use indexing, partitioning, and query optimization techniques like avoiding `SELECT *`. Example:  
    ```sql
    CREATE INDEX idx_customer_id ON orders(customer_id);
    SELECT customer_id, SUM(amount)
    FROM orders
    WHERE order_date >= '2025-01-01'
    GROUP BY customer_id;
    ```

94. **Q: How do you implement retry logic in Azure Functions?**  
    **A:** Use `azure-functions-durable` for retries. Example:  
    ```python
    import azure.durable_functions as df
    def orchestrator_function(context: df.DurableOrchestrationContext):
        retries = 3
        for _ in range(retries):
            try:
                yield context.call_activity("MyActivity")
                break
            except Exception:
                if _ < retries - 1:
                    yield context.create_timer(context.current_utc_datetime + timedelta(seconds=10))
                else:
                    raise
    ```

95. **Q: How do you handle versioning in a FastAPI application?**  
    **A:** Use path prefixes or APIRouter. Example:  
    ```python
    from fastapi import FastAPI, APIRouter
    app = FastAPI()
    v1_router = APIRouter(prefix="/v1")
    @v1_router.get("/items")
    async def get_items_v1():
        return ["item1", "item2"]
    app.include_router(v1_router)
    ```

96. **Q: How do you schedule tasks in Airflow with dynamic parameters?**  
    **A:** Use `Variable` or `Connection`. Example:  
    ```python
    from airflow.models import Variable
    params = Variable.get("my_params", deserialize_json=True)
    task = PythonOperator(task_id='dynamic_task', python_callable=lambda: print(params), dag=dag)
    ```

97. **Q: How do you integrate FastAPI with Apache Kafka?**  
    **A:** Use `aiokafka`. Example:  
    ```python
    from fastapi import FastAPI
    from aiokafka import AIOKafkaProducer
    app = FastAPI()
    async def send_message(message: str):
        producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
        await producer.start()
        await producer.send_and_wait("my_topic", message.encode())
        await producer.stop()
    @app.post("/send")
    async def send_to_kafka(message: str):
        await send_message(message)
        return {"status": "sent"}
    ```

98. **Q: How do you implement logging in Azure Functions?**  
    **A:** Use the `logging` module. Example:  
    ```python
    import azure.functions as func
    import logging
    def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info("Function triggered")
        return func.HttpResponse("Logged")
    ```

99. **Q: How do you handle backpressure in Airflow?**  
    **A:** Use task concurrency limits and `max_active_runs` in DAG configuration. Example:  
    ```python
    dag = DAG('backpressure_dag', max_active_runs=1, concurrency=2, start_date=datetime(2025, 1, 1))
    ```

100. **Q: How do you secure sensitive data in Airflow?**  
     **A:** Store secrets in Airflow Variables or Connections, encrypted in the Metadata Database. Example:  
     ```python
     from airflow.models import Connection
     conn = Connection(conn_id='my_db', conn_type='postgres', host='localhost', login='user', password='pass')
     ```
