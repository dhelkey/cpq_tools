#Python functions for generating BASH code

def generate_bsub_code(py_file, job_name="my_python_job", 
                        output_file="job_output.%J",
                          error_file="job_error.%J",
                          py_version='3.8'):
    """
    Generates a batch script for submitting a Python script to an LSF job scheduler,
    with Python 3.8 module loaded.

    Args:
        py_file (str): The name of the Python file to run.
        job_name (str): The name of the LSF job. Default is "my_python_job".
        output_file (str): The name of the job output file. Default is "job_output.%J".
        error_file (str): The name of the job error file. Default is "job_error.%J".

        
##TODO - add code to request memory, in the BSUB string

    Returns:
        str: A batch script as a string.

    Example:
        print(generate_batch_code('pytest.py', 'data_analysis', 'analysis_out.%J', 'analysis_err.%J'))

    GPT-4 "Code Wizard" - 20230201
    """
    batch_script = f"""#!/bin/bash
#BSUB -J {job_name} # LSF Job Name
#BSUB -o {output_file} # Name of the job output file
#BSUB -e {error_file} # Name of the job error file
module unload python
module load python/{py_version}
python --version
python $HOME/{py_file}
"""
    return batch_script

# Example usage:
# print(generate_batch_code('pytest.py'))

