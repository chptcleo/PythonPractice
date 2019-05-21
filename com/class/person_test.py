'''
Created on 2019年5月21日

@author: chenhuaping
'''

class Person(object):
    
    def __init__(self, name):
        self.__name = name
    
    def action(self):
        print('%s take action' % self.__name)

class Hunter(Person):
    
    def __init__(self, hunter_name):
        super().__init__(hunter_name)
        self.__hunter_name = hunter_name
    
    def shoot(self):
        super().action()
        print('%s is shooting' % self.__hunter_name)

if __name__ == '__main__':
    h = Hunter('bale')
    h.shoot()