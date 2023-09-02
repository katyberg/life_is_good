# Write your MySQL query statement below

# Intuition:
# If we aggregrate the order_number based on customer_number, 
# the customer_number with largest count is the answer


# If we return ONLY ONE of such customers
SELECT
    o.customer_number
FROM
    Orders o
GROUP BY
    o.customer_number
ORDER BY
    count(*) DESC
LIMIT 1
;

# # If we return ALL of such customers
# SELECT
#     o.customer_number
# FROM
#     Orders o
# GROUP BY
#     o.customer_number
# HAVING count(o.customer_number) >= all(
#     SELECT
#         count(*)
#     FROM
#         Orders
#     GROUP BY
#         customer_number
# )
# ;

# # Below works but have too many subqueries!
# SELECT
#     o.customer_number
# FROM
#     Orders o
# GROUP BY
#     o.customer_number
# HAVING count(*) = (
#     SELECT
#         MAX(cnt)
#     FROM (
#         SELECT
#             COUNT(customer_number) AS cnt
#         FROM
#             Orders
#         GROUP BY
#             customer_number
#     ) as tmp  # THIS IS NEEDED OTHERWISE GET "Every derived table must have its own alias"!!!!
# )
# ;

# # BELOW DOES NOT WORK! ERROR: Unknown column 'tmp.cnt' in 'window order by'
# SELECT
#     tmp.customer_number
# FROM (
#     SELECT
#         o.customer_number,
#         count(*) AS cnt,
#         DENSE_RANK() OVER (ORDER BY tmp.cnt DESC) AS rnk
#     FROM
#         Orders o
#     GROUP BY
#         o.customer_number
# ) AS tmp
# WHERE
#     tmp.rnk = 1
# ;

