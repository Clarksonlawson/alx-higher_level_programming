-- Script to create the table unique_id with id and name columns, where id has a default value of 1 and must be unique.

-- Create the table unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
