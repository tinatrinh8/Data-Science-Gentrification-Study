SELECT
    wd."Ward_ID",
	    wd."Year",
    ed."Income"
FROM
    "ward_profile_fact_table" wd
JOIN
    "IncomeDimension" ed ON wd."Dimension_Key" = ed."Income_Key";
