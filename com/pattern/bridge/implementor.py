'''
Created on Dec 6, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Implementor(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        print 'Implementor init'
        
    @abstractmethod
    def operate(self):
        print 'Implementor operate'
        pass
