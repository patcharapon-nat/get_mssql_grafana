# get_mssql_grafana

CREATE TABLE view_schema_check.input_trigger
(

    `interface_number` String,

    `TotalRecords` Int64,

    `GroupedDateTime` DateTime('Asia/Bangkok'),

    `TimeStamp` DateTime DEFAULT toDateTime(now(),

'Asia/Bangkok')
)
ENGINE = MergeTree
ORDER BY GroupedDateTime
SETTINGS index_granularity = 8192;

SELECT
interface_number,
COUNT(_) AS TotalRecords,
DATEADD(MINUTE, DATEDIFF(MINUTE, 0, [timestamp]) / 1 _ 1, 0) AS GroupedDateTime,
getdate() as TimeStamp
FROM
vfinindb.dbo.INPUT_TRIGGER
GROUP BY
interface_number,
DATEADD(MINUTE, DATEDIFF(MINUTE, 0, [timestamp]) / 1 \* 1, 0)
ORDER BY
GroupedDateTime;
