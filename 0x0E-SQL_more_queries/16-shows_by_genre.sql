-- Selects the title of each show and the name of each genre associated with it
-- Joins the tv_shows table with the tv_show_genres table on the show_id column
-- Joins the tv_genres table with the tv_show_genres table on the genre_id column
-- Sorts the results by the title of the show in ascending order, and then by the name of the genre in ascending order
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;
