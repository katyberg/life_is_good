# Write your MySQL query statement below

# Use User as base (because we want "for each user")
# left join buyer_id with Orders table
# then filter down to 2019
# then group and count

# +---------+------------+----------------+----------+-----------+----------+------------+---------+
# | user_id | join_date  | favorite_brand | buyer_id | seller_id | order_id | order_date | item_id |
# +---------+------------+----------------+----------+-----------+----------+------------+---------+
# | 1       | 2018-01-01 | Lenovo         | 1        | 2         | 1        | 2019-08-01 | 4       |
# | 1       | 2018-01-01 | Lenovo         | 1        | 3         | 2        | 2018-08-02 | 4       |
# | 2       | 2018-02-09 | Samsung        | 2        | 3         | 3        | 2019-08-03 | 3       |   # | 2       | 2018-02-09 | Samsung        | 2        | 4         | 6        | 2019-08-05 | 2       |
# ---- Below are filtered out!
# | 3       | 2018-01-19 | LG             | 3        | 4         | 5        | 2018-08-04 | 1       |
# | 4       | 2018-05-21 | HP             | 4        | 2         | 4        | 2018-08-04 | 1       |
# +---------+------------+----------------+----------+------------+---------+----------+-----------+

SELECT
    u.user_id as buyer_id,
    u.join_date,
    count(o.order_id) as orders_in_2019
FROM
    Users u
LEFT JOIN
    Orders o
ON
    u.user_id = o.buyer_id
    AND YEAR(o.order_date)='2019'  # NOTE THAT THIS IS A JOIN CONDITION NOT WHERE CLAUSE!!!!
# WHERE
#     o.order_date IS NULL
#     OR
#     # DATEPART("year", order_date) = 2019  # MySQL does not have DATEPART, that's for PostgresSQL.
#     EXTRACT(YEAR FROM o.order_date) = 2019
GROUP BY
    user_id
;

# The query then performs a LEFT JOIN with the Orders table (aliased as o). This kind of join ensures that even users without matching orders (i.e., users who made no purchases) will still be included in the result.
# Two conditions are applied for the join:
# Matching users in the Users table with buyers in the Orders table based on their IDs.
# Filtering the orders to only include those from the year 2019.
