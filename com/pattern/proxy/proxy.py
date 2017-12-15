'''
Created on Dec 15, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Subject(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def operation(self):
        pass
    
class RealSubject(Subject):
    
    def __init__(self):
        print 'RealSubject init'
        
    def operation(self):
        print 'RealSubject operation'
        
class Proxy(Subject):
    
    def __init__(self):
        print 'Proxy init'
        self.__rs = RealSubject()
        
    def operation(self):
        print 'Proxy operation'
        self.__rs.operation()
        
proxy = Proxy()
proxy.operation()