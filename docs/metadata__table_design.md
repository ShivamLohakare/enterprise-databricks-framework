| Column Name    | Data Type     | Mandatory   | Description                  |
| -------------- | ------------- | ----------- | ---------------------------- |
| dataset_id     | INT           | Yes         | Unique dataset identifier    |
| dataset_name   | STRING        | Yes         | Business dataset name        |
| source_type    | STRING        | Yes         | file/sqlserver/snowflake/api |
| source_path    | STRING        | Conditional | Source location              |
| file_format    | STRING        | Conditional | csv/parquet/delta            |
| target_catalog | STRING        | Yes         | Unity Catalog                |
| target_schema  | STRING        | Yes         | bronze/silver/gold           |
| target_table   | STRING        | Yes         | Destination table            |
| write_mode     | STRING        | Yes         | overwrite/append/merge       |
| primary_keys   | ARRAY<STRING> | No          | Business keys                |
| schema_evolution_enabled | BOOLEAN | Yes     | Schema Change Accetance field|
| active_flag    | BOOLEAN       | Yes         | Enable/disable processing    |
