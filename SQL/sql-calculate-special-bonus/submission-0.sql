-- Write your query below
SELECT employees.employee_id,
    CASE 
        WHEN employees.employee_id % 2 = 1 AND employees.name NOT LIKE 'M%' THEN employees.salary ELSE 0
    END AS bonus
FROM employees
ORDER BY employees.employee_id