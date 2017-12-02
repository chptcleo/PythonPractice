'''
@author: Wallace Chen
'''

def convert_test():
    items = [('name', 'wallace'), ('age', 32)]
    d = dict(items)
    print d
#     del d['age']
    print d
    print 'I am %(age)s' % d

if __name__ == '__main__':
    convert_test()
