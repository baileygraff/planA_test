
import pandas as pd
import numpy as np
from pathlib import Path
import tomli

#local file imports
import extract as xt
import load as ld

###variables###
#use tomli to open config.toml for config mgmt
with open ("config.toml", "rb") as conf:
    config = tomli.load(conf)

#path handling via Path() on directory variables
RAW_DIR = Path(config["filepaths"]["raw_dir"])
OUT_DIR = Path(config["filepaths"]["output_dir"])

json_data = config["data"]["json_data"]

#schema variables -- still needs some config mgmt
schema01 = Path("schema") / "01_create_tables.sql"
schema02 = Path("schema") / "02_transforms.sql"
schema03 = Path("schema") / "03_views.sql"

####EXTRACT area####
workingData = xt.extract_json(RAW_DIR, json_data)
#print(workingData.info())  #check work, inspect data

####LOAD area####
#load extracted data into SQLite database
ld.load_data_replace(workingData, OUT_DIR)

#run SQL schema below 
ld.run_sql_script(OUT_DIR, schema01)
ld.run_sql_script(OUT_DIR, schema02)
ld.run_sql_script(OUT_DIR, schema03)

###notes###
#consider implementing path handling > all areas (main, extract, load), instead of f-strings as paths