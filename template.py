import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name = 'cnn_classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
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
