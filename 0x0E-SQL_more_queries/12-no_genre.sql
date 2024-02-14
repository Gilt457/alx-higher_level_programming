-- This query returns the titles of all the shows in the tv_shows table
-- that do not have any genres associated with them in the tv_show_genres table.
-- It also returns NULL for the genre_id column for these shows.
-- The results are sorted by the show title in ascending order, followed by the genre_id in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
