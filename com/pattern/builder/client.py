from com.pattern.builder.concrete_builder import ConcreteBuilder
from com.pattern.builder.director import Director

if __name__ == '__main__':
    my_builder = ConcreteBuilder()
    my_director = Director(my_builder)
    my_director.construct()
    my_product = my_builder.get_result()
    print(my_product.components[0])