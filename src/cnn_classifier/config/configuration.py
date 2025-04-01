from src.cnn_classifier.constants import *
from src.cnn_classifier.utils.common import read_yaml
from src.cnn_classifier.utils.common import create_directories
from src.cnn_classifier.entity.config_entity import DataIngestionConfig


class configurationManager():
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        return DataIngestionConfig(
            root_dir = Path(config.root_dir),
            source_url = config.source_URL,
            local_data_file = Path(config.local_data_file),
            unzip_dir = Path(config.unzip_dir)
        )