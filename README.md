# Package cpq_tools

A collection of Python utilities, intended for California Perinatal/Maternal Quality Care Collaborative use.

Code is currently in a draft, unreleased state.



All code is released under the [MIT License](LICENSE)


## Function API

table_one()


network_metrics


# Using CPQ Tools Without Installation

This document explains how to use the `cpq_tools` package without installing it, by dynamically adding its path to the Python environment.

## Method


Clone github repository
```
%%cmd #Run from Jupyter Notebook - Windows
git clone https://github.com/dhelkey/cpq_tools.git
```

Add the following code at the beginning of your script:

   ```
   python
   import sys
   import os

   # Set the path to the package
   package_dir = 'cpq_tools/'
   if package_dir not in sys.path:
       sys.path.append(package_dir)

   # Import the package
   import cpq_tools as cpq

   # Alternatively, import specific functions directly
   # from cpq_tools import tableOne
   # from cpq_tools.data_functions import process_excel_variable_file
```
