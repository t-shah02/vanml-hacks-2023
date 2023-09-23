from typing import Dict
from sklearn.pipeline import Pipeline
from joblib import dump, load

import os
import dotenv

dotenv.config()
MODELS_DIRECTORY = os.environ.get("MODELS_DIRECTORY", "./models")

def load_model(filename: str) -> Pipeline:
    model_filepath = os.path.join(MODELS_DIRECTORY, filename)
    model: Pipeline = load(model_filepath)
    return model

def load_models() -> Dict[str, Pipeline]:
    models: Dict[str, Pipeline] = {}  

    for filename in os.listdir(MODELS_DIRECTORY):
        model_filepath = os.path.join(MODELS_DIRECTORY, filename)
        model: Pipeline = load(model_filepath)
        models[filename] = model

    return models

def save_model(model: Pipeline, filename: str):
    model_filepath = os.path.join(MODELS_DIRECTORY, filename)
    dump(model, model_filepath)
    