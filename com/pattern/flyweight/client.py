'''
Created on Dec 14, 2017

@author: walchen
'''
from com.pattern.flyweight.flyweight_factory import FlyweightFactory

factory = FlyweightFactory()
flyweight = factory.get_flyweight('calm')
flyweight.operation('sing')
flyweight = factory.get_flyweight('angry')
flyweight.operation('fight')
flyweight = factory.get_flyweight('calm')
flyweight.operation('sing')
