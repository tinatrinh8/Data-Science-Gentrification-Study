ALTER TABLE ward_profile_fact_table
ADD COLUMN Number_Of_Ethnic_Groups integer;

UPDATE ward_profile_fact_table w
SET Number_Of_Ethnic_Groups = subquery.Number_Of_Ethnic_Groups
FROM (
    SELECT 
        w."Ward_ID",
        w."Year", 
        COUNT(DISTINCT e."Ethnoculture") AS Number_Of_Ethnic_Groups
    FROM 
        "EthnoculturalDimension" e
    JOIN 
        ward_profile_fact_table w ON e."Ethnocultural_Key" = w."Dimension_Key"
    GROUP BY 
        w."Ward_ID", w."Year"
) AS subquery
WHERE w."Ward_ID" = subquery."Ward_ID" AND w."Year" = subquery."Year";
