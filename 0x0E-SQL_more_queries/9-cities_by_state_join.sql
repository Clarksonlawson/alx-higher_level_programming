9-cities_by_state_join.sql

-- Script to select all cities with their corresponding states using JOIN.

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select all cities with their corresponding states
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
