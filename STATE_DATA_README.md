# STATE_DATA 

Files for analysis of infant and infant-transfer STATE_DATA files.

Processing and analysis code is open source. All PHI data storage, processing, and analysis is performed on secure servers. Results stored on 


# Project Files 

| File Name                  | Description |
|----------------------------|-------------|
| [`STATE_DATA_run.ipynb`](STATE_DATA_run.ipynb)  | Code to run all project files, including preparing the BATCH job scheduler. |
| [`STATE_DATA_preprocess.py`](STATE_DATA_preprocess.py) | Preprocessing code for hospital, geographic, and socidemographic variables from public datasets. |
| [`STATE_DATA_setup.py`](STATE_DATA_setup.py)      | Setup code for common variables and file paths. Usage: ```import STATE_DATA_setup as setup```|
| [`STATE_DATA_process.py`](STATE_DATA_process.py) | Processing code for individual state datasets. Processes INFANT and LONG datasets, and generates subsampled QUICK datasets. Generates a combined STATE_DATA dataset of all states, simplifying certain types of analysis. |
| [`STATE_DATA_analysis.py`](STATE_DATA_analysis.py)   | Analysis code for STATE_DATA datasets. Exploratory data analysis, including missing value analysis. |

# License

Code provide in a draft, unreleased state under the [MIT license](LICENSE).






