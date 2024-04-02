SELECT 
    bp."Permit_Key",
    bp."Permit_Type",
    df."Est_Const_Cost",
    df."Ward_ID"
FROM 
    "BuildingPermitsDimension" bp 
JOIN 
    development_fact_table df ON bp."Permit_Key" = df."Permit_Key"
WHERE 
    df."Est_Const_Cost" > 10000000
	AND bp."Permit_Type" = 'New Houses'
