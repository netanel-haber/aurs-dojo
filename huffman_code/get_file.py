from os import path

location = path.dirname(path.abspath(__file__))
def get_file(): 
    with open(path.join(location, "raw.html")) as f:
        return f.read() 