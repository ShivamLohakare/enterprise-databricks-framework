SUPPORTED_SOURCE_TYPES = {"file", "sqlserver", "snowflake", "api"}
SUPPORTED_FILE_FORMATS = {"csv", "parquet", "delta"}
SUPPORTED_WRITE_MODES = {"overwrite", "append", "merge"}
SUPPORTED_STATUSES = {STATUS_STARTED, STATUS_SUCCESS, STATUS_FAILED, STATUS_SKIPPED}
MANDATORY_FIELDS = {"dataset_name", "source_type", "target_catalog", "target_schema", "target_table", "write_mode", "active_flag"}
DEPENDENCY_RULES = { "file" : ["source_path", "file_format"],
                     "sqlserver" : ["server", "database", "table"],
                     "snowflake" : ["account", "warehouse", "database", "schema", "table"],
                     "api" : ["base_url", "endpoint"]}
STATUS_STARTED = "STARTED"
STATUS_SUCCESS = "SUCCESS"
STATUS_FAILED = "FAILED"
STATUS_SKIPPED = "SKIPPED"
VALIDATION_MANDATORY_FIELDS = "MANDATORY_FIELDS"
VALIDATION_SUPPORTED_VALUES = "SUPPORTED_VALUES"
VALIDATION_DEPENDENCY = "DEPENDENCY"
