from com.pattern.factory_method.creator import Creator, ConcreteCreator
if __name__ == '__main__':
    concrete_creator = ConcreteCreator()
    concrete_product = concrete_creator.create_product()
    creator = Creator()
    creator.operate(concrete_product)

    
    