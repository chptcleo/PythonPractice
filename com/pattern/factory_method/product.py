from abc import ABCMeta, abstractmethod

class Product:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod        
    def work(self):
        pass
        
class ConcreteProduct(Product):
    
    def __init__(self):
        print('ConcreteProduct init')
        
    def work(self):
        print('ConcreteProduct work')