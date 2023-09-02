# Write your MySQL query statement below

# Intuition:
# ASSUMING BOTH TABLES COMBINED COVER ALL EMPLOYEES....

# select 
#   employee_id
# from
#   Employees
# where
#   employee_id not in (select employee_id from Salaries)
# union
# select
#   employee_id
# from
#   Salaries
# where
#   employee_id not in (select employee_id from Employees)
# order by employee_id;

# BELOW I GOT Column 'employee_id' in field list is ambiguous WHICH I DON'T KNOW WHY?!?!
SELECT employee_id
FROM (
    SELECT e.employee_id FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL
    UNION
    SELECT s.employee_id FROM Salaries s
    LEFT JOIN Employees e ON s.employee_id = e.employee_id
    WHERE e.name IS NULL
) tmp
ORDER BY
    employee_id ASC
;

# BELOW PRODUCES SYNTAX ERROR BECAUSE MYSQL DOES NOT HAVE FULL OUTER JOIN!
# SELECT
#     e.employee_id
# FROM
#     Employees e
# FULL OUTER JOIN
#     Salaries s
# ON
#     e.employee_id = s.employee_id
# WHERE
#     e.salary IS NULL or s.name IS NULL
# ORDER BY
#     employee_id ASC
# ;
