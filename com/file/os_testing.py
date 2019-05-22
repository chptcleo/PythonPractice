import os


def list_dir(dir_location):
    print(os.listdir(dir_location))
    
def list_flac(dir_location):
    print([x for x in os.listdir(dir_location) if os.path.splitext(x)[1] == '.flac'])
    
def list_dirs(dir_location):
    print([x for x in os.listdir(dir_location) if os.path.isdir(x)])
    
def list_files(dir_location):
    print([x for x in os.listdir(dir_location) if os.path.isfile(x)])

if __name__ == "__main__":
    curdir = os.path.dirname(__file__)
    list_dir(curdir)
    list_flac(curdir)
    list_dirs(curdir)
    list_files(curdir)