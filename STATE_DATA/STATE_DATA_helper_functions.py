"""
Python helper functions for STATE_DATA project 
"""
import numpy as np
import pandas as pd
def read_csv_stata(file_path):
    """Helper function to ientify and read in CSV or STATA data file
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.dta'):
        return pd.read_stata(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a '.csv' or '.dta' file.")


def process_state_data_infant(df_in,
    missing_unknown_variable_dict=None):
    """
    Prepares STATE_DATA INFANT file for analysis
    Applied individually to each State for processing the cleaned dataset of infant data

    """
    df = df_in.copy()
    
    #Convert column names to lowercase
    df.columns = df.columns.str.lower()

    #Convert all Missing/Unknown variables to "N/A" (np.nan)
    #Append "_m" (missing) to end of variable name
    for var_without_na, na_code_vec \
        in missing_unknown_variable_dict.items():
        if var_without_na in df.columns():
            var_with_na = f"{var_without_na}_m"
            df[var_with_na] = df[var_without_na]
            df.loc[df[var_without_na].isin(na_code_vec), \
                var_with_na] = np.nan
        
    #Construct date variables
    df['birthyear_covid'] = 0
    df['birthyear_aca'] = 0
    df.loc[df['birthyear']==2020, 'birthyear_covid'] = 1
    df.loc[df['birthyear']>-2014, 'birthyear_aca'] = 1

    #Hypertension (any)
    # Conditions and their values
    hyper_conditions = [ #First condition to evaluate "True" is selected
         ((df['sl_htnchr'] == 1) | (df['sl_htnges'] == 1)), #Hypertention indicated
        ((df['sl_htnchr'] == 0) | (df['sl_htnges'] == 0)) ] #No hypertension indicated
    hyper_choices = [1, 0]
    df['hyper_any'] = np.select(hyper_conditions, hyper_choices, default=np.nan)

    #Infant survival

    return df

def process_state_data_long(df_in):
    """
     Process LONG
    """
    pass
