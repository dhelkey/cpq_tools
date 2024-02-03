
#Functions for reading and writing files
def wF(outfile, file_contents):
    """Write file_contents to outfile"""
    with open(outfile, 'w') as f:
        f.write(file_contents)

def rF(infile):
    """Read infile contents"""
    with open(infile,'r') as f:
        return f.read()