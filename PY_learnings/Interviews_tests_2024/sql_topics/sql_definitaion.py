"""
1. What is SQL?
A: SQL (Structured Query Language) is a standard programming language used to manage and manipulate 
relational databases. It allows users to create, read, update, and delete (CRUD) data in databases.

2. What are the different types of SQL statements?
A: SQL statements can be categorized into the following types:

DDL (Data Definition Language): Used to define and modify database structures. Examples: CREATE, ALTER, 
                                DROP.
DML (Data Manipulation Language): Used to manipulate data in the database. Examples: SELECT, INSERT, 
                                    UPDATE, DELETE.
DCL (Data Control Language): Used to control access to the database. Examples: GRANT, REVOKE.
TCL (Transaction Control Language): Used to manage transactions in the database. Examples: COMMIT, 
                                    ROLLBACK, SAVEPOINT.

3. What is a Primary Key?
A: A primary key is a column (or a set of columns) in a database table that uniquely identifies each 
record in that table. It ensures that no two rows have the same value and prevents NULL values.

Example:

sql
Copy code
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(100)
);

4. What is a Foreign Key?
A: A foreign key is a column (or a set of columns) in a table that creates a link between two tables. 
It references the primary key in another table, ensuring referential integrity between the tables.

Example:

sql
Copy code
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(ID)
);

5. What is an Index in SQL?
A: An index in SQL is a database object that improves the speed of data retrieval operations on a table 
at the cost of slower insert, update, and delete operations. Indexes are used to quickly locate rows based 
on the values of one or more columns.

Example:

sql
Copy code
CREATE INDEX idx_employee_name ON Employees(Name);

6. What is a JOIN? Explain its types.
A: A JOIN is used in SQL to combine rows from two or more tables based on a related column between them. 
Types of joins include:

INNER JOIN: Returns records that have matching values in both tables.
LEFT JOIN (or LEFT OUTER JOIN): Returns all records from the left table, and the matched records from the 
right table. If no match, NULL is returned from the right side.
RIGHT JOIN (or RIGHT OUTER JOIN): Returns all records from the right table, and the matched records from 
the left table. If no match, NULL is returned from the left side.
FULL OUTER JOIN: Returns all records when there is a match in either left or right table. If there is no 
match, NULL values are returned for non-matching rows.
Example:

sql
Copy code
SELECT Employees.Name, Orders.OrderID 
FROM Employees
INNER JOIN Orders ON Employees.ID = Orders.EmployeeID;

7. What is the difference between WHERE and HAVING clauses in SQL?
A:
WHERE: Used to filter rows before grouping operations are performed. It applies to individual rows.
HAVING: Used to filter groups after the GROUP BY operation has been applied. It applies to the result 
of the aggregation.
Example:

sql
Copy code
SELECT Department, COUNT(*)
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;

8. What is a Subquery in SQL?
A: A subquery is a query within another query. It is used to fetch data that will be used in the main 
query. Subqueries can return individual values or a result set.

Example:

sql
Copy code
SELECT Name 
FROM Employees
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'HR');


9. What is SQL Injection?
A: SQL Injection is a code injection technique where an attacker exploits a vulnerability in the 
application by inserting or injecting malicious SQL queries into input fields, which can compromise 
the database’s security.

Example of a vulnerable query:

sql
Copy code
SELECT * FROM Users WHERE Username = 'admin' AND Password = ' ' OR '1' = '1';

10. What is the difference between DELETE, TRUNCATE, and DROP?
A: DELETE: Deletes rows from a table based on a condition. It can be rolled back.
sql
Copy code
DELETE FROM Employees WHERE ID = 1;
TRUNCATE: Deletes all rows from a table without logging individual row deletions. Cannot be rolled back.
sql
Copy code
TRUNCATE TABLE Employees;
DROP: Completely removes a table (or other database objects) from the database.
sql
Copy code
DROP TABLE Employees;

11. What are Aggregate Functions in SQL?
A: Aggregate functions perform calculations on a set of values and return a single value. Common aggregate
functions include:

COUNT(): Returns the number of rows.
SUM(): Returns the sum of values.
AVG(): Returns the average of values.
MAX(): Returns the maximum value.
MIN(): Returns the minimum value.
Example:

sql
Copy code
SELECT COUNT(*), AVG(Salary), MAX(Salary), MIN(Salary)
FROM Employees;

12. What are Views in SQL?
A: A view is a virtual table based on the result of a SQL query. It doesn’t store data physically, 
but it provides a way to present and query data from one or more tables.

Example:

sql
Copy code
CREATE VIEW EmployeeSalaryView AS
SELECT Name, Salary
FROM Employees
WHERE Salary > 50000;

13. What is Normalization? Explain its Types.
A: Normalization is the process of organizing data in a database to minimize redundancy and ensure data integrity. 
The main types are:

1NF (First Normal Form): Each column contains atomic (indivisible) values, and each entry is unique.
2NF (Second Normal Form): In 1NF, and all non-key attributes are fully functionally dependent on the 
primary key.
3NF (Third Normal Form): In 2NF, and no transitive dependencies exist (non-key attributes are dependent 
only on the primary key).

14. What are Transactions in SQL?
A: A transaction in SQL is a sequence of one or more SQL operations that are executed as a single unit. 
Transactions ensure ACID properties (Atomicity, Consistency, Isolation, Durability). Key SQL transaction 
commands are:

BEGIN TRANSACTION: Starts a transaction.
COMMIT: Saves the transaction.
ROLLBACK: Reverts changes in case of an error.

15. What are Stored Procedures in SQL?
A: A stored procedure is a set of SQL statements that can be executed as a program. Stored procedures 
allow for reusable logic, can accept input parameters, and return values.

Example:

sql
Copy code
CREATE PROCEDURE GetEmployee (@ID INT)
AS
BEGIN
    SELECT * FROM Employees WHERE ID = @ID;
END;




"""


