from Thyroid_cancer_classification import logger
from Thyroid_cancer_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from Thyroid_cancer_classification.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Thyroid_cancer_classification.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline



STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.error(f"Pipeline failed for {STAGE_NAME} with error: {str(e)}")
    raise e


STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.error(f"Pipeline failed for {STAGE_NAME} with error: {str(e)}")
    raise e


STAGE_NAME = "Data Transformation"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
        logger.exception(e)
        raise e

