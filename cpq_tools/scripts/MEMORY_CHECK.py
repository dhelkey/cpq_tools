#TO Run 
#python MEMORY_CHECK.py
import sys
import platform

# Function to get version of a module
def get_module_version(module_name):
    try:
        module = __import__(module_name)
        try:
            return module.__version__
        except AttributeError:
            return 'unknown version'
    except ImportError:
        return None

# Print Python version
print(f"Python Version: {platform.python_version()}")

# Print standard package versions
packages = ['numpy', 'sklearn', 'networkx', 'igraph']
for package in packages:
    version = get_module_version(package)
    if version:
        print(f"{package} Version: {version}")
    else:
        print(f"{package} is not installed.")

# Check if psutil is installed and retrieve memory information
psutil_version = get_module_version('psutil')
if psutil_version:
    import psutil
    memory = psutil.virtual_memory()
    used_memory = memory.used / (1024**3)  # Convert to GB
    available_memory = memory.available / (1024**3)  # Convert to GB

    # Print the memory status
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Available Memory: {available_memory:.2f} GB")
else:
    print("psutil is not installed, cannot retrieve memory information.")