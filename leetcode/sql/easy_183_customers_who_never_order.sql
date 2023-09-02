# Write your MySQL query statement below
SELECT
    c.name AS Customers
FROM
    Customers c
WHERE
    c.id NOT IN (
        SELECT
            DISTINCT o.customerId
        FROM
            Orders o
    )
;

