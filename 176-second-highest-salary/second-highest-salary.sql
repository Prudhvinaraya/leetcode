# Write your MySQL query statement belowsw
SELECT 
IFNULL(
(SELECT DISTINCT 
Salary 
from Employee
Order By Salary Desc
LIMIT 1,1 ),NULL) as SecondHighestSalary;