DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    grade INT
);

INSERT INTO customers (customer_id, name, city, grade) VALUES
(1, 'Ramesh', 'New York', 120),
(2, 'Suresh', 'Chicago', 90),
(3, 'Anita', 'New York', 80),
(4, 'John', 'Boston', 110),
(5, 'Meena', 'New York', 150),
(6, 'David', 'Chicago', 130);

SELECT * FROM customers
WHERE city = 'New York' OR grade > 100;

SELECT * FROM customers
WHERE city = 'New York' AND grade > 100;