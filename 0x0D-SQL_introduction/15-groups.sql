-- Script to list the number of records with the same score in the table second_table of the database hbtn_0c_0

-- Select the score and count the number of records for each score
-- Group the results by score and order by the number of records in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
