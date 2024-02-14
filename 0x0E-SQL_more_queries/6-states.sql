-- Script to create the database hbtn_0d_usa and the table states with id and name columns.

-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
