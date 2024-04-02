SELECT 
    sd."Household_Type",
    wp."Year",
    AVG(sd."Average_Monthly_Shelter_Costs") AS "AvgShelterCosts",
    AVG(sd."Percent_Spending_30_Percent_Or_More_On_Shelter") 
	AS "AvgPercentSpendingMoreThan30Pct",
    SUM(wp."Population") AS "TotalPopulation"
FROM 
    "ShelterDimension" sd
JOIN 
    "ward_profile_fact_table" wp ON sd."Shelter_Key" = wp."Dimension_Key"
GROUP BY 
    sd."Household_Type", 
    wp."Year"
ORDER BY 
    wp."Year", 
    sd."Household_Type";
