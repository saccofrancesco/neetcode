-- Write your query below
SELECT customers.name
FROM customers
WHERE customers.id NOT IN (SELECT orders.customer_id FROM orders)