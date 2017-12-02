class ProductA:
    
    def __init__(self):
        print('ProductA init')
        
    def work(self):
        print('ProductA work')
        
class ProductA1(ProductA):
    
    def __init__(self):
        print('ProductA1 init')
        
    def work(self):
        print('ProductA1 work')

class ProductA2(ProductA):
    
    def __init__(self):
        print('ProductA2 init')
        
    def work(self):
        print('ProductA2 work')   

if __name__ == '__main__':
    a1 = ProductA1()
    a1.work()