from os import path

location = path.dirname(path.abspath(__file__))
def get_file(): 
    with open(path.join(location, "raw.txt")) as f:
        return f.read()

def write_bin_to_file(encoded):
    with open(path.join(location, "out.bin"), 'wb') as f:
        f.write(encoded) 

def read_bin_from_file():
    with open(path.join(location, "out.bin"), 'rb') as f:
        return f.read() 