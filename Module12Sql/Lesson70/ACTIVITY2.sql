-- In this activity, students have to create a” DEPARTMENT” TABLE and have to perform these actions : 1)Write a query that displays the number of employees working in each department. 2)Write a query that displays the total salary paid to employees working in each department. 3)Write a query that displays the number of employees, total salary paid to employees working in each department. 4)Write a query that displays the department code, total salary paid to employees group by department_id and manager_id=103. 5)Write a query that displays the department id, number of employees of those groups that have more than 2 employees
-- Create the DEPARTMENT table if it does not exist
DROP TABLE IF EXISTS DEPARTMENT;
CREATE TABLE IF NOT EXISTS DEPARTMENT(
    EMPLOYEE_ID TEXT,
    NAME TEXT,
    DEPARTMENT_ID TEXT, 
    MANAGER_ID TEXT,
    SALARY REAL
);
 

-- Insert sample data into the DEPARTMENT table
INSERT INTO DEPARTMENT(EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY) VALUES
('100', 'STEVEN KING', '90', '100', 24000),
('101', 'NEENA KOCHCAR', '90', '100', 17000),
('102', 'LEX DEHAAN', '90', '102', 9000), 
('103', 'BRUCE LEE', '60', '103', 4800), 
('104', 'DIANA WILLS', '60', '103', 25000), 
('105', 'VALLI PATOR', '50', '100', 4200), 
('1973', 'LUV HAMI', '60', '102', 5000), 
('106', 'DAVID AUSTIN', '90', '100', 6000);

-- Query to count the number of employees in each department
SELECT DEPARTMENT_ID AS "DepartmentCode",
COUNT(*) AS "Num of Employees"
FROM DEPARTMENT
GROUP BY DEPARTMENT_ID;

-- Query to sum the salary of each department
SELECT DEPARTMENT_ID AS "DepartmentCode",
SUM(SALARY) AS "Total Salary"
FROM DEPARTMENT
GROUP BY DEPARTMENT_ID;

-- Query to count the number of employees and sum the salary in each department
SELECT DEPARTMENT_ID AS "DepartmentCode",
COUNT(*) AS " Num of Employees", 
SUM(SALARY) AS "Total Salary"
FROM DEPARTMENT
GROUP BY DEPARTMENT_ID;



-- Query to sum the salary of employees with a specific manager
SELECT DEPARTMENT_ID AS "DepartmentCode",
SUM(SALARY) AS "Total salary"
FROM DEPARTMENT
WHERE MANAGER_ID='103'
GROUP BY DEPARTMENT_ID;

-- Query to find departments with more than 2 employees
SELECT DEPARTMENT_ID AS "DepartmentCode",
COUNT(*) AS "Num of Employees"
FROM DEPARTMENT
-- WHERE COUNT(*)>2
GROUP BY DEPARTMENT_ID 
 HAVING COUNT(*)>2; --having filters group,it written after group by

