# Write your MySQL query statement below. Beats 34.16%
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id
;

# # Use FIRST_VALUE function. Beats 86.17% (this number changes TOO MUCH to be trusted!)
# # NOTE DISTINCT IS NEEDED BECAUSE:
# # | player_id | first_login |
# # | --------- | ----------- |
# # | 1         | 2016-03-01  |
# # | 1         | 2016-03-01  |
# # | 2         | 2017-06-25  |
# # | 3         | 2016-03-02  |
# # | 3         | 2016-03-02  |
# SELECT DISTINCT
#     a.player_id,
#     FIRST_VALUE(a.event_date) OVER (
#         PARTITION BY
#             a.player_id
#         ORDER BY
#             a.event_date ASC
#     ) AS first_login
# FROM
#     Activity a
# ;

# # Window function - but this problem is too simple for that! Beats 9.99% <= slowest!
# SELECT
#     ranked.player_id,
#     ranked.event_date AS first_login
# FROM (
#     SELECT
#         a.player_id,
#         a.event_date,
#         RANK() OVER (
#             PARTITION BY
#                 a.player_id
#             ORDER BY
#                 a.event_date ASC
#         ) AS rnk  # NOTICE rank IS A KEYWORD, CANNOT USE IT!!!!
#     FROM
#         Activity a
# ) ranked
# WHERE
#     ranked.rnk = 1
# ;

