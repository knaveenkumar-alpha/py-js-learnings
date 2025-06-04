# Senior Software Developer and Lead Python Interview Questions (Part 2)

## Advanced Python Concepts
1. **Q: What is the difference between `__new__` and `__init__` in Python?**  
   **A:** `__new__` is a static method responsible for creating a new instance of a class, called before `__init__`. `__init__` initializes the instance after creation. Example:  
   ```python
   class Singleton:
       _instance = None
       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
           return cls._instance
       def __init__(self):
           self.value = 42
   ```

2. **Q: Explain the use of `metaclasses` in Python.**  
   **A:** Metaclasses are classes of classes, used to customize class creation. They are defined using `type` or by inheriting from `type`. Example:  
   ```python
   class MetaClass(type):
       def __new__(cls, name, bases, attrs):
           attrs['custom_attr'] = 100
           return super().__new__(cls, name, bases, attrs)
   class MyClass(metaclass=MetaClass):
       pass
   print(MyClass.custom_attr)  # 100
   ```

3. **Q: What is the purpose of the `@property` decorator in Python?**  
   **A:** The `@property` decorator allows methods to be accessed like attributes, enabling getter, setter, and deleter functionality. Example:  
   ```python
   class Circle:
       def __init__(self, radius):
           self._radius = radius
       @property
       def radius(self):
           return self._radius
       @radius.setter
       def radius(self, value):
           if value > 0:
               self._radius = value
   c = Circle(5)
   print(c.radius)  # 5
   c.radius = 10
   ```

4. **Q: How does Python’s `contextlib` module work for creating context managers?**  
   **A:** The `contextlib` module provides utilities like `@contextmanager` to create context managers using generators. Example:  
   ```python
   from contextlib import contextmanager
   @contextmanager
   def temp_file():
       print("Opening file")
       yield "temp.txt"
       print("Closing file")
   with temp_file() as f:
       print(f"Working with {f}")
   ```

5. **Q: What is the difference between `__getattr__` and `__getattribute__`?**  
   **A:** `__getattr__` is called when an attribute is not found through normal lookup, while `__getattribute__` is called for every attribute access. Example:  
   ```python
   class MyClass:
       def __getattr__(self, name):
           return f"Attribute {name} not found"
       def __getattribute__(self, name):
           print(f"Accessing {name}")
           return super().__getattribute__(name)
   ```

6. **Q: Explain Python’s descriptor protocol.**  
   **A:** Descriptors are objects that define `__get__`, `__set__`, or `__delete__` methods to control attribute access. Example:  
   ```python
   class Descriptor:
       def __get__(self, obj, owner):
           return obj._value
       def __set__(self, obj, value):
           obj._value = value
   class MyClass:
       value = Descriptor()
   obj = MyClass()
   obj.value = 42
   print(obj.value)  # 42
   ```

7. **Q: How do you handle exceptions in Python effectively?**  
   **A:** Use specific exception types, avoid bare `except`, and use `finally` or `else` for cleanup or success cases. Example:  
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError as e:
       print(f"Error: {e}")
   else:
       print("Success")
   finally:
       print("Cleanup")
   ```

8. **Q: What is the purpose of `collections.namedtuple`?**  
   **A:** `namedtuple` creates tuple subclasses with named fields, improving readability. Example:  
   ```python
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(1, 2)
   print(p.x, p.y)  # 1 2
   ```

9. **Q: Explain the `itertools` module and provide an example.**  
   **A:** `itertools` provides tools for efficient iteration, like `chain`, `permutations`, or `combinations`. Example:  
   ```python
   from itertools import chain
   print(list(chain([1, 2], [3, 4])))  # [1, 2, 3, 4]
   ```

10. **Q: How do you implement a custom iterator in Python?**  
    **A:** Define `__iter__` and `__next__` methods. Example:  
    ```python
    class Counter:
        def __init__(self, max):
            self.max = max
            self.current = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.current < self.max:
                self.current += 1
                return self.current
            raise StopIteration
    for num in Counter(3):
        print(num)  # 1, 2, 3
    ```

## Data Structures and Algorithms
11. **Q: Implement a function to find the shortest path in a weighted graph (Dijkstra’s algorithm).**  
    **A:**  
    ```python
    from heapq import heappush, heappop
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            curr_dist, curr = heappop(pq)
            if curr_dist > distances[curr]:
                continue
            for neighbor, weight in graph[curr].items():
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(pq, (distance, neighbor))
        return distances
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2}, 'C': {}}
    print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3}
    ```

12. **Q: Write a function to detect a cycle in a directed graph.**  
    **A:**  
    ```python
    def has_cycle(graph):
        visited = set()
        rec_stack = set()
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(has_cycle(graph))  # True
    ```

13. **Q: Implement a function to find the longest common subsequence of two strings.**  
    **A:**  
    ```python
    def lcs(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
    print(lcs("ABCDGH", "AEDFHR"))  # 4
    ```

14. **Q: Write a function to rotate a matrix by 90 degrees.**  
    **A:**  
    ```python
    def rotate_matrix(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix))  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    ```

15. **Q: Implement a function to find the intersection of two sorted arrays.**  
    **A:**  
    ```python
    def intersect_arrays(arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                result.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        return result
    print(intersect_arrays([1, 2, 2, 3], [2, 2, 4]))  # [2, 2]
    ```

16. **Q: Write a function to check if a binary tree is balanced.**  
    **A:**  
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def is_balanced(root):
        def check_height(node):
            if not node:
                return 0
            left = check_height(node.left)
            if left == -1:
                return -1
            right = check_height(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check_height(root) != -1
    ```

17. **Q: Implement a function to find the maximum subarray sum (Kadane’s algorithm).**  
    **A:**  
    ```python
    def max_subarray_sum(nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    ```

18. **Q: Write a function to compute the factorial of a number using recursion and iteration.**  
    **A:**  
    ```python
    def factorial_recursive(n):
        if n <= 1:
            return 1
        return n * factorial_recursive(n - 1)
    def factorial_iterative(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    print(factorial_recursive(5))  # 120
    print(factorial_iterative(5))  # 120
    ```

19. **Q: Implement a trie (prefix tree) to store and search words.**  
    **A:**  
    ```python
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
    class Trie:
        def __init__(self):
            self.root = TrieNode()
        def insert(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        def search(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node.is_end
    trie = Trie()
    trie.insert("hello")
    print(trie.search("hello"))  # True
    ```

20. **Q: Write a function to find the minimum window substring containing all characters of another string.**  
    **A:**  
    ```python
    from collections import Counter
    def min_window(s, t):
        if not s or not t:
            return ""
        t_count = Counter(t)
        required = len(t_count)
        window = {}
        formed = 0
        left = right = 0
        min_len = float('inf')
        min_window_sub = ""
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_sub = s[left:right + 1]
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    formed -= 1
                left += 1
            right += 1
        return min_window_sub
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    ```

## System Design and Leadership
21. **Q: How would you design a scalable notification system?**  
    **A:** Use a message queue (e.g., Kafka, RabbitMQ) for asynchronous notifications, a microservices architecture for components (user service, notification service), and a database (e.g., MongoDB) for user preferences. Implement push notifications via WebSocket or Firebase, with Redis for caching and load balancers for scalability.

22. **Q: Explain how you’d lead a team to migrate a monolithic Python application to microservices.**  
    **A:** Break down the monolith into services based on business domains, use Flask or FastAPI for lightweight APIs, containerize with Docker, and orchestrate with Kubernetes. Assign tasks based on team strengths, set milestones, and use CI/CD for deployment. Communicate progress to stakeholders regularly.

23. **Q: How do you ensure high availability in a Python-based system?**  
    **A:** Use load balancers, redundant servers, and failover mechanisms. Implement health checks in Flask/Django, use circuit breakers (e.g., `pybreaker`), and deploy on cloud platforms like AWS with auto-scaling. Monitor with tools like Prometheus and Grafana.

24. **Q: How do you handle technical debt as a lead developer?**  
    **A:** Prioritize debt based on impact (e.g., performance, maintainability). Allocate time in sprints for refactoring, enforce coding standards, and use tools like SonarQube. Communicate the importance of addressing debt to stakeholders to secure resources.

25. **Q: Design a rate-limiting middleware for a Flask application.**  
    **A:**  
    ```python
    from flask import Flask, request
    from collections import defaultdict
    import time
    app = Flask(__name__)
    requests = defaultdict(list)
    def rate_limit(max_requests, window_seconds):
        def decorator(f):
            def wrapped_function(*args, **kwargs):
                client_ip = request.remote_addr
                now = time.time()
                requests[client_ip] = [t for t in requests[client_ip] if t > now - window_seconds]
                if len(requests[client_ip]) >= max_requests:
                    return "Rate limit exceeded", 429
                requests[client_ip].append(now)
                return f(*args, **kwargs)
            return wrapped_function
        return decorator
    @app.route('/')
    @rate_limit(max_requests=5, window_seconds=60)
    def index():
        return "Success"
    ```

26. **Q: How do you mentor junior developers in Python best practices?**  
    **A:** Teach PEP 8, unit testing with `pytest`, and modular design. Conduct code reviews, pair program on complex tasks, and encourage learning through online platforms like Real Python or internal hackathons. Provide constructive feedback and set clear goals.

27. **Q: How would you implement a distributed task queue in Python?**  
    **A:** Use Celery with RabbitMQ or Redis as the broker. Example:  
    ```python
    from celery import Celery
    app = Celery('tasks', broker='redis://localhost:6379/0')
    @app.task
    def process_data(data):
        return f"Processed {data}"
    ```

28. **Q: Explain the role of a lead developer in Agile teams.**  
    **A:** A lead developer guides technical decisions, ensures code quality, mentors team members, and aligns development with business goals. They facilitate sprint planning, resolve blockers, and communicate with product owners to refine requirements.

29. **Q: How do you optimize a Python application for low latency?**  
    **A:** Profile with `cProfile`, optimize bottlenecks, use async I/O with `asyncio`, cache results with Redis, and minimize database queries. Use compiled extensions (e.g., Cython) for performance-critical code.

30. **Q: How do you ensure security in a Python-based API?**  
    **A:** Use JWT or OAuth for authentication, validate inputs with libraries like `marshmallow`, sanitize data, enable CORS properly, and use HTTPS. Regularly scan for vulnerabilities with tools like `bandit`.[](https://www.ambitionbox.com/salaries/epam-systems-salaries)

## Behavioral and Leadership Questions
31. **Q: How do you prioritize tasks in a project with tight deadlines?**  
    **A:** Assess tasks based on impact and dependencies, use MoSCoW prioritization, and delegate effectively. Communicate with stakeholders to align expectations and adjust scope if needed.

32. **Q: Describe a time you led a team through a critical production issue.**  
    **A:** In a previous role, a memory leak crashed our app. I led the team to identify the issue using `tracemalloc`, implemented a fix, and deployed it with zero downtime. I communicated updates to clients and conducted a post-mortem to prevent recurrence.

33. **Q: How do you handle underperforming team members?**  
    **A:** Identify root causes through one-on-one discussions, provide targeted feedback, and offer resources like training. Set clear performance goals and monitor progress, balancing empathy with accountability.

34. **Q: How do you ensure alignment between technical and business teams?**  
    **A:** Translate technical concepts into business value during meetings, involve stakeholders in sprint reviews, and use tools like JIRA for transparency. Regular syncs prevent miscommunication.

35. **Q: Describe a time you introduced a new technology to your team.**  
    **A:** I introduced FastAPI to replace a slower Flask API. I conducted a POC, demonstrated performance gains, trained the team, and migrated incrementally, reducing latency by 30%.

## Coding Challenges
36. **Q: Implement a function to validate a password (length 20-40, specific characters).**  
    **A:**  
    ```python
    def validate_password(password):
        if not 20 <= len(password) <= 40:
            return False
        return bool(password.isalnum())
    print(validate_password("abc123" * 5))  # True
    print(validate_password("abc"))  # False
    ```[](https://www.geeksforgeeks.org/epam-interview-experience-2024-on-campus/)

37. **Q: Write a function to find the top k frequent elements in an array.**  
    **A:**  
    ```python
    from collections import Counter
    def top_k_frequent(nums, k):
        return [num for num, _ in Counter(nums).most_common(k)]
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    ```

38. **Q: Implement a function to check if two strings are anagrams.**  
    **A:**  
    ```python
    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    print(are_anagrams("listen", "silent"))  # True
    ```

39. **Q: Write a function to implement a stack using two queues.**  
    **A:**  
    ```python
    from collections import deque
    class Stack:
        def __init__(self):
            self.q1 = deque()
            self.q2 = deque()
        def push(self, x):
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
            self.q1, self.q2 = self.q2, self.q1
        def pop(self):
            return self.q1.popleft() if self.q1 else None
    ```

40. **Q: Implement a function to reverse words in a string.**  
    **A:**  
    ```python
    def reverse_words(s):
        return ' '.join(word[::-1] for word in s.split())
    print(reverse_words("Hello World"))  # "olleH dlroW"
    ```

41. **Q: Write a function to compute the Fibonacci sequence using dynamic programming.**  
    **A:**  
    ```python
    def fib_dp(n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    print(fib_dp(6))  # 8
    ```

42. **Q: Implement a function to find the first missing positive integer.**  
    **A:**  
    ```python
    def first_missing_positive(nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
    print(first_missing_positive([3, 4, -1, 1]))  # 2
    ```

43. **Q: Write a function to merge k sorted lists.**  
    **A:**  
    ```python
    from heapq import heappush, heappop
    def merge_k_lists(lists):
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst[0], i, 0))
        result = []
        while heap:
            val, list_idx, idx = heappop(heap)
            result.append(val)
            if idx + 1 < len(lists[list_idx]):
                heappush(heap, (lists[list_idx][idx + 1], list_idx, idx + 1))
        return result
    print(merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))  # [1, 1, 2, 3, 4, 4, 5, 6]
    ```

44. **Q: Implement a function to check if a number is a power of two.**  
    **A:**  
    ```python
    def is_power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
    print(is_power_of_two(16))  # True
    ```

45. **Q: Write a function to find the longest valid parentheses substring.**  
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
    print(longest_valid_parentheses("(()))"))  # 4
    ```

## Database and DevOps
46. **Q: Write a SQL query to find the top 3 employees with the highest salary per department.**  
    **A:**  
    ```sql
    SELECT 
        d.department_name,
        e.employee_name,
        e.salary
    FROM employees e
    JOIN departments d ON e.department_id = d.department_id
    WHERE (
        SELECT COUNT(DISTINCT e2.salary)
        FROM employees e2
        WHERE e2.department_id = e.department_id AND e2.salary > e.salary
    ) < 3
    ORDER BY d.department_name, e.salary DESC;
    ```

47. **Q: How do you optimize a Python script interacting with a database?**  
    **A:** Use connection pooling, batch queries, and prepared statements. In Python, use an ORM like SQLAlchemy with `bulk_insert_mappings` for efficiency and avoid N+1 query issues.

48. **Q: Explain how you’d set up a Docker container for a Python application.**  
    **A:** Create a `Dockerfile`:  
    ```dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "app.py"]
    ```
    Build and run with `docker build -t myapp .` and `docker run -p 5000:5000 myapp`.

49. **Q: How do you implement logging in a Python application?**  
    **A:** Use the `logging` module with handlers for file and console output. Example:  
    ```python
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('app.log'), logging.StreamHandler()]
    )
    logging.info("Application started")
    ```

50. **Q: Describe your experience with CI/CD pipelines for Python projects.**  
    **A:** I’ve implemented CI/CD using GitHub Actions, running tests with `pytest`, linting with `flake8`, and deploying to AWS ECS. Example workflow:  
    ```yaml
    name: CI/CD
    on: [push]
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v3
          - name: Set up Python
            uses: actions/setup-python@v4
            with:
              python-version: '3.9'
          - name: Install dependencies
            run: pip install -r requirements.txt
          - name: Lint
            run: flake8 .
          - name: Test
            run: pytest
          - name: Deploy
            run: aws ecs update-service --cluster my-cluster --service my-service --force-new-deployment
    ```
