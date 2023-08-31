# Write your MySQL query statement below

# # Use Temporary table
# SELECT
#     pc.email AS Email
# FROM (
#     SELECT
#         p.email,
#         count(*) AS cnt
#     FROM
#         Person p
#     GROUP BY
#         email
# ) AS pc
# WHERE
#     pc.cnt > 1
# ;

# Use HAVING
SELECT
    email
FROM
    Person
GROUP BY
    email
HAVING count(email) > 1  # NOTE WHERE cannot use count therefore we use HAVING!!!!
;
