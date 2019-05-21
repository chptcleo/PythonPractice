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

class PersonalException(Exception):
    
    def __init__(self, message, status):
        super().__init__(message, status)
        self.__message = message
        self.__status = status
            
if __name__ == '__main__':
    test_else()