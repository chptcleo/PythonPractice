'''
@author: Wallace Chen
'''
import heapq
from random import shuffle

def test_heap():
    l = range(0,10)
    print l
    shuffle(l)
    print l
    h = []
    for i in l:
        heapq.heappush(h, i)
    print h
    heapq.heappush(h, 0.5)
    print h
    print heapq.heappop(h)
    print heapq.heappop(h)
    print heapq.heappop(h)
    print h

if __name__ == '__main__':
    test_heap()