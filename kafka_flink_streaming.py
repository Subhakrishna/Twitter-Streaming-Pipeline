from pyflink.table import TableEnvironment, EnvironmentSettings


env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)


t_env.get_config().get_configuration().set_string(
    "pipeline.jars",
    "C:/Users/Subha/Downloads/flink-sql-connector-kafka-1.17.0.jar"
)



# Define source table DDL
source_ddl = """
    CREATE TABLE source_table(
        textID BIGINT,
        text VARCHAR,
        selected_text VARCHAR,
        sentiment VARCHAR
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'tweets',
        'properties.bootstrap.servers' = 'localhost:9092',
        'scan.startup.mode' = 'latest-offset'
    )
"""

# Execute DDL statement to create the source table
t_env.execute_sql(source_ddl)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Define a SQL query to select all columns from the source table
sql_query = "SELECT * FROM source_table"

# Execute the query and retrieve the result table
result_table = t_env.sql_query(sql_query)

# Print the result table to the console
result_table.execute().print()
