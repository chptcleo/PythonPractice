'''
Created on Dec 20, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Receiver:
    
    def __init__(self):
        print 'Receiver init'
        
    def operation(self):
        print 'Receiver operation'
        
class Command:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def execute(self):
        pass
    
class ConcreteCommand(Command):
    
    def __init__(self, receiver):
        print 'ConcreteCommand init'
        self.__receiver = receiver
        
    def execute(self):
        print 'ConcreteCommand execute'
        self.__receiver.operation()
        
class Invoker:
    
    def __init__(self, command):
        print 'Invoker init'
        self.__command = command
        
    def invoke(self):
        print 'Invoker invoke'
        self.__command.execute()
        
class Client:
    
    def __init__(self):
        print 'Client init'
        self.__receiver = Receiver()
        self.__command = ConcreteCommand(self.__receiver)
        self.__invoker = Invoker(self.__command)
        
    def operation(self):
        print 'Client operation'
        self.__invoker.invoke()
        
client = Client()
client.operation()