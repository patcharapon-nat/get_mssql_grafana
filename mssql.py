import pymssql
import pandas as pd
import clickhouse_connect
import database as d

def input_data(server_input):
    conn = pymssql.connect(server=server_input, user='dmp_prd', password=d.user[0]['password'], database='vfinindb')
    cursor = conn.cursor()

    query = f"""
    SELECT 
        interface_number,
        COUNT(*) AS TotalRecords,
    DATEADD(MINUTE, DATEDIFF(MINUTE, 0, [timestamp]) / 1 * 1, 0) AS GroupedDateTime
    FROM 
        vfinindb.dbo.INPUT_TRIGGER
    GROUP BY 
    interface_number,
        DATEADD(MINUTE, DATEDIFF(MINUTE, 0, [timestamp]) / 1 * 1, 0)
    ORDER BY 
        GroupedDateTime;
    """

    cursor.execute(query)
    df1 = pd.DataFrame(cursor.fetchall())
    # print(df1.shape[0])
    columns = [column[0] for column in cursor.description]
    if cursor.rowcount > 0:
        df1.columns = columns
        print(df1)
        client = clickhouse_connect.get_client(host='10.99.5.244', username='default', password='cfgs123#')
        client.insert('view_schema_check.input_trigger',df1)
    else:
        print("No Row on server :" + server_input + "at database : vfinindb")
    cursor.close()
    print("--------------------------------------------------------------------")
for i in d.database:
    # print(i)
    input_data(i["server"])