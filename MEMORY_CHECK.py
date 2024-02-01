import sys
import platform

# Print Python version
print(f"Python Version: {platform.python_version()}")

# Try to import the packages and print their versions
try:
    import numpy
    print(f"numpy Version: {numpy.__version__}")
except ImportError:
    print("numpy is not installed.")

try:
    import sklearn
    print(f"sklearn Version: {sklearn.__version__}")
except ImportError:
    print("sklearn is not installed.")

try:
    import networkx
    print(f"networkx Version: {networkx.__version__}")
except ImportError:
    print("networkx is not installed.")

try:
    import igraph
    print(f"igraph Version: {igraph.__version__}")
except ImportError:
    print("igraph is not installed.")

# Try to import psutil and print memory information
try:
    import psutil
    memory = psutil.virtual_memory()
    used_memory = memory.used / (1024**3)  # Convert to GB
    available_memory = memory.available / (1024**3)  # Convert to GB

    # Print the memory status
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Available Memory: {available_memory:.2f} GB")
except ImportError:
    print("psutil is not installed, cannot retrieve memory information.")

    #To RUn:
    #python MEMORY_CHECK.py