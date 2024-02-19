
from IPython.display import display, Markdown

#Functions for writing, reading, and displaying files
def wF(outfile, file_contents):
    """Write file_contents to outfile"""
    with open(outfile, 'w') as f:
        f.write(file_contents)

def rF(infile):
    """Read infile contents"""
    with open(infile,'r') as f:
        return f.read()
    
def dF(infile):
    """Display File using Markdown"""
    display(Markdown(infile))
    

import psutil
import time
class computeInfo:
    def __init__(self):
        self.start_time = time.time()
        self.initial_memory = psutil.Process().memory_info().rss / (1024 ** 2)  # Memory in MB
        self.last_memory = self.initial_memory

    def info(self):
        """Prints the elapsed time in H:M:S, current memory usage, and memory usage change since last call."""
        current_time = time.time()
        current_memory = psutil.Process().memory_info().rss / (1024 ** 2)  # Memory in MB
        elapsed_time = current_time - self.start_time
        memory_change = current_memory - self.last_memory
        total_memory_change = current_memory - self.initial_memory

        # Calculate H:M:S from elapsed_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Elapsed Time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
        print(f"Current Memory Usage: {current_memory:.2f} MB")
        print(f"Memory Change Since Last Call: {memory_change:.2f} MB")
        print(f"Total Memory Change Since Instantiation: {total_memory_change:.2f} MB")

        # Update last memory usage for the next call
        self.last_memory = current_memory

# # Example usage
# compute_info = ComputeInfo() 
# compute_info.info() #Display initial compute info
# .....
# code here
# .....
# compute_info.info()  # Display compute info
