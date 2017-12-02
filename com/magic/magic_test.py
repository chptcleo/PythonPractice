'''
@author: Wallace Chen
'''
__metaclass__ = type

class Bird:
    def __init__(self):
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print 'Eat eat eat...'
            self.hungry = False
        else:
            print 'No, thanks. I am full'
            
class SongBird(Bird):
    def __init__(self):
#         Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'Squawk'
    
    def sing(self):
        print self.sound
        
class Rectangle():
    
    def __init__(self):
        self.width = 0
        self.height = 0
    
    def set_size(self, size):
        self.width, self.height = size
        
    def get_size(self):
        return self.width, self.height
    
    size = property(get_size, set_size)
    
class Fibs:
    
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def next(self):
        self.a, self.b = self.b,self.a+self.b
        return self.a
    
    def __iter__(self):
        return self
    
def test_generator(num):
    for i in range(0, num):
        yield i
        
def test_yield_send(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

if __name__ == '__main__':
    sb = SongBird()
    sb.sing()
    sb.eat()
    sb.eat()
    
    rec = Rectangle()
    rec.width = 10
    rec.height = 5
    print rec.size

    fibs = Fibs()
    for i in fibs:
        if i>1000:
            print i
            break
        
    print list(test_generator(3))
    r = test_yield_send(5)
    print r.next()
    print r.send('really?')
    