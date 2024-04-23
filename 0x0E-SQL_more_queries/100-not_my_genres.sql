-- select the name column from the tv_genres table
SELECT name
FROM tv_genres
-- filter out the names that are also in the subquery
WHERE name NOT IN
-- subquery to get the names of the genres that are linked to the show Dexter
(SELECT name
FROM tv_genres
-- join the tv_genres table with the tv_show_genres table on the id column
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- join the tv_show_genres table with the tv_shows table on the show_id column
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- filter the tv_shows table by the title column with the value 'Dexter'
WHERE tv_shows.title = 'Dexter')
-- group the results by the name column
GROUP BY name
-- order the results by the name column in ascending order
ORDER BY name ASC;
