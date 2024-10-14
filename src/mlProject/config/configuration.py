from mlProject.constants import *  # Make sure this import works
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=Path(r"C:\Users\DELL\Documents\End-to-end-Machine-learning-project\config\config.yaml").resolve(),
        params_filepath=Path(r"C:\Users\DELL\Documents\End-to-end-Machine-learning-project\params.yaml").resolve(),
        schema_filepath=Path(r"C:\Users\DELL\Documents\End-to-end-Machine-learning-project\schema.yaml").resolve(),
    ):
        # Load YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Create the artifacts root directory
        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']

        # Create the data ingestion root directory
        create_directories([config['root_dir']])

        # Return DataIngestionConfig instance
        data_ingestion_config = DataIngestionConfig(
            root_dir=config['root_dir'],
            source_URL=config['source_URL'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

