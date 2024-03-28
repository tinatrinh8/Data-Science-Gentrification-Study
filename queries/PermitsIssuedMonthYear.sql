SELECT 
    EXTRACT(YEAR FROM p."Issued_Date") AS Year,
    EXTRACT(MONTH FROM p."Issued_Date") AS Month,
    d."Permit_Key",
    d."Ward_ID",
    COUNT(p."Permit_Key") AS Permit_Count
FROM 
    "BuildingPermitsDimension" p
JOIN
    "development_fact_table" d ON p."Permit_Key" = d."Permit_Key"
WHERE
    p."Issued_Date" IS NOT NULL
GROUP BY 
    EXTRACT(YEAR FROM p."Issued_Date"), EXTRACT(MONTH FROM p."Issued_Date"), d."Permit_Key", d."Ward_ID"
ORDER BY 
    Year, Month;
