WITH Population2016 AS (
    SELECT 
        e."Employment" AS "OccupationType",
        SUM(w."Population") AS "Population2016"
    FROM 
        "EmploymentDimension" e
    JOIN 
        "ward_profile_fact_table" w ON e."Employment_Key" = w."Dimension_Key"
    WHERE 
        w."Year" = 2016
    GROUP BY 
        e."Employment"
),
Population2021 AS (
    SELECT 
        e."Employment" AS "OccupationType",
        SUM(w."Population") AS "Population2021"
    FROM 
        "EmploymentDimension" e
    JOIN 
        "ward_profile_fact_table" w ON e."Employment_Key" = w."Dimension_Key"
    WHERE 
        w."Year" = 2021
    GROUP BY 
        e."Employment"
)
SELECT 
    p2016."OccupationType",
    p2016."Population2016",
    p2021."Population2021",
    (p2021."Population2021" - p2016."Population2016") AS "ChangeInPopulation"
FROM 
    Population2016 p2016
JOIN 
    Population2021 p2021 ON p2016."OccupationType" = p2021."OccupationType"
ORDER BY 
    "ChangeInPopulation" DESC;
