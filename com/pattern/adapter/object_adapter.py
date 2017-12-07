'''
Created on Dec 6, 2017

@author: walchen
'''
from com.pattern.adapter.target import Target

class ObjectAdapter(Target):
    
    def __init__(self, adaptee):
        print 'ObjectAdapter init'
        self.__adaptee = adaptee
        
    def operation(self):
        print 'ObjectAdapter operation'
        self.__adaptee.special_operation()
    