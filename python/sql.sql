SELECT 
    (SELECT name FROM Users WHERE user_id = (
        SELECT user_id FROM MovieRating GROUP BY user_id ORDER BY COUNT(*) DESC LIMIT 1)
     ) AS most_active_user,
    
    (SELECT title FROM Movies WHERE movie_id = (
        SELECT movie_id FROM MovieRating 
        WHERE EXTRACT(MONTH from created_at) = '02' AND EXTRACT(YEAR from created_at) = '2020'
        GROUP BY movie_id ORDER BY AVG(rating) DESC LIMIT 1)
     ) AS highest_rated_movie;  