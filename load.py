
import pandas as pd
import sqlite3

#key variables
#data_dir = "data/"

#load to sqlite db
#tables and views can be made easily via tool like SQLiteStudio

#load transformed_data.csv
#transformed_data = pd.read_csv(f"{data_dir}transformed_data.csv")
#print("transformed data loaded to environment")

#create & connect to sqlite DB
#connection = sqlite3.connect(f"{data_dir}game_data.db")
#print("connection established")

#load data file to sqlite DB >> into general_game_data table
#transformed_data.to_sql("general_game_data", connection, if_exists='replace')
#print("data loaded into SQLite Database")

#close connection
#connection.close()
#print("connection closed")

##########POST-MEETING // upgrade1 work below#############

#load extracted data into a database (SQLite here)
def load_data_replace(targetData, 
                      outputLoc, 
                      dbName="game_data", 
                      tblName = "gen_game_data"):   ###this version replaces any exisitng db of the same name
    
    try:
        print("loading data")
        with sqlite3.connect(f"{outputLoc}{dbName}.db") as connection:
            targetData.to_sql(tblName, 
                              connection, 
                              if_exists='replace', 
                              index=False)
    except Exception as e:
        print("data loading failed: ", e)

#run a sql schema 
def run_sql_script(db_path_loc, target_script, db_name="game_data.db"):
    try:
        with sqlite3.connect(f"{db_path_loc}{db_name}") as connection:   #similar setup to load_data_replace()
            connection.executescript(target_script.read_text())         #use executescript() with read_text() on target to execute script
        print("SQL script run successfully")
    except Exception as e:
        print("SQL script failed: ", e)