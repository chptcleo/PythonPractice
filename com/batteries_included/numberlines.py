'''
@author: Wallace Chen
'''

import fileinput

def modify():
    for line in fileinput.input(inplace=1):
        line = line.rstrip()
        num = fileinput.lineno()
        print '%-40s # %2i' % (line, num)

if __name__ == '__main__':
    modify()
