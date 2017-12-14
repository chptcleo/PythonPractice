'''
Created on Dec 14, 2017

@author: walchen
'''
from com.pattern.flyweight.flyweight import Flyweight


class ConcreteFlyweight(Flyweight):
    
    def __init__(self, intrinsic_state):
        self.__intrinsic_state = intrinsic_state
        print 'ConcreteFlyweight init with intrinsic state(', self.__intrinsic_state, ')'
        
    def operation(self, extrinsic_state):
        print 'ConcreteFlyweight operation with intrinsic state(', self.__intrinsic_state, ') and extrinsic state(', extrinsic_state, ')'
        
        
