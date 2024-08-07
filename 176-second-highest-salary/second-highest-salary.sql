SELECT 
    Max(Salary) as SecondHighestSalary
    from 
    Employee 
    where Salary <>(SELECT Max(Salary) from Employee);