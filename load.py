
import pandas as pd
import sqlite3
from pathlib import Path

#load extracted data into a database (SQLite here)
def load_data_replace(targetData, 
                      outputLoc, 
                      dbName="game_data.db", 
                      tblName = "gen_game_data"):   ###this version replaces any exisitng db of the same name
    
    try:
        print("loading data")
        db_path = Path(outputLoc) / dbName
        with sqlite3.connect(db_path) as connection:
            targetData.to_sql(tblName, 
                              connection, 
                              if_exists='replace', 
                              index=False)
    except Exception as e:
        print("data loading failed: ", e)

#run a sql schema 
def run_sql_script(db_path_loc, target_script, db_name="game_data.db"):
    try:
        schema_path = Path(db_path_loc) / db_name
        with sqlite3.connect(schema_path) as connection:   #similar setup to load_data_replace()
            connection.executescript(target_script.read_text())         #use executescript() with read_text() on target to execute script
        print("SQL script run successfully")
    except Exception as e:
        print("SQL script failed: ", e)