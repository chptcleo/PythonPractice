'''
@author: Wallace Chen
'''
def test_set():
    a = set([1, 2, 2, 3])
    print a
    b = set([2, 3, 4])
    print a.union(b)
    print a | b
    print a & b
    c = a.intersection(b)
    print c
    print c.issuperset(a)
    print c > a
    print b > a
    print a.difference(b)
    print a.symmetric_difference(b)
    print a ^ b

if __name__ == '__main__':
    test_set()
