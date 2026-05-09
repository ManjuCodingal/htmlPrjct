-- In this activity students will have to create a “PRODUCTS” TABLE and have to perform these actions: 1)Write a SQL query that finds the number of products. 2)Write a SQL query that finds the average price of all products. 3)Write a SQL query that finds the sum of the price of all products.
--Create the PRODUCTS table if it does not exist
DROP TABLE IF EXISTS PRODUCTS;
CREATE TABLE IF NOT EXISTS PRODUCTS(
    PRODUCT_ID TEXT,
    PRODUCT_NAME TEXT,
    SUPPLIER_ID TEXT,
    CATEGORY_ID TEXT,
    UNIT_TEXT,
    PRICE_REAL
);

-- Insert sample data into the PRODUCTS table
INSERT INTO PRODUCTS(PRODUCT_ID, PRODUCT_NAME,SUPPLIER_ID, CATEGORY_ID, UNIT_TEXT, PRICE_REAL) VALUES
('1', 'CHAIS', '1', '1', '10 BOXES*20 BAGS', 18),
('2', 'CHANG', '1', '1', '24-12 OZ BOTTLES', 19),
('3', 'ANISEED SYRUP', '1', '2', '12-550 ML BOTTLES', 10),
('4', 'CHEF ANTON SEASONING', '2', '2', '48-6 OZ JARS', 22),
('5', 'CHEF ANTON MIX', '2', '2', '36 BOXES', 21.35),
('6', 'CHIPS', '2', '3', '20 PACKETS', 20.5),
('7', 'CHIPS', '2', '3', '25 PACKETS', 10.5);

SELECT PRODUCT_NAME FROM PRODUCTS;

SELECT DISTINCT PRODUCT_NAME FROM PRODUCTS;
-- Query to count the number of products
SELECT COUNT(PRODUCT_ID)
AS Product_Count
FROM PRODUCTS;
-- Query to find the average price of products
SELECT AVG(PRICE_REAL)
AS Avg_Price
FROM PRODUCTS;
-- Query to find the total price of products
SELECT SUM(PRICE_REAL)
AS Total_Price
FROM PRODUCTS;
-- get highest and lowest price
SELECT MIN(PRICE_REAL)
FROM PRODUCTS;

SELECT MAX(PRICE_REAL)
FROM PRODUCTS;
--  find products above average price
SELECT* 
FROM PRODUCTS
WHERE PRICE_REAL> (
SELECT AVG(PRICE_REAL)FROM PRODUCTS
);



