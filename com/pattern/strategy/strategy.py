from abc import ABCMeta, abstractmethod

class Strategy:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def process(self):
        pass
    
class ConcreteStrategyA(Strategy):
    
    def process(self):
        print 'ConcreteStrategyA process'
        
class ConcreteStrategyB(Strategy):
    
    def process(self):
        print 'ConcreteStrategyB process'
        
class Context:
    
    def __init__(self):
        self.__strategy = None
        
    def set_strategy(self, strategy):
        self.__strategy = strategy
    
    def operation(self):
        self.__strategy.process()
        
if __name__ == '__main__':
    
    context = Context()
    strategya = ConcreteStrategyA()
    strategyb = ConcreteStrategyB()
    
    context.set_strategy(strategya)
    context.operation()
    context.set_strategy(strategyb)
    context.operation()
