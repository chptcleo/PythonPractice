'''
Created on Dec 7, 2017

@author: walchen
'''
from com.pattern.composite.component import Component

class Composite(Component):
    
    def __init__(self):
        print 'Composite init'
        self.__components = []
        
    def add_component(self, component):
        print 'Composite add component'
        self.__components.append(component)
        
    def remove_component(self, component):
        print 'Composite remove component'
        self.__components.remove(component)
        
    def get_child(self, index):
        print 'Composite get child'
        return self.__components[index]
    
    def operate(self):
        print 'Composite operate'
        for component in self.__components:
            component.operate()