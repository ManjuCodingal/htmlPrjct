-- -Create a 'STUDENT" Table and use "AND"& "OR"Operators to filter the necessary data asked in the question like: 1)To fetch all the records from the Student table where Age is 18 and ADDRESS is Delhi 2)To fetch all the records from the Student table where NAME is Ram and Age is 18. 3)To fetch all the records from the Student table where NAME is Ram or NAME is SUJIT. 4)To fetch all the records from the Student table where NAME is Ram or Age is 20. 5)To fetch all the records from the Student table where Age is 18 NAME is Ram or RAMESH.
-- Create the STUDENT table if it does not exist
-- NOT NULL is used for NAME to ensure every student record has a name
DROP TABLE IF EXISTS STUDENT;
CREATE TABLE IF NOT EXISTS STUDENT (
    ROLL_NO TEXT PRIMARY KEY,
    NAME TEXT NOT NULL,
    ADDRESS TEXT,
    PHONE TEXT,
    AGE INTEGER
);

-- Insert sample data into the STUDENT table
INSERT INTO STUDENT (ROLL_NO, NAME, ADDRESS, PHONE, AGE) VALUES
('1', 'RAM', 'DELHI', '******', 18),
('2', 'RAMESH', 'GURGAON', '******', 18),
('3', 'SUJIT', 'ROHTAK', '******', 20),
('4', 'SURESH', 'DELHI', '******', 18),
('5', 'AMAN', 'ROHTAK', '******', 20),
('6', 'HARSH', 'GURGAON', '******', 18);

-- Select all records from the STUDENT table to verify insertion
SELECT * FROM STUDENT;

-- Query students who are 18 years old and live in Delhi
SELECT * FROM STUDENT 
WHERE AGE=18 AND ADDRESS='DELHI';

-- Query students who are 18 years old and named RAM
SELECT * FROM STUDENT
WHERE AGE=18 AND NAME='RAM';

-- Query students named Ram or Sujit
SELECT * FROM STUDENT
WHERE NAME= 'RAM' OR NAME='SUJIT';

-- Query students named Ram or aged 20
SELECT * FROM STUDENT
WHERE NAME= 'RAM' OR AGE=20;

-- Query students aged 18 and named Ram or Ramesh
SELECT * FROM STUDENT
WHERE AGE= 18 AND (NAME='RAM' OR NAME='RAMESH');




