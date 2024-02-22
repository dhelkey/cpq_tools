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


def generate_bsub_code(py_file, job_name="my_python_job", 
                        output_file="job_output.%J",
                          error_file="job_error.%J",
                          py_version='3.8'):
    """
    Generates a batch script for submitting a Python script to an LSF job scheduler

    Args:
        py_file (str): The name of the Python file to run.
        job_name (str): The name of the LSF job. Default is "my_python_job".
        output_file (str): The name of the job output file. Default is "job_output.%J".
        error_file (str): The name of the job error file. Default is "job_error.%J".

    Returns:
        str: A batch script as a string.

    Example:
        print(generate_bsub_code('pytest.py', 'data_analysis', 'analysis_out.%J', 'analysis_err.%J'))
    """
    batch_script = f"""#!/bin/bash
#BSUB -J {job_name} # LSF Job Name
#BSUB -o {output_file} # Name of the job output file
#BSUB -e {error_file} # Name of the job error file
#BSUB -u dhelkey@stanford.edu
#BSUB -B #Start notification
#BSUB -N #END notification

module unload python
module load python/{py_version}
python --version
python $HOME/{py_file}
"""
    return batch_script

# Example usage:
# print(generate_batch_code('generate_bsub_code.py'))

# def write_bsub(job_name, code_file, out_folder = 'bsub_files'):
#     """Generate and write bsub code; returns terminal prompt
#     Uses generate_bsub_code and wF to generate the full bsub code
#     Saves .sh to file
#     """

#     bsub_code = generate_bsub_code(code_file, 
#         job_name = job_name)

#     outfile = f"{job_name}.sh"

#     #Write .sh file
#     wF(outfile, bsub_code)

#     out_command = f"bsub < {outfile}"
#     out = {'out_command':out_command, 
#            'bsub_code':bsub_code}
#     return(out)


# ##TODO combine the above file...
# def project_bsub(project, project_files = None, verbose = False):
#     """Batch processing with BSUB;
#     Generate BATCH job scheduler .sh files and bsub call for running each part of the project"""
#     #Define dictionary of project files

#     code_file = 'out_dir/' + project_files[project]
#     bsub_code = generate_bsub_code(code_file, 
#         job_name = job_name)
#     outfile = f"{job_name}.sh"
#     out_command = f"bsub < {outfile}"
#     bsub_data = write_bsub(project, code_file)
#     if verbose:
#         print(bsub_data['bsub_code'])
#     return(bsub_data['out_command'])

def process_state_data_infant(df_in,
                              state=None,
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
        if var_without_na in df.columns:
            var_with_na = f"{var_without_na}_m"
            df[var_with_na] = df[var_without_na]
            df.loc[df[var_without_na].isin(na_code_vec), \
                var_with_na] = np.nan
        
    df['state'] = state

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
