# Write your MySQL query statement below
SELECT e.name as Employee
FROM Employee as e
INNER JOIN Employee as m 
ON m.id = e.managerID
WHERE e.salary > m.salary 