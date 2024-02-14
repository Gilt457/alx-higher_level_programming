-- This SQL statement creates a table called force_name in the database if it does not exist already.
-- The table has two columns: id (an integer) and name (a string of up to 256 characters) that cannot be null.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
