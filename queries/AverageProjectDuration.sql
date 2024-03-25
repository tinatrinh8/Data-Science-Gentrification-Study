SELECT 
    d."Ward_ID",
    AVG(p."Completed_Date" - p."Application_Date") AS Average_Project_Duration
FROM 
    "BuildingPermitsDimension" p
JOIN 
    development_fact_table d ON p."Permit_Key" = d."Ward_ID"
GROUP BY 
    d."Ward_ID";