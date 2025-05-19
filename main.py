
import pandas as pd
import numpy as np
from pathlib import Path

#local file imports
import extract as xt
#import transform as tf  ##considering moving transform process to SQL/SQLite > to be expressed in schema directory
import load as ld

###variables###
###in round 2 of upgrades, many of these will be redone with pathlib's Path fn
raw_data = "data/raw/"
output_dir = "data/output/"
json_data = "test.json"

#schema variables
schema01 = Path("schema") / "01_create_tables.sql"
schema02 = Path("schema") / "02_transforms.sql"
schema03 = Path("schema") / "03_views.sql"

####EXTRACT area####
workingData = xt.extract_json(raw_data, json_data)
#print(workingData.info())  #check work, inspect data

####LOAD area####
#load extracted data into SQLite database
ld.load_data_replace(workingData, output_dir)

#run SQL schema below
ld.run_sql_script(output_dir, schema01)
ld.run_sql_script(output_dir, schema02)
ld.run_sql_script(output_dir, schema03)

###notes###
#consider implementing path handling > all areas (main, extract, load), instead of f-strings as paths