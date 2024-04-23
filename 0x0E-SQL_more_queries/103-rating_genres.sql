-- This query calculates the total rating of each genre by summing up the ratings of the shows that belong to that genre
-- It uses INNER JOIN to combine three tables: tv_genres, tv_show_genres, and tv_show_ratings
-- It groups the results by the name of the genre and sorts them in descending order by the rating
SELECT name, SUM(tv_show_ratings.rate) 'rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
