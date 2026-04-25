[16:23, 19/04/2026] Einstein: -- Create table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);

-- Insert records
INSERT INTO students (id, name, age, grade) VALUES
(1, 'Alice', 14, '8th'),
(2, 'Bob', 15, '9th'),
(3, 'Charlie', 14, '8th'),
(4, 'David', 16, '10th');

-- Display all records
SELECT * FROM students;

-- Fetch students aged 14
SELECT * FROM students
WHERE age = 14;

-- Fetch students in 9th grade
SELECT * FROM students
WHERE grade = '9th';

-- Fetch student named Alice
SELECT * FROM students
WHERE name = 'Alice';
[16:27, 19/04/2026] Einstein: -- Create a table
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Marks INT,
    City VARCHAR(50)
);

-- Insert sample data
INSERT INTO Students (ID, Name, Age, Marks, City) VALUES
(1, 'Alice', 18, 85, 'Copenhagen'),
(2, 'Bob', 20, 70, 'Roskilde'),
(3, 'Charlie', 19, 90, 'Aarhus'),
(4, 'David', 21, 60, 'Odense'),
(5, 'Eva', 18, 95, 'Copenhagen');

-- 1. Arithmetic Operators (+, -, *, /)
SELECT Name, Marks, Marks + 5 AS BonusMarks
FROM Students;

-- 2. Comparison Operators (=, >, <, >=, <=, <>)
SELECT * FROM Students
WHERE Marks > 80;

-- 3. Logical Operators (AND, OR, NOT)
SELECT * FROM Students
WHERE Marks > 70 AND City = 'Copenhagen';

SELECT * FROM Students
WHERE Marks < 70 OR Age > 20;

SELECT * FROM Students
WHERE NOT City = 'Aarhus';

-- 4. BETWEEN Operator
SELECT * FROM Students
WHERE Marks BETWEEN 70 AND 90;

-- 5. IN Operator
SELECT * FROM Students
WHERE City IN ('Copenhagen', 'Odense');

-- 6. LIKE Operator (pattern matching)
SELECT * FROM Students
WHERE Name LIKE 'A%';   -- Names starting with A

-- 7. IS NULL Operator (example)
-- (First insert a NULL value)
INSERT INTO Students (ID, Name, Age, Marks, City)
VALUES (6, 'Frank', 22, NULL, 'Aalborg');

SELECT * FROM Students
WHERE Marks IS NULL;