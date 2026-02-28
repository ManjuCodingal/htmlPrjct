DROP TABLE IF EXISTS PRODUCT;  -- To avoid error when we run the file the second time.
-- If line 1 not provided then on running file 2nd time this happens:
-- Table already exists (because of IF NOT EXISTS)
-- Your INSERT statement runs again
-- It tries to insert. But PRO_ID = 101 is already in the table. So SQL throws
CREATE TABLE IF NOT EXISTS PRODUCT(
  PRO_ID TEXT PRIMARY KEY,
  PRO_NAME TEXT,
  PRO_PRICE INTEGER,
  PRO_COM TEXT
);
INSERT INTO PRODUCT(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM)
VALUES
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
-- SELECT * FROM PRODUCT;  -- This line shows the products table. This can be used to check if the data is inserted correctly.
SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MIN(pro_price) FROM PRODUCT); -- Displays only product(s) with minimum price.
SELECT pro_name, pro_price
   FROM PRODUCT
   WHERE pro_price = 
    (SELECT MAX(pro_price) FROM PRODUCT);    -- Displays only product(s) with maximum price.