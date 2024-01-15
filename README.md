# Package cpq_tools

A collection of Python utilities, intended for California Perinatal/Maternal Quality Care Collaborative use.

Tools simplify analysis processing tasks, and are designed to 

Code is currently in a draft, unreleased state.

All code released under the [MIT License](LICENSE). Code is provied for user conviencnece, with no guarentee is made regarding acuracy of results. ALl analaysis should be performed under the supervision of qualified personell.

Tools constructed with the assistance of generative AI tools, primarily ChatGPT-4.


##Structure

cpq_tools - Python tools, intended for CPQCC/CMQCC data analysis tasks

sni


[Data Preprocessing]

table_one() 

Generate table one values for research purposes


[Network Code]

network_metrics

## Design Philosophy
Functions are intended for analysis of processed, generally rectangular datasets, where each row represents a single observation. These datasets are typically stored with categorical variables recorded as integers, to simplify storage.



These functions are designe to prepare this data for presentation, incluing


# Using CPQ Tools Without Installation

This document explains how to use the `cpq_tools` package without installing it, by dynamically adding its path to the Python environment. 

'cpq_tools' may also be installed by manually downloading the ZIP file directly from GitHub and running the following code:

'''



## Method

Clone github repository
```
%%cmd #Run from Jupyter Notebook - Windows
git clone https://github.com/dhelkey/cpq_tools.git
```

```
cd cpq_tools
git pull
```

Add the following code at the beginning of your script:

   ```
import sys
import os

package_dir_relative = 'cpq_tools/'
package_dir_full = os.path.abspath(package_dir_relative)
if package_dir_full not in sys.path:
    sys.path.append(package_dir_full)

# Import package
import cpq_tools as cpq
```

```
package_path = 'path_to_zip_file.zip'
#Unzip (If exists, warn, but overwrite)
#Please Python code.
```
#Please, finish for this LASST bit please, along with descriptiion. E.g. replace this comment with tesxt)


Runing on server complicate

#Linux server enings
sed -i 's/\r//' ./unzip_cpq.sh

./unzip_cpq.sh