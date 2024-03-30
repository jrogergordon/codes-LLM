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