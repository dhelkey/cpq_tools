"""
Setup code for STATE_DATA


Define global variables

STATE_DATA_PRIVATE.py - 

    XXX - Contains the PHI data path
    XXX -  dictionarythe state datafile names
"""
#Python imports
import os
import sys
import pandas as pd
import numpy as np

from STATE_DATA_PRIVATE import STATE_DATA_DOCUMENTATION_FILE, \
    PHI_DATA_PATH #XXX


#Parameters & Settings


#Extract and parse full list of variables from STATE_DATA_DOCUMENTATION.xlsx
VARIABLE_DF, VARIABLE_KEY_DICT, \
      VARIABLE_DESC_DICT = process_excel_variable_file(
    STATE_DATA_DOCUMENTATION_FILE,
    var_col="Variable", 
    desc_col="Description/Label", 
    type_col="Type",
    values_col='Values'
)
variable_key_dict


#Included study variables