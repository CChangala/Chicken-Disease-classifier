import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name = 'cnn_classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f".src{project_name}/_init_.py",
    f".src{project_name}/components/_init_.py",
    f".src{project_name}/utils/_init_.py",
    f".src{project_name}/config/configuration/_init_.py",
    f".src{project_name}/pipeline/_init_.py",
    f".src{project_name}/entity/_init_.py",
    f".src{project_name}/constants/_init_.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipnyb",
]

for file_path in list_of_files:
    filepath = Path(file_path)
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True)
        logging.info(f"Creating directory: {filepath.parent}")
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Creating file: {filepath}")  # noqa
    else: 
        logging.info(f"File already exists: {filepath}")
