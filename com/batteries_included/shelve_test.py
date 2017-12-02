'''
@author: Wallace Chen
'''
import shelve

def test_shelve():
    s = shelve.open('shelve.data', writeback=True)
    s['x'] = ['a','b','c']
    print s
    s['x'].append('d')
    print s
    s.close()

if __name__ == '__main__':
    test_shelve()
