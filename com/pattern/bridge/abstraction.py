'''
Created on Dec 6, 2017

@author: walchen
'''
class Abstraction(object):
    
    def __init__(self, implementor):
        print 'Abstraction init'
        self.__implementor = implementor
        
    def invoke_operate(self):
        print 'Abstraction invoke operate'
        self.__implementor.operate()
        
    