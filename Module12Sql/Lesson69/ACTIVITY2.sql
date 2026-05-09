DROP TABLE IF EXISTS employees;
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT
);
INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Amit', 'IT', 90000),
(2, 'Neha', 'HR', 50000),
(3, 'Rahul', 'IT', 120000),
(4, 'Sneha', 'Finance', 70000),
(5, 'Arjun', 'HR', 45000),
(6, 'Priya', 'Finance', 80000),
(7, 'Vikas', 'IT', 110000),
(8, 'Anjali', 'Marketing', 60000),
(9, 'Rohit', 'Marketing', 65000),
(10, 'Kiran', 'HR', 55000);

SELECT SUM(salary) 
AS total_salary
FROM employees;

SELECT AVG(salary) 
AS average_salary
FROM employees;


SELECT COUNT(DISTINCT department)
 AS department_count
FROM employees;

SELECT MAX(salary) 
FROM employees;

SELECT MIN(salary) 
FROM employees;