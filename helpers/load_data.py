from typing import Dict
import dotenv
import os
import pandas as pd

dotenv.load_dotenv()

DATA_DIRECTORY = os.environ.get("DATA_DIRECTORY", './data')

def load_dataset(directory_name: str, filename: str) -> pd.DataFrame:
    data_filepath = os.path.join(DATA_DIRECTORY, directory_name, filename)
    return pd.read_csv(data_filepath)

def load_datafolder(directory_name: str) -> Dict[str, pd.DataFrame]:
    data_folderpath = os.path.join(DATA_DIRECTORY, directory_name)
    dfs: Dict[str, pd.DataFrame] = {}

    for filename in os.listdir(data_folderpath):
        data_filepath = os.path.join(data_folderpath, filename)
        df = pd.read_csv(data_filepath, parse_dates=[1, 2])
        dfs[filename] = df

    return dfs
