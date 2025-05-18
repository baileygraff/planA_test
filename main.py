
import pandas as pd
import numpy as np

#local file imports
import extract as xt
import transform as tf

###variables###
raw_data = "data/raw/"
json_data = "test.json"

####extract area####
workingData = xt.extract_json(raw_data, json_data)
print(workingData.info())  #check work