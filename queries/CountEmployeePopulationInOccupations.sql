SELECT
    ed."Employment",
    COUNT(*) AS "Number_Of_Employees",
    wft."Population"
FROM
    "ward_profile_fact_table" wft
INNER JOIN
    "EmploymentDimension" ed ON ed."Employment_Key" = ed."Employment_Key"
GROUP BY
    ed."Employment",
    wft."Population"
ORDER BY
    "Number_Of_Employees" DESC;