'''
Created on Dec 7, 2017

@author: walchen
'''
from com.pattern.composite.composite import Composite
from com.pattern.composite.leaf import Leaf

composite = Composite()
leaf1 = Leaf()
leaf2 = Leaf()
composite.add_component(leaf1)
composite.add_component(leaf2)

composite.operate()