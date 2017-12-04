'''
Created on Dec 4, 2017

@author: walchen
'''
class Singleton(object):
    
    __instance = None
    
    def __new__(cls, *args, **kw):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kw)
        return Singleton.__instance
    
a = Singleton()
b = Singleton()
print a == b
            
