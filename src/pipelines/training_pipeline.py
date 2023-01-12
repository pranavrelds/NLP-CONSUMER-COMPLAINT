import os,sys
from config.logger import logger, DetailedException
from src.DTO.input_dto import DataIngestionConfig
from src.DTO.output_dto import DataIngestionArtifacts

class TrainingPipeline:    
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.training_pipeline_config: TrainingPipelineConfig = training_pipeline_config

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifacts

        except Exception as e:
            raise DetailedException(e, sys)
