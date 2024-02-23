"""
STATE_DATA_ANALYSIS.py

Analysis of STATE_DATA dataset, created by:
        STATE_DATA_PROCESS.py

"""
#Test ability to add conventional commits
import os
import pandas as pd
from cpq_tools import computeInfo
from STATE_DATA_setup import phi_data_path, \
          var_key_dict, var_desc_dict, study_vars_all

compute_info = computeInfo()
compute_info.info()

quick = True #Default to quick analysis

file_use = 'STATE_DATA_infant_full.pkl'
if quick:
    file_use = 'STATE_DATA_infant_quick.pkl'
#First, run on the test file
file_use = 'MI_test.pkl'

dat = pd.read_pickle(os.path.join(phi_data_path, file_use))
study_vars_all = [var for var in study_vars_all if var in dat.columns]

#Loop over the list of variables
for var in study_vars_all:
    desc = var_desc_dict[var]
    print(desc)
    print(dat[var].value_counts().head(5))
    print('')

re_var_use = 'racem_na'
re_var_key = var_key_dict[re_var_use]
print(dat[re_var_use].value_counts().replace(re_var_key))

#TODO
#RE (%) by State
#Construct frequency tables
#Years, by state - including missing
#RE, by state - incluing missing
#Construct missingness report
#First, overall missingness, verifying that all desired variables present
