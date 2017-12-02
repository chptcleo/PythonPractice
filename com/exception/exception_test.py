'''
@author: Wallace Chen
'''

def test_else():
    while True:
        try:
            x = input('Please input first number: ')
            y = input('Please input second number: ')
            z = x/y
            print 'x/y =', z
        except Exception, e:
            print e
            print 'Error occur, please retry'
        else:
            print 'Complete execution'
            break
        finally:
            print 'finally clause'
            
if __name__ == '__main__':
    test_else()