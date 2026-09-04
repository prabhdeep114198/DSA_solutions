# Write your MySQL query statement below
SELECT eu.unique_id , e.name from EMPLOYEES e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;