'''
@author: Wallace Chen
'''
from abc import ABCMeta, abstractmethod

class Component(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        print 'Component init'
        
    @abstractmethod
    def operation(self):
        print 'Component operation'
        pass
    
class ConcreteComponent(Component):
    
    def __init__(self):
        print 'ConcreteComponent init'
        
    def operation(self):
        print 'ConcreteComponent operation'
        
class Decorator(Component):
    
    def __init__(self, component):
        print 'Decorator init'
        self.__component = component
        
    def operation(self):
        print 'Decorator operation'
        self.__component.operation()
        
class ConcreteDecoratorA(Decorator):
    
    def __init__(self, component):
        self.__component = component
        print 'ConcreteDecoratorA init'
        
    def operation(self):
        print 'ConcreteDecoratorA operation'
        self.__component.operation()
        self.additional_operation()
        
    def additional_operation(self):
        print 'ConcreteDecoratorA additional operation'
        
class ConcreteDecoratorB(Decorator):
    
    def __init__(self, component):
        self.__component = component
        print 'ConcreteDecoratorB init'
        
    def operation(self):
        print 'ConcreteDecoratorB operation'
        self.__component.operation()
        self.additional_operation()
        
    def additional_operation(self):
        print 'ConcreteDecoratorB additional operation'
        
if __name__ == '__main__':
    a_concrete_component = ConcreteComponent()
    a_concrete_decorator = ConcreteDecoratorA(a_concrete_component)
    a_concrete_decorator = ConcreteDecoratorB(a_concrete_decorator)
    a_concrete_decorator.operation()
    
        
        
        
        
        