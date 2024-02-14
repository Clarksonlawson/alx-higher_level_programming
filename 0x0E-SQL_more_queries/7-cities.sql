-- Script to create the table cities with id, state_id, and name columns, where state_id is a FOREIGN KEY.

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
