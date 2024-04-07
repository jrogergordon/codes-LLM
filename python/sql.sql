SELECT m.title AS results
FROM Movies m
WHERE m.movie_id = (
    SELECT mr.movie_id
    FROM MovieRating mr
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);
