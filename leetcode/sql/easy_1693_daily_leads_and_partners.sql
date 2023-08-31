# Write your MySQL query statement below
SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM
    DailySales
GROUP BY
    date_id, make_name
;


# # Pandas
# import pandas as pd
# def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
#     df = daily_sales.groupby(['date_id', 'make_name']).agg({
#         'lead_id': 'nunique',
#         'partner_id': 'nunique'
#     }).reset_index()
#     df = df.rename(columns={  # rename
#         'lead_id': 'unique_leads',
#         'partner_id': 'unique_partners'
#     })
#     return df

