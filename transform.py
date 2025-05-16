
import pandas as pd
import numpy as np

#important variables
data_dir = "data/"
csv_data = "collected_data.csv"

#load key data
#def load_csv_data(directory, csvName, workingName):
#    workingName = pd.read_csv(f"{directory}{csvName}")
#    print("csv file loaded")

#load_csv_data(data_dir, csv_data, "game_data")
game_data = pd.read_csv(f"{data_dir}{csv_data}")

print(game_data.info()) #inspect data, see what we are working with

#identify key variables
#revenue, downloads, session_duration, sessions_per_day
#all seem pretty important to revenue overall
#session_duration, sessions_per_day, and downloads can be analyzed together

#export "transformed_data" to csv for loading. consider alternative versions that append to existing data stores in best way
game_data.to_csv(f"{data_dir}transformed_data.csv") 
print("transformed data exported successfully")