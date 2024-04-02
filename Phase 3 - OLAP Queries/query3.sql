SELECT 
    f."Ward_ID",
    w."Ward_Name",
    COUNT(*) AS "TotalPermitsWard13"
FROM 
    "development_fact_table" f
JOIN 
    "BuildingPermitsDimension" p 
	ON f."Permit_Key" = p."Permit_Key"
JOIN 
    "WardDimension" w ON f."Ward_ID" = w."Ward_ID"
WHERE 
    f."Ward_ID" = 13
GROUP BY 
    f."Ward_ID", w."Ward_Name";
