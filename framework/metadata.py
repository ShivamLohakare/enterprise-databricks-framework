import json
import os

from framework.constants import (MANDATORY_FIELDS, SUPPORTED_SOURCE_TYPES, SUPPORTED_SOURCE_FORMATS, SUPPORTED_WRITE_MODES)
//
first load the metadata 
validate mandatory fields
validate supporting fields

def load_metadata(metadata_path):
  if not os.path.exists(metadata_path):
    raise FileNotFoundError(f"Metadata file not found : {metadata_path}")
  try :
    with open(metadata_path, 'r', encoding='utf-8') as file :
      metadata = json.load(file)
  except json.JSONDecodeError :
     raise ValueError(f"Invalid JSON found : {metadata_path}")
  if not metadata :
    raise ValueError(f"No metadata configurations found : {metadata_path}")
  return metadata

for dataset in metadata :
  def validate_mandatory_fields(dataset):
    dataset_name = dataset.get("dataset_name")
    missing_fields = []

    for field in MANDATORY_FIELDS :
      value = dataset.get(field)
      if value is None or value == "" :
        missing_fileds.append(field)
      if not missing_fields :
        return {
          "is_valid" : True
        }
      else :
        return {
          "is_valid" : False,
          "dataset_name" : dataset_name,
          "validation_type" : "MANDATORY FIELDS",
          "missing_fields" : missing_fields
        }
//
Logic: for validate_mandatory_fields
    1. Read dataset_name
    2. Create missing_fields list
    3. Loop through MANDATORY_FIELDS
    4. Check None or ""
    5. Return result
//

  def validate_supported_values(dataset):
    dataset_name = dataset.get("dataset_name")
    dataset_source_type = dataset.get("source_type")
    dataset_file_format = dataset.get("file_format")
    dataset_write_mode = dataset.get("write_mode")
    invalid_fields = []

    if dataset.get("source_type") not in SUPPORTED_SOURCE_TYPES :
        validation_error = {"field" : "source_type",
                "invalid_value" : dataset_source_type,
                "error_mesage" : "Unsupported Source Type"
               }
        invalid_fields.append(validation_error)
    if dataset.get("file_format") not in SUPPROTED_FILE_FORMATS :
        validation_error = {"field" : "file_format",
                "invalid_value" : dataset_file_format,
                "error_mesage" : "Unsupported File Format"
               }
        invalid_fields.append(validation_error)
    if dataset.get("write_mode") not in SUPPORTED_WRITE_MODES :
        validation_error = {"field" : "write_mode",
                "invalid_value" : dataset_write_mode,
                "error_mesage" : "Unsupported Write Mode"
               }
        invalid_fields.append(validation_error)
    if not invalid_fields :
      return {
        "is_valid" : True
      }
    else :
      return {
        "is_valid" : False,
        "dataset_name" : dataset_name,
        "validation_type" : "SUPPORTED_VALUES",
        "invalid_field" : invalid_field,
      }

  def validate_dependencies(dataset) :
    



  
