-- Script to create the table id_not_null with id and name columns, where id has a default value of 1.

-- Create the table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

