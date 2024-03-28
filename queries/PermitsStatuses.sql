SELECT 
    d."Ward_ID",
    dt."Year",
    b."Status",
    COUNT(*) AS "Permit_Count"
FROM 
    "development_fact_table" d
JOIN 
    "BuildingPermitsDimension" b ON d."Permit_Key" = b."Permit_Key"
JOIN 
    "DateDimension" dt ON d."Issued_Date_Key" = dt."Date_Key"
GROUP BY 
    d."Ward_ID", dt."Year", b."Status"
ORDER BY 
    d."Ward_ID", dt."Year", b."Status";
