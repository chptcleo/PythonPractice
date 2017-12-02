from com.pattern.abstract_factory.factory import ConcreteFactory1, ConcreteFactory2

if __name__ == '__main__':
    factory1 = ConcreteFactory1()
    productA1 = factory1.create_productA()
    productA1.work()
    productB1 = factory1.create_productB()
    productB1.work()
    
    factory2 = ConcreteFactory2()
    productA2 = factory2.create_productA()
    productA2.work()
    productB2 = factory2.create_productB()
    productB2.work()
