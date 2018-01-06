from abc import ABCMeta, abstractmethod

class Mediator:
    
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, msg):
        pass
    
class Colleague:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def send(self, msg):
        pass
    
    @abstractmethod
    def notify(self, msg):
        pass
    
class ConcreteColleague(Colleague):
    
    def __init__(self, name, mediator):
        self.__name = name
        self.__mediator = mediator
        
    def send(self, msg):
        self.__mediator.process(msg, self)
        
    def notify(self, msg):
        print self.__name, 'get info:', msg
        
class ConcreteMediator(Mediator):
    
    colleague1 = None
    colleague2 = None
        
    def process(self, msg, colleague):
        if self.colleague1 == colleague:
            self.colleague2.notify(msg)
        else:
            self.colleague1.notify(msg)
            
if __name__ == '__main__':
    un = ConcreteMediator()
    usa = ConcreteColleague('USA', un)
    iraq = ConcreteColleague('IRAQ', un)
    un.colleague1 = usa
    un.colleague2 = iraq
    
    usa.send('Do not produce nuclear')
    iraq.send('I do not have nuclear')
    
        
        