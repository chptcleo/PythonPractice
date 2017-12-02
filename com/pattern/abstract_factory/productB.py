class ProductB:
    
    def __init__(self):
        print('ProductB init')
        
    def work(self):
        print('ProductB work')
        
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