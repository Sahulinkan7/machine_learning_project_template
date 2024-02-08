import os,sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format="[%(asctime)s] : %(message)s")

list_of_files=[
    f"src/__init__.py",
    f"src/entity/__init__.py",
    f"src/entity/artifact_entity.py",
    f"src/entity/config_entity.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/data_validation.py",
    f"src/components/model_trainer.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/pipeline/training_pipeline.py",
    f"src/utils/__init__.py",
    f"src/utils/commonutils.py",
    f"src/constants/__init__.py",
    f"src/exception.py",
    f"src/logger.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    f"config/config.yaml",
    f"params.yaml",
    f"notebook/experiment.ipynb",
    f"setup.py",
    f"dvc.yaml",
    f"requirements.txt",
    f"requirements_dev.txt",
]


for file in list_of_files:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for filename {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        logging.info(f"file {filepath} already exist, can not be created again.")
