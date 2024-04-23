-- This code creates and uses a database named hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- This code creates a table named states with two columns: id and name
-- The id column is an integer that is unique, not null, and auto-incremented
-- The name column is a variable-length string that is not null
-- The id column is also the primary key of the table
CREATE TABLE IF NOT EXISTS states (
  id INT UNIQUE NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY(id)
);
