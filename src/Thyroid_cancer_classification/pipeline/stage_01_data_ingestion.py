from Thyroid_cancer_classification.config.configuration import ConfigurationManager
from Thyroid_cancer_classification.components.data_ingestion import DataIngestion
from Thyroid_cancer_classification import logger


STAGE_NAME = "Stage 01: Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx========x")
    except Exception as e:
        logger.error(f"Pipeline failed for {STAGE_NAME} with error: {str(e)}")
        raise e    