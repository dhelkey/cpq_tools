"""
Setup code and parameters for STATE_DATA 

Usage:
from STATE_DATA_setup import variable1, variable2 

Requires:
    STATE_DATA_PRIVATE.py (NOT uploaded)

#TODO - Add tests (ensure data loads correctly with script changes)

"""
#Imports
import pandas as pd
from cpq_tools import process_excel_variable_file

#Import parameters and settings from the PRIVATE file (not uploaded)
# from STATE_DATA_PRIVATE import phi_data_path, state_infant_long_files

from STATE_DATA_PRIVATE import phi_data_path, \
    state_infant_long_files, file_var_documentation, file_vars_use

#Documentation of variables defined in this script

#Define helper functions
def read_csv_stata(file_path):
    """Helper function to ientify and read in CSV or STATA data file
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.dta'):
        return pd.read_stata(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a '.csv' or '.dta' file.")
    
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

#Extracting parsed documentation (All documentation stored in these 
#parsed dictionaries)
var_key_dict =  parsed_documentation['var_key_dict']
var_desc_dict = parsed_documentation['desc_dict']
var_type_dict = parsed_documentation['type_dict']

state_data_vars_dat = pd.read_excel(file_vars_use)

#Read STATE_DATA_vars_use.xlsx 
#Overwrite any variable descriptions 
#Frome this, ADD the variable names (constructed=1) to var_disc_dict
#Right now, we are focusing on var_desc_dic
#Variables with missing values encoded (We use all lowercase variable names)
missing_unknown_var_dict = {'bcmod_route':[9],
                           'educatm':[0],
                           'educatv_m2':[0],
                           'kotelchuck':[9],
                           'racem':[0],
                           'racem_exp':[9],
                           'bc_attendant':[9],
                           'insurance_mom':[0]}
    #Identifying Missing Values
    #Constructs [variable]_m for variables with missing value codes
    #Replaces variable specific missing value codes (0,9,...)
    # with np.nan "."
    # This can simplify analysis in certain situations
    # E.g. Missing value reports, consistant regression handling
    # NOTE -  Caution needed when using for regression.
    #  1. Statistical functions may drop NA values
    # 2. Default comparison category may change for categorical variables


#TODO Here is the main todo
#Add recoded missing values to each of the type, description, and values dictionaries


#Add variables names with 'np.nan' missing value coding to
#   VARIABLE_KEY_DICT, VARIABLE_DESC_DICT

#Parse list of variables included for analysis
#Read in list of included variables #(Name, description, constructed, type (just for constructed))
#Add in unincluded variables to the dictinaries (type, descrition, (no categorical variables constructed?))

#Create a processe 



#TODO - Verify we have descriptions and types for all variables, and keys for all categorical variables