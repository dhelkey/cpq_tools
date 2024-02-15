# Package cpq_tools

A collection of Python utilities, intended for use by California Perinatal/Maternal Quality Care Collaborative statisticians for data processing and analysis tasks.

No PHI data or any actual infant level ata is include.

ALl code released into the [public domain] (UNLICENSE) in a draft state, for user conviencnece. All analysis using these tools should be performed under the supervision of qualified personell.

Tools constructed with the assistance of generative AI tools, primarily ChatGPT-4.

## STATE_DATA

[STATE_DATA package usage](STATE_DATA_README.md)

## Network

[Network](NETWORK_EXAMPLE.ipynb)

## cpq_tools

Python tools, intended for CPQCC/CMQCC data analysis tasks

[Data Preprocessing]

table_one() 

Generate table one values for publication preperation purposes

missingness_grid()

Generate crosstabulations of variable missingess


[Network Code]

compute_network_metrics()

Compute network metrics from individual records

[Example Package Usage](EXAMPLE.ipynb)


# Using CPQ Tools Without Installation

'cpq_tools' may also be installed by manually downloading the ZIP file directly from GitHub and dynamically adding its path to the Python environment by running the following code:

Clone github repository
```
%%cmd 
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
