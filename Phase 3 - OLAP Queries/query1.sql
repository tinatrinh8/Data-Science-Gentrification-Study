SELECT d."Year", d."Quarter", COUNT(*) AS "TotalPermitsPerQuarter"
FROM "BuildingPermitsDimension" p
JOIN "DateDimension" d ON p."Application_Date_Key" = d."Date_Key"
GROUP BY d."Year", d."Quarter"
ORDER BY d."Year", d."Quarter";
