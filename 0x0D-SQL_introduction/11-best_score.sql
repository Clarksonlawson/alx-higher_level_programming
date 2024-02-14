-- Script to list all records with a score >= 10 in the table second_table of the database hbtn_0c_0

-- Select the score and name columns from the second_table where score is greater than or equal to 10
-- Order the results by score in descending order
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

