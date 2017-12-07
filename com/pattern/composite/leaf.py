'''
Created on Dec 7, 2017

@author: walchen
'''
from com.pattern.composite.component import Component

class Leaf(Component):
    
    def __init__(self):
        print 'Leaf init'
        
    def operate(self):
        print 'Leaf operate'
        
    def add_component(self, component):
        print 'Leaf add component'
    
    def remove_component(self, component):
        print 'Leaf remove component'
    
    def get_child(self, index):
        print 'Leaf get child'
