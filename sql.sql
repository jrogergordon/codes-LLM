SELECT 
    P1.product_id,
    COALESCE(P2.new_price, 10) AS price
FROM 
    Products P1
LEFT JOIN 
    Products P2
ON 
    P1.product_id = P2.product_id AND 
    P2.change_date <= '2019-08-16'
GROUP BY  
    P1.product_id; 