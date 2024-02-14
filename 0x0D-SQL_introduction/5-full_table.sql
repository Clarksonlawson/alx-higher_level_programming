-- Script to print the full description of the table first_table

-- Select the table schema from information_schema.tables
SELECT 
    CONCAT('Table\tCreate Table') AS 'Table Create Table'
FROM 
    information_schema.tables
WHERE 
    table_schema = 'hbtn_0c_0' AND
    table_name = 'first_table';
