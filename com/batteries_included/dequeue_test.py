'''
@author: Wallace Chen
'''
from collections import deque

def test_dequeue():
    d = deque(range(1,6))
    print d
    d.append(0)
    d.append(6)
    print d
    d.pop()
    print d
    d.appendleft(9)
    print d
    d.rotate(2)
    print d
    d.rotate(-1)
    print d
    
test_dequeue()