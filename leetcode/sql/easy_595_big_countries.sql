# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area >= 3000000  # assuming the unit is km2 which the table does not specify!
OR population >= 25000000;

