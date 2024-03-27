SELECT 
    wd."Ward_Name",
    w."Year",
    e."Employment" AS "Occupation_Category",
    COUNT(*) AS "Count", -- Or use SUM(w."Population") if you're looking to sum up a population figure instead of counting entries
    SUM(w."Population") AS "Total_Population_in_Occupation"
FROM 
    "EmploymentDimension" e
JOIN 
    "ward_profile_fact_table" w ON e."Employment_Key" = w."Dimension_Key"
JOIN 
    "WardDimension" wd ON w."Ward_ID" = wd."Ward_ID"
GROUP BY 
    wd."Ward_Name", w."Year", e."Employment";
