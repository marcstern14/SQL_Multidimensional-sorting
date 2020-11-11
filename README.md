# SQL_Multidimensional-sorting
This is a series of scripts I wrote in Python that implements SQL for multidimensional parsing of a database.
This was done as part of an Advanced Python course at NYU (completed summer 2020).

Assignment descriptions below:

2.1 SQL to CSV: write function sql_to_csv(db_filename, table, csv_filename) that reads from a table in an sqlite database, and writes to a CSV file. 

2.2 CREATE TABLE / DROP TABLE: write a script that creates a new table called weather_newyork in the session_2.db database with the following columns: date (should be a TEXT column), mean_temp (INT), precip (FLOAT), events (TEXT). 

2.3 CSV to SQL: Starting with the DROP TABLE and CREATE TABLE code from the previous solution, write a script that reads from weather_newyork.csv, selects the date, mean_temp, precip and events columns, and inserts them row-by-row into the table you created, weather_newyork. 

2.4 JSON to SQL: Starting with the DROP TABLE and CREATE TABLE code from the previous solution, write a script that reads from weather_newyork_dod.json, selects the date, mean_temp, precip and events values from each dict, and inserts them row-by-row into the table you created, weather_newyork (make sure values are in correct order). 
