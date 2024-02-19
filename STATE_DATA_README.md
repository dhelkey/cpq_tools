# STATE_DATA Readme

STATE_DATA projectfFiles for processing and analysis of infant and infant-transfer data.

We provide processing and analysis code . All PHI data storage, processing, and analysis is performed on secure servers. 


## Project Files 

| File Name                  | Description |
|----------------------------|-------------|
| [`STATE_DATA_run.ipynb`](STATE_DATA_run.ipynb)  | Code to run all project files, including preparing the BATCH job scheduler. |
| [`STATE_DATA_preprocess.py`](STATE_DATA_preprocess.py) | Preprocessing code for hospital, geographic, and socidemographic variables from public datasets. |
| [`STATE_DATA_setup.py`](STATE_DATA_setup.py)      | Setup code for common variables and file paths. Usage: ```import STATE_DATA_setup as setup```|
| [`STATE_DATA_process.py`](STATE_DATA_process.py) | Processing code for individual state datasets. Processes INFANT and LONG datasets, and generates subsampled QUICK datasets. Generates a combined STATE_DATA dataset of all states, simplifying certain types of analysis. |
| [`STATE_DATA_analysis.py`](STATE_DATA_analysis.py)   | Analysis code for STATE_DATA datasets. Exploratory data analysis, including missing value analysis. |


## Dependancies

The primary languages used in the STATE_DATA project are: 

* SAS - Initial dataset processing and export

* Python - Dataset processing, analysis, visualization


### Python Packages

* NetworkX - Network construction & analysis

* Igraph - Network construction & analysis

* Numpy - Numerical tools

* Pandas - Data manipulation

* statsmodels - Statistical analysis

* matplotlib - Visualization tools

* Seaborn - Visualizaiton tools


### License

[License discussion](doc/license_info.md)





