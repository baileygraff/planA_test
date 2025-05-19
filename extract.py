
import pandas as pd
import numpy as np
from pathlib import Path

#function to extract json data and return it as pandas dataframe
#takes data location (filepath) and target (file name)
def extract_json(data_location, targetData):
    try:
        print('extracting json data')
        json_path = Path(data_location) / targetData
        return pd.read_json(json_path) 
    except Exception as e:
        print('json extraction failed: ', e)
        return pd.DataFrame()  #still returns an empty dataframe object to limit problems downstream

