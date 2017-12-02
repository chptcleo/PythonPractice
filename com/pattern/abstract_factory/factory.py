from com.pattern.abstract_factory.productA import ProductA1, ProductA2
from com.pattern.abstract_factory.productB import ProductB1, ProductB2
class AbstractFactory:
    
    def __init__(self):
        print('AbstractFactory init')
    
    def create_productA(self):
        print('AbstractFactory create_productA')
        
    def create_productB(self):
        print('AbstractFactory create_productB')

class ConcreteFactory1(AbstractFactory):
    
    def __init__(self):
        print('ConcreteFactory1 init')
        
    def create_productA(self):
        print('ConcreteFactory1 create_productA')
        return ProductA1()
        
    def create_productB(self):
        print('ConcreteFactory1 create_productB')
        return ProductB1()
        
class ConcreteFactory2(AbstractFactory):
    
    def __init__(self):
        print('ConcreteFactory2 init')
        
    def create_productA(self):
        print('ConcreteFactory2 create_productA')
        return ProductA2()
        
    def create_productB(self):
        print('ConcreteFactory2 create_productB')
        return ProductB2()
