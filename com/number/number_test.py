import math
def test_input():
    x = input("x: ")
    y = input("y: ")
    z = x * y
    print 'x*y =', z
    
def calculate():
    x = 2
    y = 3
    z = pow(x, y)
    print 'pow(x, y) =', z
    a = 32.9
    print 'math.floor(a) =', math.floor(a)
    print 'math.ceil(a) =', math.ceil(a)

    
if __name__ == '__main__':
    test_input()
    calculate()
