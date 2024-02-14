-- Script to list the number of shows linked to each genre from hbtn_0d_tvshows.

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
