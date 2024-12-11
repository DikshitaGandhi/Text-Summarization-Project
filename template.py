import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

projectname='text Summarization'
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{projectname}/__init__.py",
    f"src/{projectname}/components/__init__.py",
    f"src/{projectname}/utils/__init__.py",
    f"src/{projectname}/utils/common.py",
    f"src/{projectname}/logging/__init__.py",
    f"src/{projectname}/config/__init__.py",
    f"src/{projectname}/config/configuration.py",
    f"src/{projectname}/pipeline/__init__.py",
    f"src/{projectname}/entity/__init__.py",
    f"src/{projectname}/constants/__init__.py",
    "config/config,yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Created empty file: {filepath}")


    else:
        logging.info(f"File {filepath} already exists and is not empty.")