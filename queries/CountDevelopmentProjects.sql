SELECT 
    EXTRACT(YEAR FROM dt."Date") AS "Year",
    w."Ward_ID",
    COUNT(p."Permit_Key") AS "Count_of_Development_Projects"
FROM 
    "development_fact_table" d
JOIN 
    "BuildingPermitsDimension" p ON d."Permit_Key" = p."Permit_Key"
JOIN 
    "DateDimension" dt ON d."Application_Date_Key"= dt."Date_Key"
JOIN 
    "WardDimension" w ON d."Ward_ID" = w."Ward_ID"
GROUP BY 
    EXTRACT(YEAR FROM dt."Date"), w."Ward_ID";
