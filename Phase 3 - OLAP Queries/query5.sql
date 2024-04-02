SELECT 
    d."Year",
	COUNT(*) AS "TotalDemolitions",
	SUM(dd."Affordable Rental Homes for Demolition") AS "TotalAffordableDemolitions",
	SUM(dd."Mid-Range Rental Homes for Demolition") AS "TotalMidRangeDemolitions",
	SUM(dd."High-End Rental Homes for Demolition") AS "TotalHighEndDemolitions",
	SUM(dd."Affordable Rental Homes Replaced") AS "TotalAffordableReplacements",
	SUM(dd."Mid-Range Rental Homes Replaced") AS "TotalMidRangeReplacements",
	SUM(dd."High-End Rental Homes Replaced") AS "TotalHighEndReplacements"
FROM 
    "DemolitionDimension" dd
JOIN 
    "DateDimension" d ON dd."Approval_Date_Key" = d."Date_Key"
GROUP BY 
    d."Year"
ORDER BY 
    d."Year";
