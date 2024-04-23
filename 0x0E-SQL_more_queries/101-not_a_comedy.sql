-- This query selects the titles of all tv shows that do not have the genre Comedy
-- It uses a subquery to filter out the titles that are associated with the genre Comedy in the tv_genres table
SELECT title
FROM tv_shows
WHERE title NOT IN
-- This subquery selects the titles of all tv shows that have the genre Comedy
(SELECT title
FROM tv_shows
-- This join connects the tv_shows and tv_show_genres tables by their show_id columns
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- This join connects the tv_show_genres and tv_genres tables by their genre_id columns
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- This condition filters the rows where the genre name is Comedy
WHERE tv_genres.name = 'Comedy')
-- This clause groups the results by title
GROUP BY title
-- This clause sorts the results by title in ascending order
ORDER BY title ASC;
