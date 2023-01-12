from datetime import datetime
from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    feature_store_file_path:str
    metadata_file_path:str
    download_dir:str


@dataclass
class DataValidationArtifacts:
    accepted_file_path:str
    rejected_dir:str