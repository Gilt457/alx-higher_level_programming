-- This query joins the cities and states tables on the state_id column and selects the id and name of each city along with the name of the corresponding state. The result is sorted by the city id in ascending order.
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
