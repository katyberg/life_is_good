# Write your MySQL query statement below
SELECT name
FROM customer
WHERE referee_id is NULL or referee_id != 2;  # IMPORTANT NULL has to be checked separately!

