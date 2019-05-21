'''

@author: chenhuaping
'''


class Car(object):
    
    __name = None
    __loss = None
    
    def __init__(self, name, loss):
        self.__name = name
        self.__loss = loss
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__losss[0]
    
    def get_loss(self):
        return self.__loss[1] * self.__loss[2]


if __name__ == '__main__':
    lexus = Car('300h', [35, 5000, 10])
    print(getattr(lexus, '_Car__name'))
    print(dir(lexus))
