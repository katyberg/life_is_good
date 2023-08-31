# Write your MySQL query statement below
SELECT product_id
FROM products
WHERE low_fats = 'Y'  # even though these values are ENUM they are still queried like string
AND recyclable = 'Y';

