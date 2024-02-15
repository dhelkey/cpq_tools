"""
Process STATE_DATA, save overall STATE_DATA and individual [STATE]:
                    INFANT and LONG records
                        For the FULL dataset and subsampled QUICK dataset

NOTE -The last part of this script (combining datasets)
         requires storing all datasets in MEMORY, and may cause RAM errors without sufficient memory.
         Larger dataserts may require keeping states seperate.
    

OUTPUTS (PICKLE outputs - Stored in PHI data directory)
        [STATE]_[INFANT/LONG]_[FULL/QUICK].pkl
        STATE_DATA_[INFANT/LONG]_[FULL/QUICK].pkl

"""
import os
import numpy as np
from cpq_tools import ComputeInfo
from STATE_DATA_setup import phi_data_path, \
    missing_unknown_variable_dict, state_infant_long_files
# import STATE_DATA_setup as setup

compute_info = computeInfo()

#Processing parameters
p_subsample = 0.05 #Percentage of data to subsample for quick=True datasets

##Subsample Pandas dataframe df 
#NOTE- Subsampling is more involved for LONG dataset

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


#Full data storage
data_type_vec = ['infant', 'long']
data_length_vec = ['full', 'quick']

full_data_dict = {data_type: {data_length: [] for \
                data_length in data_length_vec} for \
                     data_type in data_type_vec}

for state, (file_infant, file_long) in state_infant_long_files.items():

    compute_info.info()
    file_dict = {'infant':file_infant, 'long':file_long}
    for data_type, file_use in file_dict.items():
        if data_type=='long':
            continue #Finalize INFANT processing code before reading in LONG code
        file_path = phi_data_path + file_use

        df_raw = read_csv_stata(file_path)
        df_raw['state'] = state

        df_processsed = process_state_data_infant(df_raw)
        #Print rows, columns of df_raw vs df_processed
        print('raw', df_raw.shape,'processed', df_processed.shape)
        #Print number of subsampled rows

        # Calculate the number of rows to sample
        n_samples = int(len(df_processsed) * p_subsample)
        # Subsample the DataFrame
        df_subsampled = df.sample(n=n_samples)
        print('sampled', df_subsampled.shape)

        quick_dict = {'full':df_processsed,
                      'quick':df_subsampled}
        for data_length, df_save in quick_dict.items():
            state_save_file_name = f"{state}_{data_type}_{data_length}.pkl"
            state_save_file_path = os.path.join(phi_data_path, 
                                           state_save_file_name)
            #Save dataset [state]_[data_type]_[full/small].pkl
            df_save.to_pickle(state_save_file_path)
            #Append data to list: [data_type]_[full/small] (all states)
            data_list[data_type][data_length].append(df_save)

#Export all-state STATE_DATA dataset
for data_type in data_type_vec:
            for data_length in data_length_vec:
                full_save_file_name = f"STATE_DATA_{data_type}_{data_length}.pkl"
                full_save_file_path = os.path.join(phi_data_path,
                                                   full_save_file_name)
                #Combine Pandas dataframes
                full_out_df = pd.concat(data_list[data_type][data_length], axis=1)
                full_out_df.to_pickle(full_save_file_path)

compute_info.info()
print('Data parsed')