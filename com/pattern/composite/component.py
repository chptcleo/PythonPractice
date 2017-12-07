'''
Created on Dec 7, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Component(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        print 'Component init'
        
    @abstractmethod
    def add_component(self, component):
        print 'Component add component'
        pass
    
    @abstractmethod
    def remove_component(self, component):
        print 'Component remove component'
        pass
    
    @abstractmethod
    def get_child(self, index):
        print 'Component get child'
        pass
    
    @abstractmethod
    def operate(self):
        print 'Component operate'
        