-- Create table
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