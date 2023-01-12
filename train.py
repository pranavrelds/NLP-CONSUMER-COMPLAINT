from src.pipelines.training_pipeline import TrainingPipeline
from src.DTO.input_dto import TrainingPipelineConfig

if __name__=="__main__":
    training_pipeline_config= TrainingPipelineConfig()
    training_pipeline = TrainingPipeline(training_pipeline_config=training_pipeline_config)
    training_pipeline.start()