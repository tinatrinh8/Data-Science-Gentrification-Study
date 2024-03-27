SELECT
    dt."Year",
    COUNT(df."Demolition_Key") AS Approved_Demolitions
FROM
    "demolition_fact_table" df
INNER JOIN
    "DateDimension" dt ON df."Approval_Date_Key" = dt."Date_Key"
INNER JOIN
    "DemolitionDimension" dm ON df."Demolition_Key" = dm."Demolition_Key"
GROUP BY
    dt."Year";
