
SELECT 
    w."Ward_ID",
    w."Year", -- Assuming 'Year' does not need double quotes; adjust if it's case-sensitive.
    COUNT(DISTINCT e."Ethnoculture") AS Number_Of_Ethnic_Groups
	
FROM 
    "EthnoculturalDimension" e
JOIN 
    ward_profile_fact_table w ON e."Ethnocultural_Key" = w."Dimension_Key"
GROUP BY 
    w."Ward_ID", w."Year"; -- Group by both Ward_ID and Year