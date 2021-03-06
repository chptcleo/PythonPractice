from com.pattern.factory_method.product import ConcreteProduct
class Creator:
    
    def __init__(self):
        print('Creator init')
    
    def create_product(self):
        print('Creator create product')
        
    def operate(self, product):
        print('Creator operate')
        product.work()
        
class ConcreteCreator(Creator):
    
    def __init__(self):
        print('ConcreteCreator init')
        
    def create_product(self):
        print('ConcreteCreator create product')
        return ConcreteProduct()