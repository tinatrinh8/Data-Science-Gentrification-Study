SELECT 
    f."Ward_ID",
    d."Year",
    COUNT(*) AS "TotalPermits"
FROM 
    "development_fact_table" f
JOIN 
    "BuildingPermitsDimension" p ON f."Permit_Key" = p."Permit_Key"
JOIN 
    "DateDimension" d ON p."Application_Date_Key" = d."Date_Key"
GROUP BY 
    f."Ward_ID", 
    d."Year"
ORDER BY 
    f."Ward_ID", 
    d."Year";
