SELECT
    dft."Ward_ID",
    dd."Year",
    AVG(dft."Application_to_Issuance_Duration") AS "AverageProjectDuration",
    RANK() OVER (PARTITION BY dd."Year" ORDER BY AVG(dft."Application_to_Issuance_Duration") DESC) AS "DurationRank"
FROM
    "development_fact_table" dft
JOIN
    "DateDimension" dd ON dft."Application_Date_Key" = dd."Date_Key"
WHERE
    dd."Year" BETWEEN EXTRACT(YEAR FROM CURRENT_DATE) - 5 AND EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY
    dft."Ward_ID",
    dd."Year"
ORDER BY
    dd."Year" DESC, "AverageProjectDuration" DESC;
