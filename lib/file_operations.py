import os

def create(filename, content=None):
    with open(filename, 'a') as f:
        if content:
            f.write(content)
        os.utime(filename, None)
        
    return 0
