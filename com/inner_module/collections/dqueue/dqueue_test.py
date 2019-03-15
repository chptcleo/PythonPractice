'''

@author: chenhuaping
'''
from collections import deque

if __name__ == '__main__':
    d = deque(['x','y','z'])
    d.appendleft('a')
    d.append('m')
    print(d)
    print(d.popleft())