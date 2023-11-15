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

```python
import zipfile
import os
import sys
import shutil

def import_package_from_zip(zip_file_name, repo_name, remove_zip=False):
    zip_file_path = os.path.join(os.getcwd(), zip_file_name)
    temp_dir = os.path.join(os.getcwd(), "_TEMP")
    target_dir = os.path.join(temp_dir, repo_name + "-main")

    os.makedirs(target_dir, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

    package_dir = os.path.join(target_dir, repo_name)
    sys.path.append(package_dir)

    if remove_zip:
        os.remove(zip_file_path)

repo_name = 'cpq_tools'
zip_file_name = f'{repo_name}.zip'
import_package_from_zip(zip_file_name, repo_name, remove_zip=False)
```


This is a change