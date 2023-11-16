# Package cpq_tools

## Download updated code from Github

### Windows

```cmd
curl -L -o cpq_tools.zip https://github.com/dhelkey/cpq_tools/archive/refs/heads/main.zip
```

### Linux

```bash
wget -O cpq_tools-main.zip https://github.com/dhelkey/cpq_tools/archive/refs/heads/main.zip
```

## Import package using Python
```
import os
import sys
import shutil
import zipfile

def import_package_from_zip(zip_file_name, repo_name, remove_zip=False):
    # Construct the full path to the zip file
    zip_file_path = os.path.join(os.getcwd(), zip_file_name)
    print(f"Zip file path: {zip_file_path}")

    # Create a temporary directory for extraction
    temp_dir = os.path.join(os.getcwd(), "_TEMP")
    print(f"Temporary directory: {temp_dir}")

    # Construct the target directory for the extracted content
    target_dir = os.path.join(temp_dir, repo_name + "-main")
    print(f"Target directory: {target_dir}")

    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        print(f"Extracting zip file to {target_dir}")
        zip_ref.extractall(target_dir)

    # Construct the package directory path
    package_dir = os.path.join(target_dir, repo_name)
    print(f"Package directory: {package_dir}")

    # Append the package directory to the system path
    sys.path.append(package_dir)
    print(f"Package directory added to system path")

    # Remove the zip file if specified
    if remove_zip:
        print(f"Removing zip file: {zip_file_path}")
        os.remove(zip_file_path)

# Specify the repository name
repo_name = 'cpq_tools'
zip_file_name = f'{repo_name}-main.zip'

# Call the function to import the package from zip
import_package_from_zip(zip_file_name, repo_name, remove_zip=False)

# Import package
from cpq_tools import tableOne
```






# Package Usage


### `process_excel_variables` 

The `process_excel_variable_file` function processes Excel files (.xls or .xlsx) containing variable data. It outputs a pandas DataFrame detailing variable names, descriptions, and types, and a dictionary mapping variable names to their possible values.


```python
variable_description_df, variable_key_dict = process_excel_variable_file(
    'data/state_data_documentation.xlsx',
    var_col="Variable", 
    desc_col="Description/Label", 
    type_col="Type",
    values_col='Values'
)




EXAMPLES


import requests
from io import BytesIO
from zipfile import ZipFile

def download_github_repo_with_requests(repo_url, branch='main', target_dir='downloaded_repository'):
    url = f"{repo_url}/archive/refs/heads/{branch}.zip"
    response = requests.get(url)
    zipfile = ZipFile(BytesIO(response.content))
    zipfile.extractall(path=target_dir)

download_github_repo_with_requests('https://github.com/dhelkey/cpq_tools')



import wget

def download_github_repo_with_wget(repo_url, branch='main', target_file='downloaded_repository.zip'):
    url = f"{repo_url}/archive/refs/heads/{branch}.zip"
    wget.download(url, target_file)

download_github_repo_with_wget('https://github.com/dhelkey/cpq_tools')
