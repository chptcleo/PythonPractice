'''
Created on Dec 15, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Handler(object):
    
    __metaclass__ = ABCMeta
    
    
    def __init__(self):
        print 'Handler init'
        self.successor = None
        
    def set_successor(self, successor):
        print 'Handler set successor'
        self.successor = successor
        
    def get_successor(self):
        print 'get successor'
        return self.successor
    
    @abstractmethod
    def handle(self):
        pass
    
class ConcreteHandler(Handler):
    
#     def __init__(self):
#         print 'ConcreteHandler init'
#         self.successor = None
    
    def handle(self):
        print 'ConcreteHandler handle'
        if self.successor is None:
            print 'ConcreteHandler handle request here'
        else:
            self.successor.handle()
            
handler1 = ConcreteHandler()
handler2 = ConcreteHandler()
handler1.set_successor(handler2)
handler1.handle()