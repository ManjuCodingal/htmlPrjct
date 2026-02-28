-- Q. Is a .db file required to run .sql files?

-- OPTION 1: If You’re Using SQLite- Yes — you typically need a .db file.
--  SQLite stores the entire database in a single file (like mydatabase.db).
-- In VS Code (with a SQLite extension):You create or open a .db file.Then run your SQL queries against that file
-- The .db file is where all your tables, data, changes and schema are stored for SQLite. You can create it manually or let SQLite create it when you run your first query that creates a table.

-- OPTION 2: If You’re Using MySQL / PostgreSQL / SQL Server
-- No — you do NOT create a .db file manually.
-- These databases run as a server service, and you connect to them.
-- Examples: MySQL, PostgreSQL, Microsoft SQL Server
-- For these:
-- You install the database server--> Start the service --> Create a database using SQL (CREATE DATABASE mydb;) --> Then run .sql files against that database

-- Q. Use of DROP TABLE IF EXISTS <tableName> in SQL?
DROP TABLE IF EXISTS supplier;  -- To avoid error when we run the file the second time.
-- If line 1 not provided then on running file 2nd time this happens:
-- Table already exists (because of IF NOT EXISTS)
-- Your INSERT statement runs again
-- It tries to insert. But PRO_ID = 101 is already in the table. So SQL throws

CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Smith', 20, 'London'),
('S2', 'Jones', 10, 'Paris'),
('S3', 'Blake', 30, 'Paris'),
('S4', 'Clarke', 20, 'London'),
('S5', 'Adams', 30, 'Athens');

SELECT * FROM supplier;