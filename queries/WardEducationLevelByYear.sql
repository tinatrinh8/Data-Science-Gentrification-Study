SELECT
    wd."Ward_ID",
    ed."Education_Level",
    wd."Year"
FROM
    "ward_profile_fact_table" wd
JOIN
    "EducationDimension" ed ON wd."Dimension_Key" = ed."Education_Key"
JOIN
    "DateDimension" dd ON wd."Year" = dd."Year"
GROUP BY
    wd."Ward_ID",
    ed."Education_Level",
    wd."Year";
