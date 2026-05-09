-- Create a "Products" table and write two queries, one for finding the cheapest product and one to find the costliest product.
DROP TABLE IF EXISTS products;
CREATE TABLE IF NOT EXISTS products(
PRO_ID TEXT PRIMARY KEY,
PRO_NAME TEXT,
PRO_PRICE INTEGER,
PRO_COM TEXT
);


INSERT INTO products(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM)VALUES
 
    ("101","MOTHER BOARD",3200,"15"),
    ("102","KEY BOARD",450,"16"),
    ("103","ZIP DRIVE",250,"14"),
    ("104","SPEAKER",550,"16"),
    ("105","MONITOR",5000,"11"),
    ("106","DVD DRIVE",900,"12"),
    ("107","CD DRIVE",800,"12"),
    ("108","PRINTER",2600,"13"),
    ("109","REFILL CARTRIDGE",350,"13"),
    ("110","MOUSE",250,"12");

SELECT * FROM products;

SELECT PRO_NAME, PRO_PRICE
FROM products
WHERE PRO_PRICE=(SELECT MIN(PRO_PRICE) FROM products);

SELECT PRO_NAME, PRO_PRICE
FROM products
WHERE PRO_PRICE=(SELECT MAX(PRO_PRICE) FROM products);
 




