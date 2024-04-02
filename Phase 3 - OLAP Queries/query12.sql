SELECT 
    dft."Ward_ID",
    dd."Year",
    COUNT(dft."Permit_Key") AS PermitsIssued,
    LAG(COUNT(dft."Permit_Key"), 1) OVER (PARTITION BY dft."Ward_ID" ORDER BY dd."Year") AS PreviousYearPermits,
    LEAD(COUNT(dft."Permit_Key"), 1) OVER (PARTITION BY dft."Ward_ID" ORDER BY dd."Year") AS NextYearPermits
FROM 
    "development_fact_table" dft
JOIN 
    "DateDimension" dd ON dft."Issued_Date_Key" = dd."Date_Key"
GROUP BY 
    dft."Ward_ID", 
    dd."Year";
