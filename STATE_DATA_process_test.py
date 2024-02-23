#Test code to run the processing script on a 
#single states data  - To test 
import os
import numpy as np
import pandas as pd
from cpq_tools import computeInfo
from STATE_DATA_setup import phi_data_path, \
     state_infant_long_files, missing_unknown_var_dict
from STATE_DATA import process_state_data_infant, \
            process_state_data_long, read_csv_stata

compute_info = computeInfo()
compute_info.info()

state = 'MI'
file_infant, file_long=state_infant_long_files[state]

#Process Infant dataset
file_path = phi_data_path + file_infant
df_raw = read_csv_stata(file_path)
df_processed = process_state_data_infant(df_raw, state=state,
            missing_unknown_variable_dict = missing_unknown_var_dict)
       
file_out = f"{state}_test.pkl"
df_processed.to_pickle(file_out)

print(df_processed.shape, df_processed.birth_year.value_counts())
compute_info.info()

