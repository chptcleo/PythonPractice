from com.pattern.builder.builder import Builder
from com.pattern.builder.product import Product

class ConcreteBuilder(Builder):
    
    def __init__(self):
        print('ConcreteBuilder init')
        self._product = Product()
    
    def build_part1(self):
        print('ConcreteBuilder build part1')
        self._product.components.append('component1')
        
    def build_part2(self):
        print('ConcreteBuilder build part2')
        self._product.components.append('component2')
        
    def get_result(self):
        print('ConcreteBuilder get result')
        return self._product
        