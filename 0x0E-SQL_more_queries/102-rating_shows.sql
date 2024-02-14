-- This query returns the title and the total rating of each TV show
-- It uses a left join to combine the tv_shows and tv_show_ratings tables
-- It groups the results by title and sorts them in descending order by rating
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
