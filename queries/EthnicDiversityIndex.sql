SELECT 
    w."Ward_ID",
    w."Year", 
    COUNT(DISTINCT e."Ethnoculture") AS Number_Of_Ethnic_Groups
	
FROM 
    "EthnoculturalDimension" e
JOIN 
    ward_profile_fact_table w ON e."Ethnocultural_Key" = w."Dimension_Key"
GROUP BY 
    w."Ward_ID", w."Year"; 