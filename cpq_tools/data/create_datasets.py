#Create sample datasets to demonstrate methods
import pandas as pd
import numpy as np
import random

# Sample dataset with detailed individual-level data
SAMPLE_INFANT_DATA = pd.DataFrame({
    'RacialCategory': [1, 2, 4, 4, 2, 1, 2, 3, 1, 2, 1, 3, 
                      4, 1, 1, 1, 4, 1, 3, 2, 1, 3, 1, 2, 
                      4, 3, 2, 4, 2, 3, 1, 2, 1, 3, 2, 1],
    'HispanicLatino': [0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 
                       1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
    'Sex': [0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 
            1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
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
    'RacialCategory': {1: 'NH Black', 2: 'Hispanic',
                        3: 'NH White',  4: 'AANHPI'},
    'HispanicLatino': {0: 'Not Hispanic or Latino',
                    1: 'Hispanic or Latino'},
    'Sex': {0: 'Female', 1: 'Male'}
}

#Define sample network data (transfer level)
#Unweighted
network_data_raw = {
    'more_central': [
        (1, 2),
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 7),
        (4, 5),
        (5, 8),
        (6, 5),
        (7, 5), 
        (8, 5)
    ],
    'less_central': [
        (1, 2),
        (2, 3),
        (2, 1),
        (3, 6),
        (4, 7),
        (5, 1),
        (7, 8), 
        (5, 2),
        (6, 5),
        (8, 6)    
    ],
    'more_dense': [
        (1, 2),
        (2, 3),
        (2, 1),
        (2, 6),
        (3, 6),
        (4, 5),
        (4, 7),
        (5, 1), 
        (5, 2),
        (7, 5),
        (7, 8),
        (6, 5),
        (8, 5),
        (8, 6)    
    ],
    'less_dense': [
        (1, 4),
        (1, 4),
        (2, 1),
        (2, 1),
        (3, 2),
        (3, 2),
        (4, 5),
        (5, 8),
        (5, 4),
        (5, 4),
        (6, 5),
        (6, 5),
        (7, 8), 
        (7, 8),
        (8, 5)    
    ], 
    'more_efficient': [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6),
        (6, 7), (7, 8), (8, 1), (1, 3), (2, 4),
        (3, 5), (4, 6), (5, 7), (6, 8), (7, 1)
    ],
    'less_efficient': [
        (1, 2), (1, 2), (2, 3), (2, 3), (3, 4),
        (3, 4), (4, 5), (4, 5), (5, 6), (5, 6),
        (6, 7), (6, 7), (7, 8), (7, 8), (8, 1)
    ],
     'more_modular': [
        (1, 2),
        (2, 1),
        (2, 5),
        (3, 6),
        (4, 7),
        (5, 1),
        (7, 8), 
        (5, 2),
        (6, 5),
        (8, 4)    
    ],
    'less_modular': [
        (1, 4),
        (2, 3),
        (2, 1),
        (3, 6),
        (4, 7),
        (5, 1),
        (7, 8), 
        (5, 2),
        (6, 5),
        (8, 6)    
    ],
 
}

# Converting each list of tuples in the dictionary to a DataFrame
SAMPLE_NETWORK_DATA = {key: pd.DataFrame(value,
                         columns=['from_hosp', 'to_hosp']) \
                 for key, value in network_data_raw.items()}



