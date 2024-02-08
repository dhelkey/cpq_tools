#Python functions for generating BASH code
from .helper_funs import wF
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


def write_bsub(job_name, code_file):
    """Generate and write bsub code; returns terminal prompt
    Uses generate_bsub_code and wF to generate the full bsub code
    Saves .sh to file
    """

    bsub_code = generate_bsub_code(code_file, 
        job_name = job_name)

    outfile = f"{job_name}.sh"

    #Write .sh file
    wF(outfile, bsub_code)

    out_command = f"bsub < {outfile}"
    out = {'out_command':out_command, 
           'bsub_code':bsub_code}
    return(out)


