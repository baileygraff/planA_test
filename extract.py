
import pandas as pd
import numpy as np

#variable declaration >> can be consilidated to config file in future
#data_loc = "data/raw/"
#testData = 'test.json'

#load JSON REST API data response
#def load_json_data(directory, inputData, working_name):
#    working_name = pd.read_json(f"{directory}{inputData}")
#    print(f"{testData} successfully loaded")

#load_json_data(data_dir, testData, api_data)

#api_json = pd.read_json("data/test.json")

#extracted_data = pd.DataFrame(api_json)
#print(extracted_data.info())  #check work

#export extracted data as csv
#extracted_data.to_csv(f"{data_dir}collected_data.csv")
#next step: redefine this as a function that can be called

###upgrade1 work below (mostly)###

def extract_json(data_location, targetData):
    try:
        print('extracting json data')
        return pd.read_json(f"{data_location}{targetData}") 
    except Exception as e:
        print('json extraction failed: ', e)
        return pd.DataFrame()  #still returns an empty dataframe object to limit problems downstream

