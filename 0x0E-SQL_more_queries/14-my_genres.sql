-- This query selects the name of each genre from the tv_genres table
-- It joins the tv_show_genres table to get the genre_id for each show
-- It then joins the tv_shows table to get the title of each show
-- It filters the results by the title 'Dexter' to get only the genres of that show
-- It groups the results by the name of the genre to avoid duplicates
-- It orders the results by the name of the genre in ascending order
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;

