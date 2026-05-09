-- Create a table "noble_win" and write a query to find all the details of the Nobel winners for the subject not started with the letter 'P' and arrange the list as the most recent comes first, then by name in order.
-- Create the NOBEL_WIN table if it does not exist
DROP TABLE IF EXISTS noble_win;
CREATE TABLE IF NOT EXISTS noble_win(
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
);
 

-- Insert sample data into the NOBEL_WIN table
INSERT INTO noble_win(YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES
(1970, 'PHYSICS', 'HANNES ALFVEN', 'SWEDEN', 'SCIENTIST'),
(1970, 'PHYSICS', 'LOUIS NEEL', 'FRANCE', 'SCIENTIST'),
(1971, 'PHYSICS', 'PAUL', 'FRANCE', 'SCIENTIST'),
(1971, 'CHEMISTRY', 'HAMILTON', 'SWEDEN', 'LINGUIST'),
(1972, 'LITERATURE', 'BERNARD KELSON', 'GERMANY', 'ECONOMIST'),
(1972, 'ECONOMICS', 'JOSEPH', 'RUSSIA', 'ECONOMIST'),
(1973, 'BIOLOGY', 'PHILIPS', 'USA', 'PRIME MINISTER'),
(1980, 'BIOLOGY', 'MARTIN', 'USA','PRESIDENT'),
(1981, 'PHYSIOLOGY', 'HANNAH', 'HUNGARY', 'SCIENTIST'),
(1975, 'PHYSICS', 'PETER', 'CHILE', 'SCIENTIST');

-- Select all records from the NOBEL_WIN table where the subject does not start with 'P'
SELECT* FROM noble_win
WHERE SUBJECT NOT LIKE 'P%';

SELECT* FROM noble_win
ORDER BY YEAR DESC;

SELECT* FROM noble_win
ORDER BY WINNER;

SELECT* FROM noble_win
WHERE SUBJECT NOT LIKE 'P%'
ORDER BY WINNER ASC, YEAR DESC;



