-- This code creates a table called id_not_null in MySQL
-- The table has two columns: id and name
-- The id column is an integer with a default value of 1
-- The name column is a variable-length string of up to 256 characters
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
