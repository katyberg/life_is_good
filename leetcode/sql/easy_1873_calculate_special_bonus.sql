# # Write your MySQL query statement below
# SELECT
#     employee_id,
#     IF(employee_id % 2 = 1 AND name NOT REGEXP '^M', salary, 0) AS bonus
# FROM
#     employees
# ORDER BY
#     employee_id
# ;

# This should work for postgres too!
SELECT
    employee_id,
    CASE
        WHEN
            employee_id % 2 = 1
            AND name NOT REGEXP '^M'
            # AND LEFT(name, 1) != 'M'  # this works too!
        THEN
            salary
        ELSE
            0
    END
    AS bonus
FROM
    employees
ORDER BY
    employee_id
;

