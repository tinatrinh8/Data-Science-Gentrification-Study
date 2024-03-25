SELECT 
    p."Structure_Type",
    COUNT(p."Permit_Key") AS Count_of_Permits_by_Structure_Type
FROM 
    "BuildingPermitsDimension" p
GROUP BY 
    p."Structure_Type";
