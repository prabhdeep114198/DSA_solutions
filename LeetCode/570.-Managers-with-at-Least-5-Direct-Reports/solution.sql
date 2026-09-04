# Write your MySQL query statement below
SELECT e.name from Employee e
JOIN (
SELECT managerId FROM Employee
Where managerId is NOT NULL
GROUP BY managerID
HAVING count(*) >= 5
) m
ON e.id = m.managerId;