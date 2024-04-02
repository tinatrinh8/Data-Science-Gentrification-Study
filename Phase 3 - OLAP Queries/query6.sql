SELECT 
    e."Employment" AS "OccupationType",
    w."Year",
    SUM(w."Population") AS "TotalPopulationForOccupation",
    AVG(w."No_Cert_Ratio") AS "AverageNoCertRatio"
FROM 
    "EmploymentDimension" e
JOIN 
    "ward_profile_fact_table" w ON e."Employment_Key" = w."Dimension_Key"
GROUP BY 
    e."Employment", 
    w."Year"
ORDER BY 
    w."Year", 
    e."Employment";
