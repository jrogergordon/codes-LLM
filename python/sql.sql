WITH daily_amount AS (
    SELECT 
        visited_on, 
        SUM(amount) AS amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS row_num
    FROM 
        Customer
    GROUP BY 
        visited_on
)
SELECT 
    visited_on, 
    ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
FROM 
    daily_amount
WHERE 
    row_num > 6
ORDER BY 
    visited_on;