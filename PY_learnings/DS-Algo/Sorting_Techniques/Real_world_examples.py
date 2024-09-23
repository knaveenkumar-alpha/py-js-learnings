"""
Sorting algorithms have various applications in real-world systems across different domains. Below are several examples 
where specific sorting algorithms are used:

1: E-commerce Websites
---------------------
Sorting products by price, rating, or popularity: When users search for products, the results are often sorted by price, 
popularity, rating, etc. Algorithms like Quick Sort or Merge Sort are used to ensure efficient sorting when dealing with 
large datasets.
Example: On Amazon, users may want to see the cheapest items first or the highest-rated items at the top. Sorting helps 
prioritize what is shown.

2. Databases
------------
Efficient querying: Sorting algorithms are essential in database systems for ordering records by date, name, or other 
attributes. Merge Sort is commonly used in databases because it is stable and can handle large datasets through external 
sorting techniques.
Example: SQL databases like MySQL and PostgreSQL use sorting algorithms for ORDER BY clauses when executing queries.

3. Search Engine
----------------
Sorting search results by relevance: After fetching search results based on a query, search engines sort them by relevance, 
using complex ranking algorithms. Once relevance scores are computed, sorting algorithms like Heap Sort or Quick Sort are 
used to sort the results quickly.
Example: Google search results are sorted by a combination of factors, including relevance and user-specific criteria.

4. File Systems
---------------
Sorting files by name, size, or modification date: File systems often need to display files in a specific order. Merge Sort 
or Quick Sort might be used depending on the size of the directory and how data is structured.
Example: In Windows or macOS, when you list files in a directory and sort them by date or file size, a sorting algorithm is 
applied.

5. Graphics Rendering
---------------------
Z-buffering: In 3D rendering, sorting is used to determine which object is in front and should be rendered first. Sorting 
algorithms are used to sort the objects by their depth (Z-order).
Example: In video games or graphical applications, rendering objects closest to the camera first ensures that the proper 
layers are visible.

6. Network Traffic Analysis
---------------------------
Sorting packets by arrival time: In networking, packets may arrive out of order, and sorting algorithms are used to arrange 
them in the correct sequence for processing. Insertion Sort might be useful for small sets of packets, while Merge Sort or 
Quick Sort might be employed for larger volumes of network traffic.
Example: In TCP/IP protocols, packets need to be sorted and reassembled in the correct order for accurate transmission.

7. Event Scheduling
-------------------
Task scheduling in operating systems: Operating systems schedule tasks based on priority. Sorting algorithms are used to 
arrange processes by priority, execution time, or deadline.
Example: Linux uses a priority-based scheduling system that might rely on sorting algorithms like Heap Sort to manage tasks 
in a priority queue.

8. Data Analytics
-----------------
Sorting data for better visualization: In data science, sorting is essential when visualizing data trends. Algorithms like 
Timsort are commonly used in libraries like Python's pandas to sort large datasets efficiently.
Example: When generating a bar chart of sales data, sorting the data by date or sales amount helps in understanding trends 
more clearly.

9. Digital Libraries
--------------------
Sorting books by title or author: In digital libraries or online book catalogs, users often want to sort books by title, 
author, publication date, etc. Sorting algorithms help manage this.
Example: Google Books or Kindle libraries allow users to sort by publication year or author’s name, typically using 
algorithms like Merge Sort for large-scale data.

10. Operating Systems
---------------------
Memory management and garbage collection: In memory management, operating systems sometimes use sorting to manage free and 
allocated memory blocks, allowing efficient use of memory resources.
Example: In garbage collection, the Mark-Sweep algorithm sorts objects to determine which ones should be cleaned up.

11. Financial Systems
---------------------
Sorting stock market data: Financial applications like trading platforms need to sort stocks by price, volume, or date. 
This often requires real-time sorting algorithms with O(n log n) complexity.
Example: Stock trading platforms like Robinhood or Bloomberg sort financial data in real time based on user preferences.

12. Music or Video Streaming Services
-------------------------------------
Sorting playlists by duration, artist, or popularity: Streaming platforms like Spotify, YouTube, and Netflix use sorting 
to arrange media based on user preferences.
Example: In a Spotify playlist, users might sort songs by artist or play count, typically using algorithms like Merge Sort 
or Quick Sort to handle large libraries.

13. Artificial Intelligence (AI)
--------------------------------
Sorting training data in machine learning: In AI and machine learning, sorting is often used to preprocess data before 
training models. Algorithms like Quick Sort are employed to arrange data points for analysis.
Example: When training a classification model, the dataset might be sorted based on specific features for more efficient 
processing.

14. Healthcare
--------------
Patient data sorting: In hospital management systems, patient data is often sorted by age, admission date, or medical 
condition. Sorting ensures that critical patients are treated first.
Example: An electronic health record (EHR) system may sort patient records by urgency or appointment time.

15. Map and GPS Systems
-----------------------
Sorting locations by proximity: In GPS applications, sorting is used to display nearby locations or routes by proximity 
to a user’s current location.
Example: Google Maps sorts nearby restaurants or gas stations by distance from the user.


Summary Table of Algorithms and Real-World Examples:
Algorithm	     Real-World Example
------------------------------------------------------------------------------
Bubble Sort      Sorting small datasets in learning environments
Selection Sort	 Used in scenarios with low memory constraints
Insertion Sort	 Ideal for nearly sorted datasets like task lists
Merge Sort	     Sorting large datasets in databases, file systems
Quick Sort	     Search engines, e-commerce product sorting
Heap Sort	     Task scheduling in operating systems
Timsort	         Python's sorted() function, efficient for real-world data
Radix Sort	     Sorting large integers or string data in financial systems

These are some real-world examples where sorting algorithms are employed to solve practical problems in technology and business.
Each sorting algorithm has its strengths and weaknesses, and choosing the right one depends on the nature of the dataset and the
system requirements.

"""