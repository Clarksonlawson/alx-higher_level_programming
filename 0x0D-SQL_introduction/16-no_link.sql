-- Script to list all records of the table second_table of the database hbtn_0c_0

-- Don't list rows without a name value
-- Select the score and name columns from the second_table where name is not null
-- Order the results by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

