import json
import os

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
//
validate_mandatory_fields()
validate_supported_values()
validate_dependencies()
//
def validate_mandatory_fields(dataset):
  

def validate_supported_values(dataset):
  dataset_name = dataset.get("dataset_name")
  dataset_source_type = dataset.get("source_type")
  dataset_file_type = dataset.get("file_type")
  dataset_write_mode = dataset.get("write_mode")
  if not dataset.get("source_type") in SUPPORTED_SOURCE_TYPE:
    raise ValueError(f"Does not matches source type in dataset : {dataset.get(dataset_name)}")

if result["is_valid"] :
  valid_dataset.append(dataset)
else :
  invalid_dataset.append(result)
  
