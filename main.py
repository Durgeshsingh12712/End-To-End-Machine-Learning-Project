from src.wineQualityPrediction import logger
from src.wineQualityPrediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.wineQualityPrediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.wineQualityPrediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.wineQualityPrediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.wineQualityPrediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<\n\nx=========x")

except Exception as e:
    logger.exception(e)
    raise e