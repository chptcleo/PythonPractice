'''
@author: Administrator
'''
from io import StringIO

def write_io():
    string_io = StringIO()
    string_io.write('hello')
    string_io.write(' ')
    string_io.write('world')
    print(string_io.getvalue())
    
    
def read_io():
    string_io = StringIO('what is up')
    while True:
        s = string_io.read()
        if s == '':
            break
        print(s.strip())

if __name__ == '__main__':
    write_io()
    read_io()