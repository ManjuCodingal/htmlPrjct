import sqlite3
import pandas as pd

# Connect to database (creates file if not exists)
database = 'database.sqlite'
conn = sqlite3.connect(database)

print("Opened database successfully")

# Create a table (so database is not empty)
conn.execute("""
CREATE TABLE IF NOT EXISTS supplier (
    SNO TEXT PRIMARY KEY,
    SNAME TEXT,
    STATUS INTEGER,
    CITY TEXT
);
""")

conn.commit()

# Read all tables from database
tables = pd.read_sql("""
SELECT * 
FROM sqlite_master
WHERE type='table';
""", conn)

print("\nTables in Database:")
print(tables)

conn.close()

# #### **1. Import Database**
# """

# # Import file from your system
# from google.colab import files
# file = files.upload()

# """#### **2. Connect with SQLite Database**"""

# # Connect with sqlite database
# # Import necessary libraries
# import sqlite3 # imports Python’s built-in SQLite module

# # Connect to Database
# database = 'database.sqlite' # This will create a new database file named 'database.sqlite' in the current directory if it doesn't exist, or connect to it if it does exist.

# conn = sqlite3.connect(database)
# print('Opened data successfully')

# # Read SQL query for getting all the tables of database into a dataframe
# # Here SELECT * means select all
# import pandas as pd
# tables = pd.read_sql("""SELECT * 
#                     FROM sqlite_master
#                     WHERE type='table';""", conn)
# # tables
# print(tables)
# # sqlite_master is a system table in SQLite.
# # It stores metadata about: tables, indexes, triggers, and views in the database.
# # It is automatically created by SQLite.