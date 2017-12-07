'''
Created on Dec 6, 2017

@author: walchen
'''
from com.pattern.adapter.adaptee import Adaptee
from com.pattern.adapter.object_adapter import ObjectAdapter
from com.pattern.adapter.class_adapter import ClassAdapter

def invoke_target(target):
    target.operation()

adaptee = Adaptee()
object_adapter = ObjectAdapter(adaptee)
invoke_target(object_adapter)

class_adapter = ClassAdapter()
invoke_target(class_adapter)
