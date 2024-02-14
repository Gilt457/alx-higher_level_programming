-- Query to find the number of shows for each genre
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
-- Join the tables tv_genres and tv_show_genres by matching the genre ids
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
-- Group the results by genre name
GROUP BY genre
-- Sort the results in descending order by number of shows
ORDER BY number_of_shows DESC;
