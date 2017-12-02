from abc import ABCMeta, abstractmethod

class ProductB:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def work(self):
        pass
        
class ProductB1(ProductB):
    
    def __init__(self):
        print('ProductB1 init')
        
    def work(self):
        print('ProductB1 work')

class ProductB2(ProductB):
    
    def __init__(self):
        print('ProductB2 init')
        
    def work(self):
        print('ProductB2 work')   

if __name__ == '__main__':
    a1 = ProductB1()
    a1.work()