from collections import namedtuple

if __name__ == '__main__':
    
    Circle = namedtuple('Circle', ('x', 'y', 'z'))
    c = Circle(3, 4, 8)
    print('point: %d,%d, r: %d' % (c.x, c.y, c.z))
