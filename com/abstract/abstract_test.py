'''
@author: Wallace Chen
'''
__metaclass__ = type
class Secretive:
    def __inaccessible(self):
        print 'Can\'t accessible'
        
    def accessible(self):
        print 'Can accessible'
        
class A:
    def __init__(self):
        self.name = None
        
    def get_name(self):
        return self.name
    
    def set_name(self, value):
        self.name = value
    
    def hello(self):
        print "I am A"
        
class B:
    def hello(self):
        print "I am B"
        
class C(B, A):
    def hello(self):
        print 'I am C'

def test_doc():
    'This is test_doc function'
    print 'hello'
    
def change_list(w_list):
    '''
    This is change_list function
    '''
    w_list[0] = ['kobe', 'james']
    
def with_stars(**kwds):
    print kwds['name'], 'is', kwds['age']

def without_start(kwds):
    print kwds['name'], 'is', kwds['age']

def multipler(factor):
    def multiply_by_factor(number):
        return factor * number
    return multiply_by_factor

if __name__ == '__main__':
    print test_doc.__doc__
    help(test_doc)
    c_list = ['wallace', 'wade']
    change_list(c_list)
    print c_list
    help(change_list)
    info = {'name':'wallace','age':'32'}
    with_stars(name='wallace', age='32')
    with_stars(**info)
    without_start(info)
    x = multipler(2)
    print x(3)
    print multipler(3)(8)
    o = Secretive()
    print type(o)
    print o.__class__
    o.accessible()
    o._Secretive__inaccessible()
    c = C()
    c.hello()
    a = A()
    a.set_name('new_A')
    print a.name
    print getattr(a, 'name')
    setattr(a, 'age', '32')
    print a.age
    a1 = A()
    print getattr(a1, 'name')
