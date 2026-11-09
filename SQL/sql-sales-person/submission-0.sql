-- Write your query below
SELECT name
FROM sales_person
WHERE sales_id NOT IN (
    SELECT s.sales_id
    FROM sales_person AS s
    JOIN orders AS o ON o.sales_id = s.sales_id
    JOIN company AS c ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
)