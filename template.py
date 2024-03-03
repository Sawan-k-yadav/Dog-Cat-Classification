import os
from pathlib import Path  #This Path library is used to handle any kind of path issue in any operating system
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "DogCatClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",   # This .github folder will be used for CI/CD pipeline action
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",                     # This setup.py used for creating local package
    "research/trails.ipynb"
]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    # Here we are checking this file path does not exist or if there is no data in that file then create 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass   # Creating an empty file here only
            logging.info(f"Creating Empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

