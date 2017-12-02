class Product:
    
    def __init__(self):
        print('Product init')
        
    def work(self):
        print('Product work')
        
class ConcreteProduct(Product):
    
    def __init__(self):
        print('ConcreteProduct init')
        
    def work(self):
        print('ConcreteProduct work')