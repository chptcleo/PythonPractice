'''
Created on Dec 14, 2017

@author: walchen
'''
from com.pattern.flyweight.concrete_flyweight import ConcreteFlyweight


class FlyweightFactory():
    
    def __init__(self):
        print 'FlyweightFactory init'
        self.__flyweights = {}
        
    def get_flyweight(self, intrinsic_state):
        print 'FlyweightFactory get flyweight with intrinsic_state ', intrinsic_state
        if self.__flyweights.has_key(intrinsic_state) is False:
            self.__flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)
        return self.__flyweights[intrinsic_state]
