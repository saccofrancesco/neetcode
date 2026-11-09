-- Write your query below
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance
FROM users AS u
LEFT JOIN rides AS r ON r.user_id = u.id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC