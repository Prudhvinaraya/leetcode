SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
LEFT JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    -- Subquery to get the maximum salary for each department
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
)
ORDER BY d.name, e.salary DESC;
