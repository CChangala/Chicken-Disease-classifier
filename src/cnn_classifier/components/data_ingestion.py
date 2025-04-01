import os
import urllib.request as request
import zipfile
from cnn_classifier.entity.config_entity import DataIngestionConfig
from src.cnn_classifier import logger
from src.cnn_classifier.utils.common import get_size
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_url, 
                filename = self.config.local_data_file)
            logger.info(f"File downloaded at {filename} with info {header}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists of size {get_size(Path(self.config.local_data_file))}")

    def unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) 