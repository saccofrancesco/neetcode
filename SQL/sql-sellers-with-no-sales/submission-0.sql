-- Write your query below
SELECT seller_name
FROM seller
WHERE seller_id NOT IN (
    SELECT s.seller_id
    FROM seller AS s
    JOIN orders AS o ON o.seller_id = s.seller_id
    AND o.sale_date >= '2020-01-01' AND o.sale_date <= '2020-12-31'
)
ORDER BY seller_name