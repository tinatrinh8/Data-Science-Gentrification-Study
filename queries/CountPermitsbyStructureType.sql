SELECT 
    w."Ward_ID",
    EXTRACT(YEAR FROM dt."Date") AS "Year",
    p."Structure_Type",
    COUNT(p."Permit_Key") AS "Count_of_Permits_by_Structure_Type"
FROM 
    "BuildingPermitsDimension" p
JOIN 
    "development_fact_table" d ON p."Permit_Key" = d."Permit_Key"
JOIN 
    "DateDimension" dt ON d."Application_Date_Key" = dt."Date_Key"
JOIN 
    "WardDimension" w ON d."Ward_ID" = w."Ward_ID"
GROUP BY 
    w."Ward_ID",
    EXTRACT(YEAR FROM dt."Date"),
    p."Structure_Type";
