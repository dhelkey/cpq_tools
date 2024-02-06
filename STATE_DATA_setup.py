"""
Setup code for STATE_DATA


Define variables  for analysis

Requires:
    STATE_DATA_PRIVATE.py (NOT uploaded) - 

    XXX - Contains the PHI data path
    XXX -  dictionarythe state datafile names
"""
#Python imports
import os
import sys
import pandas as pd
import numpy as np

from STATE_DATA_PRIVATE import STATE_DATA_DOCUMENTATION_FILE, \
    STATE_DATA_FILES, PHI_DATA_PATH

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


#Included study variables