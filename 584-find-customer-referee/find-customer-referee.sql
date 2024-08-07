/* Write your PL/SQL query statement below */
SELECT
    name 
FROM 
    Customer
WHERE
    referee_id is Null
    or referee_id !=2;