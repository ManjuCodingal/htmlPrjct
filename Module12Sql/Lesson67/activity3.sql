CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Grade VARCHAR(10),
    City VARCHAR(50)
);

INSERT INTO Students VALUES (1, 'Aman', 18, 'A', 'Delhi');
INSERT INTO Students VALUES (2, 'Priya', 17, 'B', 'Mumbai');
INSERT INTO Students VALUES (3, 'Rohit', 18, 'A', 'Delhi');
INSERT INTO Students VALUES (4, 'Neha', 16, 'C', 'Chandigarh');
INSERT INTO Students VALUES (5, 'Karan', 17, 'B', 'Delhi');


SELECT * FROM Students;



SELECT * FROM Students
WHERE City = 'Delhi';


SELECT Name, Grade FROM Students
WHERE Grade = 'A';

SELECT * FROM Students
WHERE Age > 17;