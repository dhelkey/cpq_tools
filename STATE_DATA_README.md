# STATE_DATA 

Files for analysis of infant and infant-transfer STATE_DATA files.

# Project Files 

| File Name                  | Description |
|----------------------------|-------------|
| [`STATE_DATA_setup.ipynb`](STATE_DATA_setup.ipynb)  | Code to run all files for this project, including preparing the BATCH job scheduler. |
| [`STATE_DATA_setup.py`](STATE_DATA_setup.py)      | Setup code, necessary for multiple states in the project. Includes documentation, common parameters, PHI data location, etc. Called automatically by the [`_processing.py`](STATE_DATA_processing.py) and [`_analysis.py`](STATE_DATA_analysis.py) scripts. |
| [`STATE_DATA_processing.py`](STATE_DATA_processing.py) | Processing code for individual state datasets. Processes INFANT and LONG datasets, and generates subsampled QUICK datasets. Generates a combined STATE_DATA dataset of all states, simplifying certain types of analysis. |
| [`STATE_DATA_analysis.py`](STATE_DATA_analysis.py)   | Analysis code for STATE_DATA datasets. Exploratory data analysis, including missing value analysis. |



