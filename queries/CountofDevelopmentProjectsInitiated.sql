SELECT 
    dt."Date_Key",
    w."Ward_ID",
    COUNT(p."Permit_Key") AS Count_of_Development_Projects_Initiated
FROM 
    "development_fact_table" d
JOIN 
    "BuildingPermitsDimension" p ON d."Permit_Key" = p."Permit_Key"
JOIN 
    "DateDimension" dt ON d."Application_Date_Key"= dt."Date_Key" AND p."Application_Date" = dt."Date"
JOIN 
    "WardDimension" w ON d."Ward_ID" = w."Ward_ID"
WHERE
    p."Status" = 'Initiated' -- Replace 'Initiated' with the appropriate status indicator from your data
GROUP BY 
    dt."Date_Key", w."Ward_ID";
