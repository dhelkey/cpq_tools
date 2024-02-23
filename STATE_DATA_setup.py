"""
Setup code and parameters for STATE_DATA 

Usage:
from STATE_DATA_setup import variable1, variable2 

Requires:
    STATE_DATA_PRIVATE.py (NOT uploaded)

#TODO - Add tests (ensure data loads correctly with script changes)

"""
#Imports
import numpy as np
import pandas as pd
from cpq_tools import process_excel_variable_file

#Import parameters and settings from the PRIVATE file (not uploaded)
from STATE_DATA_PRIVATE import phi_data_path, \
    state_infant_long_files, file_var_documentation, file_vars_use

#Identifying Missing Values
#Constructs [variable]_na for variables with missing value codes
#Replaces variable specific missing value codes (0 or 9, depending on variable)
# with np.nan - "."
# This can simplify analysis in certain situations
# E.g. Missing value reports, consistant regression handling
# NOTE -  Caution needed when using for regression.
#  1. Statistical functions may drop NA values
# 2. Default comparison category may change for categorical variables
missing_unknown_var_dict = {'bcmod_route':[9],
                           'educatm':[0],
                           'educatv_m2':[0],
                           'kotelchuck':[9],
                           'racem':[0],
                           'racem_exp':[9],
                           'bc_attendant':[9],
                           'insurance_mom':[0]}

#Extract and parse full list of variables from STATE_DATA_documentation.xlsx
#All variables, including extranious variables, currently unused in analysis
#WE are interested in 3 dictionaries (key = variable name)
#         - type (categorical, continious,...)
#         - description
#         - values (dictionary key)
parsed_documentation = process_excel_variable_file(
    file_var_documentation,
    var_col="Variable", 
    desc_col="Description/Label", 
    type_col="Type",
    values_col='Values'
)

#These dictionaries control interaction with variables
#Extracting parsed documentation (All documentation stored in these 
#parsed dictionaries)
#E.g. Descriptions are stored in var_desc_dict
var_key_dict =  parsed_documentation['var_key_dict']
var_desc_dict = parsed_documentation['desc_dict']
var_type_dict = parsed_documentation['type_dict']

#Study specific variables/descriptions
study_vars_df = pd.read_excel(file_vars_use)
study_vars_all = study_vars_df['variable'] 

#NOTE: overwrites variable descriptions 
for var in study_vars_all:
    var_desc_dict[var] = study_vars_df.loc[study_vars_df['variable']==var,\
                                            'description']
    
#Use constructed variables with NA values for missing values, where appropriate
study_vars_all = [f"{var}_na"  if var in missing_unknown_var_dict.keys() else var \
        for var in study_vars_all] 

#Add recoded variables with 'np.nan' missing value coding
#  to each of the type, description, and values dictionaries
for var_without_na in missing_unknown_var_dict.keys():
    var_with_na = f"{var_without_na}_na"
    var_desc_dict[var_with_na] = var_desc_dict[var_without_na]
    var_type_dict[var_with_na] = var_type_dict[var_without_na]
    key_use = var_key_dict[var_without_na]
    key_use[np.nan] = 'Missing/Unknown'
    var_key_dict[var_with_na] = key_use