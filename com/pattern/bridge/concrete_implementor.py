'''
Created on Dec 6, 2017

@author: walchen
'''
from com.pattern.bridge.implementor import Implementor

class ConcreteImplementor(Implementor):
    
    def __init__(self):
        print 'ConcreteImplementor init'
        
    def operate(self):
        print 'ConcreteImplementor operate'