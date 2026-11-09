-- Write your query below
SELECT p.first_name, p.last_name, a.city, a.state
FROM person AS p
LEFT JOIN address AS a ON a.person_id = p.person_id