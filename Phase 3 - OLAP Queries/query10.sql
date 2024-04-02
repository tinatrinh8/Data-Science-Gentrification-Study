SELECT 
    dft."Ward_ID",
    SUM(dft."Est_Const_Cost") AS "TotalHighEndConstructionCost"
FROM 
    "development_fact_table" dft
WHERE 
    dft."Est_Const_Cost" > 50000
GROUP BY 
    dft."Ward_ID"
ORDER BY 
    "TotalHighEndConstructionCost" DESC
LIMIT 5;
