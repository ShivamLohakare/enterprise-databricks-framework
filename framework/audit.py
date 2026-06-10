from framework.constants import (STATUS_SUCCESS, STATUS_STARTED, STATUS_FAILED, STATUS_SKIPPED)

def get_dataset_context(dataset) :
  return {
    "dataset_id" : dataset.get("dataset_id"),
    "dataset_name" : dataset.get("dataset_name"),
    "target_catalog" : dataset.get("target_catalog"),
    "target_schema" : dataset.get("target_schema"),
    "target_table" : dataset.get("target_table"),
    "source_path" : dataset.get("source_path")
  }

def create_audit_record(dataset_context, status, validation_type, error_details, audit_run_id, timestamp):
  audit_record = dataset_context.copy()
  audit_record["status"] = status
  audit_record["validation_type"] = validation_type
  audit_record["error_details"] = error_details
  audit_record["audit_run_id"] = audit_run_id
  audit_record["timestamp"] = timestamp

  return audit_record


def generate_validation_audit_records(validation_result) :
  audit_records = []
  audit_run_id = 
  timestamp = 

  valid_datasets = validation_result.get("valid_datasets",[])
  invalid_datasets = validation_result.get("invalid_datasets",[])

  for datasets in valid_datasets :
    dataset_context = get_dataset_context("dataset")
    audit_record = create_audit_record(
      dataset_context = dataset_context,  
      status = STATUS_SUCCESS,
      validation_type = None,
      error_details = None,
      audit_run_id = audit_run_id,
      timestamp = timestamp)
    audit_records.append(audit_record)
    
  for datasets in invalid_datasets :
    dataset_context = get_dataset_context("dataset")
    audit_record = create_audit_record(
      dataset_context = dataset_context,  
      status = STATUS_FAILED,
      validation_type = None,
      error_details = None,
      audit_run_id = audit_run_id,
      timestamp = timestamp)
    audit_records.append(audit_record)
  return audit_records
  

