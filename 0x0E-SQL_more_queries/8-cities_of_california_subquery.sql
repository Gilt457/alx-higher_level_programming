-- This query selects the id and name of all the cities in California from the database hbtn_0d_usa
-- It uses a subquery to filter the state_id based on the name of the state
-- It sorts the results by id in ascending order
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
