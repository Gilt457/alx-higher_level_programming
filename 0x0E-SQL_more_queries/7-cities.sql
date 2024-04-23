-- This code creates a new database called hbtn_0d_usa and switches to it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- This code creates a new table called cities with four columns: id, state_id, name, and a foreign key constraint
CREATE TABLE IF NOT EXISTS cities (
  id INT UNIQUE AUTO_INCREMENT NOT NULL, -- This column is the primary key and has an auto-incrementing value
  state_id INT NOT NULL, -- This column references the id column of the states table
  name VARCHAR(256) NOT NULL, -- This column stores the name of the city
  PRIMARY KEY(id), -- This constraint ensures that the id column is unique and not null
  FOREIGN KEY(state_id) REFERENCES states(id) -- This constraint ensures that the state_id column matches a valid id from the states table
);
