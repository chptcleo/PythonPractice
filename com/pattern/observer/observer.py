'''
Created on Jan 10, 2018

@author: walchen
'''
from abc import ABCMeta, abstractmethod
from com.abstract.abstract_test import __metaclass__

class Subject:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def add_observer(self):
        pass
    
    @abstractmethod
    def remove_observer(self):
        pass
    
    @abstractmethod
    def notify(self):
        pass
    
class ConcreteSubject(Subject):
    
    def __init__(self):
        self.__observers = []
        
    def add_observer(self, observer):
        self.__observers.append(observer)
        
    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.remove(observer)
            
    def notify(self):
        for observer in self.__observers:
            observer.update()
            
class Observer:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(self):
        pass
    
class ConcreteObserver(Observer):
    
    def __init__(self, subject):
        subject.add_observer(self)
    
    def update(self):
        print 'ConcreteObserver update'
        
if __name__ == '__main__':
    
    subject = ConcreteSubject()
    observer1 = ConcreteObserver(subject)
    observer2 = ConcreteObserver(subject)
    
    subject.notify()