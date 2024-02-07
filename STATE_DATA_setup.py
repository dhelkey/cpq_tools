"""
Setup code and parameters for STATE_DATA 

Usage:
from STATE_DATA_setup import variable1, variable2 
-or-
import STAT_DATA_setup as setup

setup.variable1
setup.variable2

Requires:
    STATE_DATA_PRIVATE.py (NOT uploaded)

#TODO - Add tests (ensure data loads correctly with script changes)

"""

#Documentation of variables defined in this script
var_key_docstring = """
setup variables:

Parameters defined in PRIVATE file:
    phi_data_path - Location of PHI data - All intermediate data is saved here.
    state_infant_long_files  - Dictionary of STATE_DATA files
                        Two files per state:
                            INFANT - Infant birth records - One row per infant
                            LONG - Infant discharge records - One row per infant/stay
    file_var_documentation - Path to documentation file (excel)
    file_included_vars - Path to included variable table (excel)

Constructed by STATE_DATA_setup.py:

     - Panas dataframe of variable information (Parsed STATE_DATA_DOCUMENTATION_FILE)

    missing_unknown_var_dict - Variable values corrosponding to missing/unknown

#IMPORT CODE

"""



#Python imports
import pandas as pd

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
    
#Import parameters and settings from the PRIVATE file (not uploaded)
from STATE_DATA_PRIVATE import file_var_documentation, \
    file_included_vars, phi_data_path, state_infant_long_files

#Extract and parse full list of variables from STATE_DATA_DOCUMENTATION.xlsx
#All variables, including extranious variables, currently unused for analysis
#WE are interested in 3 dictionaries (key = variable name)
#         - type (categorical, continious,...)
#         - description
#         - values (dictionary key)
VARIABLE_INFO_DF, VARIABLE_KEY_DICT, \
      VARIABLE_DESC_DICT = process_excel_variable_file(
    STATE_DATA_DOCUMENTATION_FILE,
    var_col="Variable", 
    desc_col="Description/Label", 
    type_col="Type",
    values_col='Values'
)

#Read in list of included variables


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

#Add recoded missing values to each of the type, description, and values dictionaries


#Add variables names with 'np.nan' missing value coding to
#   VARIABLE_KEY_DICT, VARIABLE_DESC_DICT

#Parse list of variables included for analysis

#Create a processe 



#TODO - Verify we have descriptions and types for all variables, and keys for all categorical variables