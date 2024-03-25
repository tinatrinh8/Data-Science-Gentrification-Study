SELECT
    wft."Ward_ID",
    ed."Employment",
    COUNT(*) AS "Number_Of_Employees",
    wft."Population"
FROM
    "ward_profile_fact_table" wft
INNER JOIN
    "EmploymentDimension" ed ON ed."Employment_Key" = ed."Employment_Key"
GROUP BY
    wft."Ward_ID",
    ed."Employment",
    wft."Population"
ORDER BY
    wft."Ward_ID",
    "Number_Of_Employees" DESC;
