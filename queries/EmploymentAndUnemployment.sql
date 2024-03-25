SELECT 
    w."Ward_ID",
    w."Year",
    CAST(SUM(CASE WHEN e."Employment" = 'Employed' THEN w."Population" ELSE 0 END) AS FLOAT) / NULLIF(SUM(w."Population"), 0) * 100.0 AS Employment_Rate,
    CAST(SUM(CASE WHEN e."Employment" = 'Unemployed' THEN w."Population" ELSE 0 END) AS FLOAT) / NULLIF(SUM(w."Population"), 0) * 100.0 AS Unemployment_Rate
FROM 
    "EmploymentDimension" e
JOIN 
    "ward_profile_fact_table" w ON e."Employment_Key" = w."Dimension_Key"
GROUP BY 
    w."Ward_ID", w."Year";