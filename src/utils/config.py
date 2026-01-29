"""Configuration management for the entire project."""
import os 
from pathlib import Path 
from typing import Dict, Any 
import yaml 
from dotenv import load_dotenv 

# Load environment variables from the .env file 
load_dotenv() 

# Project root directory 
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data paths 
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL = PROJECT_ROOT / "data" / "external"

# Model paths 
MODELS_DIR = PROJECT_ROOT / "models"

# ensuring the directories exist 
DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
DATA_EXTERNAL.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)

# now defining loading the Configuration
def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loading configuration from the YAML file. 

    Parameters
    ----------
    config_path: str 
        Path to config file relative to configs/directory 

    Returns 
    ----------
    Dict[str, Any]
        Configuration dictionary 
    """
    config_file = PROJECT_ROOT / "configs" / config_path
    with open(config_file , "r") as f: 
        config = yaml.safe_load(f)
    return config 

# Model hyperparameters from environment or defaults 
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 64))
LEARNING_RATE = float(os.getenv("LEARNING_RATE" , 0.001))
EPOCHS = int(os.getenv("EPOCHS", 50)) # loading all of these from the yaml file previously outlined 

# MLFlow configuration 
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "mlruns")
MLFLOW_EXPERIMENT_NAME = os.getenv(
        "MLFLOW_EXPERIMENT_NAME", "baseball-pitch-prediction"
        )
