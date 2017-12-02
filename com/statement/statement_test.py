'''
@author: Wallace Chen
'''
from math import sqrt

def test_else():
    for n in range(99, 81, -1):
        root = sqrt(n)
        if root == int(root):
            print n
            break
    else:
        print 'Didn\'t found it.' 

def test_exec():
    scope = {}
    exec 'sqrt = 1' in scope
    exec 'print \'hello, baby\''
    print scope['sqrt']
    print sqrt(9)
    
def test_eval():
    print eval('2*3')
    
if __name__ == '__main__':
    test_else()
    test_exec()
    test_eval()
