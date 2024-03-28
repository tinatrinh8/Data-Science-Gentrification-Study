SELECT 
    dt."Year",
    COUNT(d."Permit_Key") AS Permits_Issued
FROM 
    "development_fact_table" d
JOIN 
    "DateDimension" dt ON dt."Date_Key" = dt."Date_Key"
GROUP BY 
    dt."Year";
