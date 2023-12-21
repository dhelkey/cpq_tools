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
import sys
import os

package_dir_relative = 'cpq_tools/'
package_dir_full = os.path.abspath(package_dir_relative)
if package_dir_full not in sys.path:
    sys.path.append(package_dir_full)

# Import package
import cpq_tools as cpq
```
