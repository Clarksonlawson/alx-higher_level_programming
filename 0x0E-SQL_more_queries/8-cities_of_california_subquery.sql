-- Script to select all cities of California without using JOIN.

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select all cities of California
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
