'''
Created on Dec 14, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod


class Flyweight(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        print 'Flyweight init'

    @abstractmethod        
    def operation(self, extrinsic_state):
        pass
    
    
