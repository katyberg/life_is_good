# Write your MySQL query statement below

# Intuition
# Join Rides with Users, aggregrate distances, order them first with distance DESC then name ASC


SELECT
    u.name AS name,
    WHEN
        SUM(r.distance) IS NOT NULL
    THEN
        SUM(r.distance) AS travelled_distance
    ELSE
        0 AS travelled_distance
    END
FROM
    Users u
LEFT JOIN
    Rides r
ON
    r.user_id = u.id
GROUP BY
    r.user_id
ORDER BY
    travelled_distance DESC, u.name ASC
;


# # Below query is MISSING Donald WHO HAS NO RIDE!!!!
# SELECT
#     u.name AS name,
#     SUM(r.distance) AS travelled_distance
# FROM
#     Rides r
# LEFT JOIN
#     Users u
# ON
#     r.user_id = u.id
# GROUP BY
#     r.user_id
# ORDER BY
#     travelled_distance DESC, u.name ASC
# ;
