'''
Created on Dec 14, 2017

@author: walchen
'''
from com.pattern.flyweight.flyweight import Flyweight


class ConcreteCompositeFlyweight(Flyweight):
    
    def __init__(self):
        print 'ConcreteCompositeFlyweight init'
        self.__flyweights = []
        
    def add(self, flyweight):
        print 'ConcreteCompositeFlyweight add ', flyweight
        self.__flyweights.append(flyweight)
        
    def operation(self, extrinsic_state):
        print 'ConcreteCompositeFlyweight operation'
        for flyweight in self.__flyweights:
            flyweight.operation(extrinsic_state)
        
