
import pandas as pd
import sqlite3

#key variables
data_dir = "data/"

#load to sqlite db
#tables and views can be made easily via tool like SQLiteStudio

#load transformed_data.csv
transformed_data = pd.read_csv(f"{data_dir}transformed_data.csv")
print("transformed data loaded to environment")

#create & connect to sqlite DB
connection = sqlite3.connect(f"{data_dir}game_data.db")
print("connection established")

#load data file to sqlite DB >> into general_game_data table
transformed_data.to_sql("general_game_data", connection, if_exists='replace')
print("data loaded into SQLite Database")

#close connection
connection.close()
print("connection closed")