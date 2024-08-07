/* Write your PL/SQL query statement below */
select name from
(select managerId as mid, count(id) as dr
from Employee
where managerID IS not null
group by managerId) x
inner join Employee on x.mid=Employee.id
where dr>4 ;