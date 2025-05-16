
import pandas as pd
import numpy as np

#variable declaration >> can be consilidated to config file in future
data_dir = "data/"
testData = 'test.json'
json_keys = []

#load JSON REST API data response
#def load_json_data(directory, inputData, working_name):
#    working_name = pd.read_json(f"{directory}{inputData}")
#    print(f"{testData} successfully loaded")

#load_json_data(data_dir, testData, api_data)

api_json = pd.read_json("data/test.json")

extracted_data = pd.DataFrame(api_json)
#print(extracted_data.info())  #check work

#export extracted data as csv
extracted_data.to_csv(f"{data_dir}collected_data.csv")
#next step: redefine this as a function that can be called
