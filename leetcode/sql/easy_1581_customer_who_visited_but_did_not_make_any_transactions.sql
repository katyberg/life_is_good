# Write your MySQL query statement below

# +----------+-------------+----------------+--------+
# | visit_id | customer_id | transaction_id | amount |
# +----------+-------------+----------------+--------+
# | 1        | 23          | 12             | 910    |
# | 2        | 9           | 13             | 970    |
# | 4        | 30          |                |        |
# | 5        | 54          | 2              | 310    |
# | 5        | 54          | 3              | 300    |
# | 5        | 54          | 9              | 200    |
# | 6        | 96          |                |        |
# | 7        | 54          |                |        |
# | 8        | 54          |                |        |
# +----------+-------------+----------------+--------+

SELECT
    v.customer_id,
    count(*) as count_no_trans
FROM
    Visits v
LEFT JOIN
    Transactions t
ON
    v.visit_id = t.visit_id
WHERE
    transaction_id IS NULL
GROUP BY
    v.customer_id  # IMPORTANT!!!! GROUP BY NEEDS TO BE AT THE END!!!!
;

# SELECT
#     v.customer_id,
#     count(*) as count_no_trans
# FROM
#     Visits v
# LEFT JOIN
#     Transactions t
# ON
#     v.visit_id = t.visit_id
# GROUP BY
#     v.customer_id
# WHERE
#     transaction_id IS NULL  # MY
# ;

# Other people solution which is very similar....
# SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans 
# from Visits v 
# LEFT JOIN Transactions t 
# ON v.visit_id = t.visit_id  
# WHERE t.transaction_id IS NULL 
# GROUP BY v.customer_id; 

