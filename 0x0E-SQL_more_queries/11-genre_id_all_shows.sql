-- This query joins the tv_shows and tv_show_genres tables using a left join
-- It selects the title of each show and the corresponding genre id, if any
-- It sorts the results by the title in ascending order, and then by the genre id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
