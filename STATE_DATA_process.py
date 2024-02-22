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
import pandas as pd
from cpq_tools import computeInfo
from STATE_DATA_setup import phi_data_path, \
     state_infant_long_files, missing_unknown_var_dict
from STATE_DATA import process_state_data_infant, \
            process_state_data_long, read_csv_stata
# import STATE_DATA_setup as setup

compute_info = computeInfo()
compute_info.info()


#Processing parameters
p_subsample = 0.05 #Percentage of data to subsample for quick=True datasets

##Subsample Pandas dataframe df 
#NOTE- Subsampling is more involved for LONG dataset

#Full data storage
data_type_vec = ['infant', 'long']
data_length_vec = ['full', 'quick']

full_data_dict = {data_type: {data_length: [] for \
                data_length in data_length_vec} for \
                     data_type in data_type_vec}

for state, (file_infant, file_long) in state_infant_long_files.items():
    print(state)
    
    file_dict = {'infant':file_infant, 'long':file_long}
    for data_type, file_use in file_dict.items():
        if data_type=='long':
            continue #Finalize INFANT processing code before reading in LONG code
        file_path = os.path.join(phi_data_path, file_use)

        df_raw = read_csv_stata(file_path)
        
        df_processed = process_state_data_infant(df_raw, state=state,
            missing_unknown_variable_dict = missing_unknown_var_dict)
        #Print rows, columns of df_raw vs df_processed
        print('raw', df_raw.shape,'processed', df_processed.shape)
        #Print number of subsampled rows

        # Calculate the number of rows to sample
        n_samples = int(len(df_processed) * p_subsample)
        # Subsample the DataFrame
        df_subsampled = df_processed.sample(n=n_samples)
        print('sampled', df_subsampled.shape)

        quick_dict = {'full':df_processed,
                      'quick':df_subsampled}
        for data_length, df_save in quick_dict.items():
            state_save_file_name = f"{state}_{data_type}_{data_length}.pkl"
            state_save_file_path = os.path.join(phi_data_path, 
                                           state_save_file_name)
            #Save dataset [state]_[data_type]_[full/small].pkl
            df_save.to_pickle(state_save_file_path)

            #To save memory, remove the next part of the code
            #and delete quick_dict, and df_processed

            #Append data to list: [data_type]_[full/small] (all states)
            full_data_dict[data_type][data_length].append(df_save)

        compute_info.info() #Compute info after INFANT and LONG data imported

#Export all-state STATE_DATA dataset
for data_type in data_type_vec:
            for data_length in data_length_vec:
                full_save_file_name = f"STATE_DATA_{data_type}_{data_length}.pkl"
                full_save_file_path = os.path.join(phi_data_path,
                                                   full_save_file_name)
                #Combine Pandas dataframes
                full_out_list = full_data_dict[data_type][data_length]
                if full_out_list:
                    full_out_df = pd.concat(full_out_list, axis=0)
                    full_out_df.to_pickle(full_save_file_path)
                else:
                    full_out_df = None
                    

compute_info.info()
print('Data parsed')