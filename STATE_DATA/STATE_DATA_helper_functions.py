"""
Python helper functions for STATE_DATA project 
"""



def process_state_data_infant(df_in):
    """
    Prepares STATE_DATA INFANT file for analysis
    Applied individually to each State for processing the cleaned dataset of infant data

    """
    df = df_in.copy()
    
    #Convert column names to lowercase
    df.columns = df_clean.columns.str.lower()

    #Convert all Missing/Unknown variables to "N/A" (np.nan)
    #Append "_m" (missing) to end of variable name
    for var_without_na, na_code_vec \
        in missing_unknown_variable_dict.items():
        var_with_na = f"{var_without_na}_m"
        df[var_with_na] = df[var_without_na]
        df.loc[df[var_without_na].isin(na_code_vec), 
               va_with_na] = np.nan
        
    return df

    #Construct date variables
    df['year_covid'] = 0
    df['year_aca'] = 0
    df.loc[df['year']==2020, 'year_covid'] = 1
    df.loc[df['year']>-2014, 'year_aca'] = 1

    #Hypertension (any)
    # Conditions and their values
    hyper_conditions = [ #First condition to evaluate "True" is selected
         ((df['sl_htnchr'] == 1) | (df['sl_htnges'] == 1)), #Hypertention indicated
        ((df['sl_htnchr'] == 0) | (df['sl_htnges'] == 0)),  #No hypertension indicated
    hyper_choices = [1, 0]
    df['hyper_any'] = np.select(hyper_conditions, hyper_choices, default=np.nan)


    #Identify infant survival
    

def process_state_data_long(df_in):
     """
     Process LONG
     """

