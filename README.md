# Package cpq_tools

A collection of Python utilities, intended for California Perinatal/Maternal Quality Care Collaborative data processing and 

Tools simplify analysis processing tasks, and are designed to 

Code is currently in a draft, unreleased state.

All code released under the [MIT License](LICENSE). Code is provied for user conviencnece, with no guarentee is made regarding acuracy of results. ALl analaysis should be performed under the supervision of qualified personell.

Tools constructed with the assistance of generative AI tools, primarily ChatGPT-4.

[Example Package Usage](EXAMPLE.ipynb)

## Network





## Structure

cpq_tools - Python tools, intended for CPQCC/CMQCC data analysis tasks

[Data Preprocessing]

table_one() 

Generate table one values for publication preperation purposes

missingness_grid()

Generate crosstabulations of variable missingess


[Network Code]

compute_network_metrics()

Compute network metrics from individual records

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
<!-- 
```
package_path = 'path_to_zip_file.zip'
#Unzip (If exists, warn, but overwrite)
#Please Python code.

#Linux server enings
sed -i 's/\r//' ./unzip_cpq.sh

./unzip_cpq.sh -->