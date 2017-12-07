'''
Created on Dec 6, 2017

@author: walchen
'''
from com.pattern.bridge.concrete_implementor import ConcreteImplementor
from com.pattern.bridge.abstraction import Abstraction

implementor = ConcreteImplementor()
abstraction = Abstraction(implementor)
abstraction.invoke_operate()