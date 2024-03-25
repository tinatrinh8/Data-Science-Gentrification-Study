WITH AgeDistributions AS (
    SELECT wpf."Ward_ID", ad."Age_Range", wpf."Population"
    FROM "ward_profile_fact_table" wpf
    JOIN "AgeDimension" ad ON ad."Age_Key" = wpf."Dimension_Key"
)
SELECT "Ward_ID", 
       (SELECT "Age_Range" 
        FROM (SELECT "Age_Range", 
                     row_number() OVER (ORDER BY "Age_Range") as rn, 
                     count(*) OVER () as cnt 
              FROM AgeDistributions as ad2 
              WHERE ad2."Ward_ID" = ad."Ward_ID") as sub 
        WHERE rn = (cnt + 1) / 2) AS Median_Age
FROM AgeDistributions as ad
GROUP BY "Ward_ID";