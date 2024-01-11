#Create sample datasets for use within this package
#Manually specified DataFrames to demonstrate and test methods

import pandas as pd
import numpy as np

# Sample dataset with detailed individual-level data
SAMPLE_INFANT_DATA = pd.DataFrame({
    'RacialCategory': [1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1, 3, 
                      2, 1, 3, 1, 2, 1, 3, 2, 1, 3, 1, 2, 
                      1, 3, 2, 1, 2, 3, 1, 2, 1, 3, 2, 1],
    'HispanicLatino': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    'Sex': [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
})

# Sample dataset with detailed individual-level data
SAMPLE_INFANT_DATA_NA = pd.DataFrame({
    'RacialCategory': [1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 1, 3, 
                      2, np.nan, 3, 1, 2, 1, np.nan, 2, 1, 3, 1, 2, 
                      1, 3, 2, 1, 2, 3, 1, 2, 1, 3, 2, 1],
    'HispanicLatino': [0, 0, np.nan, 0, 1, 0, 0, 1, 0, 1, 1, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    'Sex': [0, 1, np.nan, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            1, 0, 1, 0, 1, np.nan, 0, 1, 1, 0, 1, 0]
})

SAMPLE_VARIABLE_KEY_DICT = {
    'RacialCategory': {1: 'American Indian/Alaska Native', 2: 'Asian', 3: 'Black or African American'},
    'HispanicLatino': {0: 'Not Hispanic or Latino', 1: 'Hispanic or Latino'},
    'Sex': {0: 'Female', 1: 'Male'}
}