'''
Created on Dec 6, 2017

@author: walchen
'''
from com.pattern.adapter.target import Target
from com.pattern.adapter.adaptee import Adaptee

class ClassAdapter(Target, Adaptee):
    
    def __init__(self):
        print 'ClassAdapter init'
    
    def operation(self):
        print 'ClassAdapter operation'
        Adaptee.special_operation(self)