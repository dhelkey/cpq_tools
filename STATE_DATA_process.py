"""
Process STATE_DATA, save overall STATE_DATA and individual [STATE]:
                    INFANT and LONG records
                        For the FULL dataset and subsampled QUICK dataset
                        
NOTE -The last part of this script (combining datasets)
         requires storing all datasets in MEMORY, and may cause RAM errors
    

OUTPUTS (PICKLE outputs - Stored in PHI data directory)
        [STATE]_[INFANT/LONG]_[FULL/QUICK].pkl
        STATE_DATA_[INFANT/LONG]_[FULL/QUICK].pkl

"""
import os
import numpy as np
import STATE_DATA_setup as setup

#Processing parameters
p_subsample = 0.05 #Percentage of data to subsample 

##Subsample Pandas dataframe (Note - Subsampling is more involved for LONG dataset

def state_data_process_infant(df_in):
    """
    Processing script to prepare STATE_DATA for analysis
    Applied individually to each State for processing INFANT data

    """
    df = df_in.copy()
    
    #Convert column names to lowercase
    df.columns = df_clean.columns.str.lower()

    #Convert all Missing/Unknown variables to "N/A" (np.nan)
    #Append "_m" (missing) to end of variable name
    for var_without_na, na_code_vec \
        in setup.missing_unknown_variable_dict.items():
        var_with_na = f"{var_without_na}_m"
        df[var_with_na] = df[var_without_na]
        df.loc[df[var_without_na].isin(na_code_vec), 
               va_with_na] = np.nan

    #Construct date variables

    #Identify infant survival

#Full data storage
        
# Creating the data_type_vec and data_length_vec as specified
data_type_vec = ['infant', 'long']
data_length_vec = ['full', 'quick']

 # Simplified dictionary initialization with comprehension
full_data_dict = {data_type: {data_length: [] for \
                data_length in data_length_vec} for \
                     data_type in data_type_vec}

for state, (file_infant, file_long) in STATE_DATA_FILES.items():

    file_dict = {'infant':file_infant, 'long':file_long}
    for data_type, file_use in file_dict.items():
        if data_type=='long':
            continue #Finalize INFANT processing code first
        file_path = setup.phi_data_path + file_use

        df_raw = read_csv_stata(file_path)
        df_raw['state'] = state

        df_processsed, df_subsampled = setup.process_state_data(df_raw)

        #Print rows, columns of df_raw vs df_processed

        #Print number of subsampled rows

        quick_dict = {'full':df_processsed,
                      'quick':df_subsampled}
        for data_length, df_save in quick_dict.items():
            state_save_file_name = f"{state}_{data_type}_{data_length}.pkl"
            state_save_file_path = os.path.join(setup.phi_data_path, 
                                           state_save_file_name)
            #Save dataset [state]_[data_type]_[full/small].pkl
            df_save.to_pickle(state_save_file_path)
            #Append data to list: [data_type]_[full/small] (all states)
            data_list[data_type][data_length].append(df_save)

#Export all-state STATE_DATA dataset
for data_type in data_type_vec:
            for data_length in data_length_vec:
                full_save_file_name = f"STATE_DATA_{data_type}_{data_length}.pkl"
                full_save_file_path = setup.phi_data_path
                full_out_df = pd.concat(data_list[data_type][data_length])
                full_out_df.to_pickle(full_out_df)

#Save full STATE_DATA datasets

        


    # file_clean = PHI_DATA_PATH + file_clean
    # file_long = PHI_DATA_PATH + file_long
# dat_clean_list = []
# dat_long_list = []

# out_file = PHI_DATA_PATH + 'STATE_DATA.pkl'

    # # Read the clean file
    # df_clean = pd.read_csv(file_clean) if file_clean.endswith('.csv') \
    #     else pd.read_stata(file_clean)
    # df_clean['state'] = state
    # df_clean.columns = df_clean.columns.str.lower()
    # dat_clean_list.append(df_clean)

    # # Read the long file
    # df_long = pd.read_csv(file_long) if file_long.endswith('.csv')\
    #         else pd.read_stata(file_long)
    # df_long['state'] = state
    # df_long.columns = df_long.columns.str.lower()
    # dat_long_list.append(df_long)
# 
    #Subsample datasets for quick analysis

    #Write out INFANT and LONG datasets for each state

# Concatenate the lists into DataFrames
# dat_clean = pd.concat(dat_clean_list)
# dat_long = pd.concat(dat_long_list)
# if quick:
#     dat_clean = dat_clean.sample(n=10000)


#

# dat_clean.to_pickle(out_file)

# dat_clean.state.value_counts()



#Import & process data by state

# INFANT & LONG datasets (First, process INFANT records, then process LONG records)
#Merge infant level records into the LONG dataset
#The LONG dataset will be used for network analysis


#Save each as seperate PKL (Python object) files




#Variable preperation & cleaning




#Prepare a 






#Prepare a subsampled version of the data







#