from os import path

def get_file():
    location = path.dirname(path.abspath(__file__)) 
    with open(path.join(location, "raw.txt")) as f:
        return f.read() 