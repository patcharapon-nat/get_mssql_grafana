# get_mssql_grafana

CREATE TABLE view_schema_check.input_trigger
(
`server_number` String,
`interface_number` String,
`TotalRecords` Int64,
`GroupedDateTime` DateTime('Asia/Bangkok'),
`TimeStamp` DateTime DEFAULT toDateTime(now(),'Asia/Bangkok')
)
ENGINE = MergeTree
ORDER BY GroupedDateTime
SETTINGS index_granularity = 8192;

---

CREATE OR REPLACE TABLE view_schema_check.input_trigger
(

    `server_number` String,

    `interface_number` String,

    `interface_name` String,

    `timestamp` DateTime,

    `TineStamp` DateTime

)
ENGINE = MergeTree
ORDER BY timestamp
SETTINGS index_granularity = 8192;

CREATE TABLE view_schema_check.input_trigger
(

    `server_number` String,

    `interface_number` String,

    `timestamp` DateTime,

    `TineStamp` DateTime,

)
ENGINE = MergeTree
ORDER BY GroupedDateTime
SETTINGS index_granularity = 8192;

CREATE or replace TABLE view_schema_check.input_trigger
(

    `server_number` String,

    `interface_number` String,

    `timestamp` String,

    `TimeStamp_now` DateTime

)
ENGINE = MergeTree
ORDER BY timestamp
SETTINGS index_granularity = 8192;
