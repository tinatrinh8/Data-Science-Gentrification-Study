SELECT 
    (p."Street_Name" || ' ' || p."Street_Type" || ' ' || 
	 COALESCE(p."Street_Direction", '')) AS "FullStreetName",
    COUNT(*) AS "TotalPermits"
FROM 
    "BuildingPermitsDimension" p
GROUP BY 
    "FullStreetName"
ORDER BY 
    "FullStreetName";
