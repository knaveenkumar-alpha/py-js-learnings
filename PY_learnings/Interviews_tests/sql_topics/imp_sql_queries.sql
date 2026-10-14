-- 1. First Highest Salary

SELECT id, name, MAX(salary) AS highest_salary
FROM emp;

-- 2. Second Highest Salary

SELECT id, name, salary 
FROM emp 
WHERE salary = (SELECT MAX(salary) 
                FROM emp 
                WHERE salary < (SELECT MAX(salary) FROM emp));

-- 3. Nth Highest Salary

SELECT id, name, salary 
FROM emp e1 
WHERE N-1 = (SELECT COUNT(DISTINCT salary) 
             FROM emp e2 
             WHERE e2.salary > e1.salary);

-- 4. Example: 4th Highest Salary

SELECT id, name, salary 
FROM emp e1 
WHERE 3 = (SELECT COUNT(DISTINCT salary) 
           FROM emp e2 
           WHERE e2.salary > e1.salary);

-- 5. Find Duplicate Records in a Table

SELECT * 
FROM emp out 
WHERE (SELECT COUNT(*) 
       FROM emp inr 
       WHERE inr.emp_id = out.emp_id) > 1;

-- 6. Employees Whose Salary is Greater Than Their Manager’s

SELECT e.id, e.name, e.salary 
FROM emp e 
JOIN emp m 
ON e.manager_id = m.emp_id 
WHERE e.salary > m.salary;

-- 7. List Workers in a Department in Decreasing Order

SELECT department, COUNT(worker_id) AS no_of_workers 
FROM workers 
GROUP BY department 
ORDER BY no_of_workers DESC;
Union vs. Union All
UNION: Removes duplicates from the result set.
UNION ALL: Keeps all duplicates in the result set.

Hotel Table Creation and Data Manipulation Example
sql
Copy code
DROP TABLE IF EXISTS hotel;

CREATE TABLE hotel(
    ssn INT NOT NULL,
    cname TEXT NOT NULL,
    address TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    room_type CHAR(9)
);

INSERT INTO hotel VALUES (12, 'Naveen', 'Kurnool', '2019-02-01', '2019-03-01', 'A/c');
INSERT INTO hotel VALUES (13, 'Sai', 'Kurnool', '2019-02-01', '2019-12-31', 'Normal');
INSERT INTO hotel VALUES (14, 'Ram', 'Tirupati', '2019-02-01', '2020-03-01', 'A/c');
INSERT INTO hotel VALUES (12, 'Sam', 'Hyderabad', '2019-04-01', NULL, NULL);
INSERT INTO hotel VALUES (12, 'John', 'Bangalore', '2019-05-01', NULL, NULL);

-- Query the hotel table
SELECT * FROM hotel;

-- Count the duration of each stay
SELECT COUNT(end_date - start_date) 
FROM hotel;

-- Update end_date where it is NULL
UPDATE hotel 
SET end_date = '2020-05-13' 
WHERE end_date IS NULL;

-- Calculate total stay duration in years, months, and days
SELECT 
    SUM(EXTRACT(YEAR FROM age(end_date, start_date))) AS years,
    SUM(EXTRACT(MONTH FROM age(end_date, start_date))) AS months,
    SUM(EXTRACT(DAY FROM age(end_date, start_date))) AS days 
FROM hotel;

-- Calculate the total amount based on stay duration
SELECT 
    SUM(EXTRACT(YEAR FROM age(end_date, start_date))) * 1200000 AS amount_years,
    SUM(EXTRACT(MONTH FROM age(end_date, start_date))) * 100000 AS amount_months,
    SUM(EXTRACT(DAY FROM age(end_date, start_date))) * 3300 AS amount_days 
FROM hotel;

-- Calculate total amount for all stays
SELECT 
    (SUM(EXTRACT(YEAR FROM age(end_date, start_date))) * 1200000 +
    SUM(EXTRACT(MONTH FROM age(end_date, start_date))) * 100000 +
    SUM(EXTRACT(DAY FROM age(end_date, start_date))) * 3300) AS total_amount 
FROM hotel;
Schema and Table Creation Example
sql
Copy code
CREATE SCHEMA postgres_prac;
SET search_path TO postgres_prac;

CREATE TABLE dept (
    deptno INT NOT NULL CONSTRAINT dept_pk PRIMARY KEY,
    dname VARCHAR(14) CONSTRAINT dept_dname_uq UNIQUE,
    loc VARCHAR(13)
);

CREATE TABLE emp (
    empno INT NOT NULL CONSTRAINT emp_pk PRIMARY KEY,
    ename VARCHAR(10),
    job VARCHAR(9),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(7,2) CONSTRAINT emp_sal_ck CHECK (sal > 0),
    comm DECIMAL(7,2),
    deptno INT CONSTRAINT emp_ref_dept_fk REFERENCES dept(deptno)
);

-- Insert data into dept table
INSERT INTO dept VALUES (10, 'ACCOUNTING', 'NEW YORK');
INSERT INTO dept VALUES (20, 'RESEARCH', 'DALLAS');
INSERT INTO dept VALUES (30, 'SALES', 'CHICAGO');
INSERT INTO dept VALUES (40, 'OPERATIONS', 'BOSTON');

-- Insert data into emp table
INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20);
INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30);
-- (additional INSERT statements...)

-- Additional Employee Queries
-- Total Salary of All Employees

SELECT SUM(sal) AS total_salary 
FROM emp;

-- Employee with the Maximum Salary

SELECT empno, ename, MAX(sal) AS max_salary 
FROM emp 
GROUP BY empno, ename;

-- Employee with Salary Greater Than Their Manager

SELECT e.empno, e.ename, e.sal, m.empno AS mgr, m.ename AS mgr_name, m.sal AS mgr_sal 
FROM emp e 
JOIN emp m 
ON e.mgr = m.empno 
WHERE e.sal > m.sal;

-- Employees Count by Department (Descending Order)

SELECT e.deptno, COUNT(e.empno) AS no_of_employee 
FROM emp e 
GROUP BY e.deptno 
ORDER BY no_of_employee DESC;

-- Player Table Example

CREATE TABLE player (
    id INT,
    first VARCHAR(25),
    year INT
);

INSERT INTO player (id, first, year) VALUES (1, 'Santo', 1977);
INSERT INTO player (id, first, year) VALUES (2, 'Santo', 1978);
-- (additional INSERT statements...)
-- Player Query: Find Players with Consecutive Years

SELECT DISTINCT(first) 
FROM player 
WHERE first IN (SELECT p1.first 
                FROM player p1 
                JOIN player p2 ON p1.year = p2.year + 1 
                JOIN player p3 ON p2.year = p3.year + 1 
                WHERE p1.first = p2.first AND p2.first = p3.first);
