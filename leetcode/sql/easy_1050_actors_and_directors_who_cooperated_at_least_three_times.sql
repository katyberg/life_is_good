# Write your MySQL query statement below
SELECT
    ad.actor_id,
    ad.director_id
FROM
    ActorDirector ad
GROUP BY
    ad.actor_id, ad.director_id
HAVING count(*) >= 3
;

# # Pandas
# import pandas as pd
#
# def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
#     cnts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='counts')
#     return cnts[cnts['counts'] >= 3][['actor_id', 'director_id']]

