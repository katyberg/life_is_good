# Write your MySQL query statement below

# Intuition:
# Select from SalesPerson whose sales_ids do not exist in sales_id column in the Orders table
# where company is "RED"

SELECT
    sp.name
FROM
    SalesPerson sp
WHERE
    sp.sales_id NOT IN (
        SELECT
            DISTINCT sales_id
        FROM
            Orders o
        INNER JOIN
            Company c
        ON
            o.com_id = c.com_id
        WHERE
            c.name = 'RED'
    )
;
