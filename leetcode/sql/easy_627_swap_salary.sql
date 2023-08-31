# Write your MySQL query statement below  

# # First approach  # beats 11.156%
# UPDATE
#     salary
# SET
#     sex = (
#         CASE
#         WHEN sex = 'f' THEN 'm'
#         WHEN sex = 'm' THEN 'f'
#         # what to do with ELSE
#         END
#     )
# ;

# # Better formatted provided by solution  # beats 17.43%
# UPDATE
#     salary
# SET
#     sex = (
#         CASE sex  # note that put 'sex' outside less verbose
#         WHEN 'f' THEN 'm'
#         WHEN 'm' THEN 'f'
#         # what to do with ELSE throw exception 
#         END
#     )
# ;

# Another way using IF  # beats 71.1%
UPDATE
    salary
SET
    sex = IF(sex='f', 'm', 'f')
;

