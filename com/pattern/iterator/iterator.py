'''
Created on Dec 22, 2017

@author: walchen
'''

from abc import ABCMeta, abstractmethod


class Aggregate:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create_iterator(self):
        pass

    
class ConcreteAggregate(Aggregate):
    
    def __init__(self):
        print 'ConcreteAggregate init'
        self.__objs = ['pig', 'dog', 'bird', 'duck']
        
    def create_iterator(self):
        print 'ConcreteAggregate create iterator'
        return ConcreteIterator(self)
    
    def get_element(self, index):
        print 'ConcreteAggreate get element by index', index
        if index < len(self.__objs):
            return self.__objs[index]
        else:
            return None
        
    def size(self):
        print 'ConcreteAggregate size'
        return len(self.__objs)

    
class Iterator:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def next(self):
        pass
    
    @abstractmethod
    def first(self):
        pass
    
    @abstractmethod
    def is_done(self):
        pass
    
    @abstractmethod
    def current_item(self):
        pass

    
class ConcreteIterator(Iterator):
    
    def __init__(self, concrete_aggregate):
        print 'ConcreteIterator init'
        self.__concrete_aggregate = concrete_aggregate
        self.__index = 0
        self.__size = concrete_aggregate.size()
    
    def first(self):
        print 'ConcreteIterator first'
        self.__index = 0
        
    def next(self):
        print 'ConcreteIterator next'
        if self.__index < self.__size:
            self.__index = self.__index + 1
        
    def is_done(self):
        print 'ConcreteIterator is done'
        return self.__index >= self.__size
    
    def current_item(self):
        print 'ConcreteIterator current item'
        return self.__concrete_aggregate.get_element(self.__index)
    
aggregate = ConcreteAggregate()
iterator = ConcreteIterator(aggregate)
while iterator.is_done() is False:
    print iterator.current_item()
    iterator.next()