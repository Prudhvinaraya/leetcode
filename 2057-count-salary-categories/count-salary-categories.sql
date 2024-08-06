/* Write your PL/SQL query statement below */
(select 'Low Salary' category ,count(case when income<20000 then 1 end )as accounts_count from Accounts)
UNION
(select 'Average Salary' category,count(case when income>=20000 and income <=50000 then 1 end)as accounts_count from Accounts)
UNION
(select 'High Salary' category,count(case when income >50000 then 1 end )as accounts_count from Accounts)
