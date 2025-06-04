# Senior Software Developer Python Interview Questions

## Python Fundamentals
1. **Q: Explain the difference between a list and a tuple in Python.**  
   **A:** A list is mutable, meaning its elements can be modified, added, or removed. A tuple is immutable, so its elements cannot be changed after creation. Lists are defined with square brackets `[]`, while tuples use parentheses `()`. Tuples are generally more memory-efficient and used for fixed data, while lists are used for dynamic data. Example:  
   ```python
   lst = [1, 2, 3]
   lst[0] = 4  # Valid
   tup = (1, 2, 3)
   tup[0] = 4  # Error: TypeError
   ```

2. **Q: What is the difference between `deepcopy` and `shallowcopy` in Python?**  
   **A:** A shallow copy (`copy.copy()`) creates a new object but references the same nested objects, so changes to nested objects affect both the original and the copy. A deep copy (`copy.deepcopy()`) creates a completely independent copy, including nested objects. Example:  
   ```python
   import copy
   lst = [[1, 2], 3]
   shallow = copy.copy(lst)
   deep = copy.deepcopy(lst)
   shallow[0][0] = 9  # Affects original lst
   deep[0][0] = 8     # Does not affect original lst
   ```

3. **Q: What are Python generators, and what are their advantages over iterators?**  
   **A:** Generators are a type of iterable that yield values one at a time, defined using `yield` in a function. They are memory-efficient because they generate values on-the-fly rather than storing them all in memory, unlike iterators which may hold entire collections. Example:  
   ```python
   def fib(n):
       a, b = 0, 1
       for _ in range(n):
           yield a
           a, b = b, a + b
   ```

4. **Q: How does Python handle memory management?**  
   **A:** Python uses a private heap space managed by the Python memory manager. Objects and data structures are stored in this heap, and the programmer has no direct access. Python employs reference counting and a cyclic garbage collector to reclaim memory from objects no longer referenced.[](https://www.edureka.co/blog/interview-questions/python-interview-questions)

5. **Q: What is a lambda function in Python? Provide an example.**  
   **A:** A lambda function is an anonymous function defined using the `lambda` keyword. It’s used for short, simple operations. Example:  
   ```python
   add = lambda x, y: x + y
   print(add(2, 3))  # Output: 5
   ```

6. **Q: Explain the use of `*args` and `**kwargs` in Python.**  
   **A:** `*args` allows a function to accept a variable number of positional arguments, stored as a tuple. `**kwargs` allows a variable number of keyword arguments, stored as a dictionary. Example:  
   ```python
   def func(*args, **kwargs):
       print(args)  # Tuple of positional args
       print(kwargs)  # Dictionary of keyword args
   func(1, 2, a=3, b=4)  # Output: (1, 2), {'a': 3, 'b': 4}
   ```

7. **Q: What is the `Global Interpreter Lock` (GIL) in Python?**  
   **A:** The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously in CPython. It simplifies memory management but limits true multithreading performance for CPU-bound tasks.

8. **Q: How do you achieve abstraction in Python?**  
   **A:** Abstraction in Python is achieved using abstract base classes (ABCs) from the `abc` module. You define abstract methods that must be implemented by subclasses. Example:  
   ```python
   from abc import ABC, abstractmethod
   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass
   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius
       def area(self):
           return 3.14 * self.radius ** 2
   ```

9. **Q: What are decorators in Python? Provide an example.**  
   **A:** Decorators are functions that modify the behavior of another function or method. They are often used for logging, access control, or memoization. Example:  
   ```python
   def log(func):
       def wrapper(*args, **kwargs):
           print(f"Calling {func.__name__}")
           return func(*args, **kwargs)
       return wrapper
   @log
   def add(x, y):
       return x + y
   add(2, 3)  # Output: Calling add, 5
   ```

10. **Q: What is the difference between a list comprehension and a generator expression?**  
    **A:** A list comprehension creates a list in memory, while a generator expression creates a generator object that yields items lazily, saving memory. Example:  
    ```python
    lst = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
    gen = (x**2 for x in range(5))  # <generator object>
    ```

## Data Structures and Algorithms
11. **Q: Write a program to check if a string is a palindrome.**  
    **A:**  
    ```python
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]
    print(is_palindrome("A man a plan a canal Panama"))  # True
    ```

12. **Q: Implement a function to find the kth largest element in an array.**  
    **A:**  
    ```python
    def find_kth_largest(nums, k):
        return sorted(nums, reverse=True)[k-1]
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
    ```

13. **Q: Write a function to reverse a linked list.**  
    **A:**  
    ```python
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def reverse_list(head):
        prev, curr = None, head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    ```

14. **Q: Detect a loop in a singly linked list.**  
    **A:** Using Floyd’s Cycle-Finding Algorithm:  
    ```python
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    ```

15. **Q: Write a function to find the longest palindromic substring.**  
    **A:**  
    ```python
    def longest_palindrome(s):
        n = len(s)
        start = 0
        max_len = 1
        for i in range(n):
            for j in range(i, n):
                substr = s[i:j+1]
                if substr == substr[::-1] and len(substr) > max_len:
                    start = i
                    max_len = len(substr)
        return s[start:start + max_len]
    print(longest_palindrome("babad"))  # "bab" or "aba"
    ```

16. **Q: Implement a binary search algorithm.**  
    **A:**  
    ```python
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    print(binary_search([1, 2, 3, 4, 5], 3))  # 2
    ```

17. **Q: Find the maximum difference between two indices j and i such that arr[j] > arr[i].**  
    **A:**  
    ```python
    def max_index_diff(arr):
        n = len(arr)
        max_diff = -1
        for i in range(n):
            j = n - 1
            while j > i:
                if arr[j] > arr[i] and max_diff < (j - i):
                    max_diff = j - i
                j -= 1
        return max_diff
    print(max_index_diff([20, 70, 40, 50, 12, 38, 98]))  # 6
    ```[](https://www.datacamp.com/blog/top-python-interview-questions-and-answers)

18. **Q: Merge two sorted lists into one sorted list.**  
    **A:**  
    ```python
    def merge_sorted_lists(list1, list2):
        result = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    ```

19. **Q: Implement a function to check if a binary tree is a BST.**  
    **A:**  
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)
    ```

20. **Q: Find the first non-repeating character in a string.**  
    **A:**  
    ```python
    def first_non_repeating(s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in s:
            if char_count[char] == 1:
                return char
        return None
    print(first_non_repeating("swiss"))  # 'w'
    ```

## System Design and Frameworks
21. **Q: How would you design a URL shortening service like TinyURL?**  
    **A:** Key components include a web server, database, and hash generator. Use a base62 encoding for short keys, store mappings in a NoSQL database (e.g., DynamoDB), and handle redirects via a REST API. Scale with load balancers and caching (e.g., Redis). Ensure uniqueness and handle collisions using a counter or UUID.

22. **Q: Explain Django’s MTV architecture.**  
    **A:** Django follows the Model-Template-View (MTV) pattern:  
    - **Model**: Represents data and database schema (ORM).  
    - **Template**: Handles presentation (HTML).  
    - **View**: Manages business logic and interacts between Model and Template.  
    URLs map requests to views, which query models and render templates.[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions/python-developer)

23. **Q: How do you optimize a Django application for performance?**  
    **A:** Use database indexing, caching (e.g., Redis or Memcached), query optimization (e.g., `select_related`, `prefetch_related`), pagination, and asynchronous tasks (e.g., Celery). Minimize database hits and use CDN for static files.

24. **Q: What are the benefits of using Flask over Django?**  
    **A:** Flask is lightweight, offering more flexibility for small or microservices-based applications. It has minimal setup and no rigid structure, unlike Django’s monolithic MTV framework. Flask is ideal for simple APIs, while Django suits complex, database-driven apps.[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions/python-developer)

25. **Q: Design a REST API for a user management system.**  
    **A:** Define endpoints like:  
    - `POST /users`: Create a user (input: name, email, password).  
    - `GET /users/{id}`: Retrieve user details.  
    - `PUT /users/{id}`: Update user.  
    - `DELETE /users/{id}`: Delete user.  
    Use JSON, HTTP status codes (e.g., 200, 404), and secure with JWT or OAuth.

26. **Q: How do you implement caching in a Python web application?**  
    **A:** Use Redis or Memcached for caching. In Flask/Django, store frequently accessed data (e.g., query results) in cache with a TTL. Example in Flask:  
    ```python
    from flask import Flask
    import redis
    app = Flask(__name__)
    cache = redis.Redis(host='localhost', port=6379)
    @app.route('/data')
    def get_data():
        data = cache.get('key')
        if data:
            return data
        data = expensive_query()
        cache.setex('key', 3600, data)  # Cache for 1 hour
        return data
    ```

27. **Q: Explain the role of middleware in Django.**  
    **A:** Middleware is a series of hooks that process requests and responses globally in Django. Examples include authentication, session management, and CSRF protection. Custom middleware can log requests or modify responses. Example:  
    ```python
    class LogMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
        def __call__(self, request):
            print(f"Request: {request.path}")
            response = self.get_response(request)
            return response
    ```

28. **Q: How do you handle database migrations in Django?**  
    **A:** Django uses `makemigrations` to create migration files based on model changes and `migrate` to apply them to the database. Always back up the database, test migrations locally, and use `south` or `django-migration` for complex migrations.

29. **Q: How would you secure a Python web application?**  
    **A:** Use HTTPS, validate/sanitize inputs, implement CSRF protection, use secure authentication (e.g., JWT, OAuth), store passwords with bcrypt, and limit database queries to prevent SQL injection. Use tools like `bandit` for static code analysis.

30. **Q: Explain the Circuit Breaker pattern in system design.**  
    **A:** The Circuit Breaker pattern prevents cascading failures in distributed systems by stopping requests to a failing service after a threshold of failures. It has three states: Closed, Open, and Half-Open. Libraries like `pybreaker` can implement it in Python.[](https://www.geeksforgeeks.org/epam-systems-interview-experience-for-senior-software-engineer-4-yoe-july-2024/)

## Behavioral and Situational Questions
31. **Q: Why do you want to work at EPAM?**  
    **A:** I’m excited about EPAM’s focus on innovative, global-scale projects and its collaborative environment. I look forward to contributing my Python expertise to cutting-edge solutions and growing professionally through continuous learning opportunities.[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions/senior-soft-engineer)

32. **Q: Describe a challenging project you worked on and how you overcame obstacles.**  
    **A:** In a previous role, I optimized a data processing pipeline that was slow due to large datasets. I identified bottlenecks using profiling tools, implemented parallel processing with `multiprocessing`, and reduced runtime by 50%. Clear communication with stakeholders ensured alignment.[](https://joingenius.com/interview-questions/senior-python-developer/)

33. **Q: How do you handle disagreements with a team member?**  
    **A:** I listen actively to understand their perspective, present my view with data or examples, and seek a solution that aligns with project goals. For example, I once resolved a design dispute by proposing a prototype to test both approaches, leading to a consensus.

34. **Q: How do you ensure code quality in your projects?**  
    **A:** I follow PEP 8 standards, use linters (e.g., PyLint, Flake8), write unit tests with `unittest` or `pytest`, conduct code reviews, and use CI/CD pipelines to catch issues early.[](https://joingenius.com/interview-questions/senior-python-developer/)

35. **Q: What have you learned from a past failure?**  
    **A:** In a project, I underestimated testing needs, leading to a production bug. I learned the importance of thorough unit and integration testing and now prioritize test-driven development (TDD) to prevent recurrence.[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions/senior-qa-automation-engineer)

## Advanced Python and Tools
36. **Q: What is the `asyncio` module in Python, and how do you use it?**  
    **A:** `asyncio` enables asynchronous programming for concurrent execution. Use `async def` for coroutines and `await` for asynchronous calls. Example:  
    ```python
    import asyncio
    async def say_hello():
        await asyncio.sleep(1)
        print("Hello")
    asyncio.run(say_hello())
    ```

37. **Q: How does Python’s `multiprocessing` differ from `threading`?**  
    **A:** `multiprocessing` runs separate processes with their own memory, bypassing the GIL for CPU-bound tasks. `threading` shares memory but is limited by the GIL, making it suitable for I/O-bound tasks.

38. **Q: Explain the use of `functools.lru_cache`.**  
    **A:** `lru_cache` is a decorator for memoization, caching function results based on arguments to avoid redundant computations. Example:  
    ```python
    from functools import lru_cache
    @lru_cache(maxsize=128)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    ```

39. **Q: How do you profile a Python application?**  
    **A:** Use `cProfile` or `line_profiler` to identify performance bottlenecks. Example:  
    ```python
    import cProfile
    def slow_function():
        sum(i**2 for i in range(1000000))
    cProfile.run('slow_function()')
    ```

40. **Q: What is the purpose of `__init__.py` in a Python package?**  
    **A:** `__init__.py` marks a directory as a Python package, allowing module imports. It can also initialize package-level variables or execute setup code.

## Coding Challenges
41. **Q: Convert a dictionary to a GET query string optimized for big data.**  
    **A:**  
    ```python
    def dict_to_query(params):
        return '&'.join(f"{k}={v}" for k, v in sorted(params.items()))
    print(dict_to_query({'name': 'John', 'age': 30}))  # age=30&name=John
    ```[](https://www.glassdoor.com/Interview/EPAM-Systems-Python-Developer-Interview-Questions-EI_IE15544.0%2C12_KO13%2C29.htm)

42. **Q: Implement a function to group anagrams.**  
    **A:**  
    ```python
    def group_anagrams(strs):
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    ```

43. **Q: Write a function to find the median of two sorted arrays.**  
    **A:**  
    ```python
    def find_median_sorted_arrays(nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n//2 - 1] + merged[n//2]) / 2
        return merged[n//2]
    print(find_median_sorted_arrays([1, 3], [2]))  # 2.0
    ```

44. **Q: Implement a function to check if a number is prime.**  
    **A:**  
    ```python
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    print(is_prime(17))  # True
    ```

45. **Q: Write a function to implement LRU Cache.**  
    **A:**  
    ```python
    from collections import OrderedDict
    class LRUCache:
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
        def get(self, key):
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]
        def put(self, key, value):
            if key in self.cache:
                self.cache.move_to_end(key)
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)
    ```

## Database and SQL
46. **Q: Write a SQL query to find the customer with the highest total order value for each year and month.**  
    **A:**  
    ```sql
    SELECT 
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        customer_id,
        SUM(order_value) AS total_value
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date), customer_id
    HAVING SUM(order_value) = (
        SELECT MAX(total)
        FROM (
            SELECT 
                YEAR(order_date) AS yr,
                MONTH(order_date) AS mth,
                SUM(order_value) AS total
            FROM orders
            GROUP BY YEAR(order_date), MONTH(order_date), customer_id
        ) sub
        WHERE yr = YEAR(order_date) AND mth = MONTH(order_date)
    );
    ```[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions)

47. **Q: How do you optimize SQL queries in Python applications?**  
    **A:** Use indexes on frequently queried columns, avoid `SELECT *`, use joins efficiently, and leverage query caching. In Python, use an ORM like Django’s to optimize queries with `select_related` or `prefetch_related`.

48. **Q: Explain database indexing and its impact on performance.**  
    **A:** Indexing creates a data structure (e.g., B-tree) to speed up data retrieval. It improves read performance but slows writes due to index updates. Choose indexes based on query patterns.

## DevOps and Cloud
49. **Q: How do you implement a CI/CD pipeline for a Python application?**  
    **A:** Use tools like Jenkins, GitHub Actions, or GitLab CI. Steps:  
    - **Build**: Install dependencies (`pip install -r requirements.txt`).  
    - **Test**: Run unit tests (`pytest`).  
    - **Deploy**: Push to a cloud service (e.g., AWS ECS) using Docker.  
    Example GitHub Actions workflow:  
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
          - name: Run tests
            run: pytest
    ```

50. **Q: What experience do you have with cloud platforms like AWS?**  
    **A:** I’ve used AWS services like EC2, S3, Lambda, and RDS for deploying Python applications. For example, I deployed a Django app on EC2 with auto-scaling and used S3 for static file storage, optimizing costs and performance.[](https://www.ambitionbox.com/interviews/epam-systems-interview-questions/python-developer)
