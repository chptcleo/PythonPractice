'''
@author: Wallace Chen
'''
import os

def read_file(file_location):
    with open(file_location, 'rb') as f:
        for line in f.readlines():
            print(line.strip())
            
def write_file(file_location):
    with open(file_location, 'a') as f:
        f.write('\nnew line')


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    file_location = os.path.join(current_dir, 'somefile.txt')
    read_file(file_location)
    write_file(file_location)