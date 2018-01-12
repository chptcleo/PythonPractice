from abc import ABCMeta, abstractmethod

class State:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def process(self):
        pass
    
class OnState(State):
    
    def process(self):
        print 'Turn off'
        
class OffState(State):
    
    def process(self):
        print 'Turn on'
        
class Context():
    
    def __init__(self):
        self.__state = None
        
    def set_state(self, state):
        self.__state = state
        
    def operation(self):
        self.__state.process()
        
if __name__ == '__main__':
    
    context = Context()
    on_state = OnState()
    off_state = OffState()
    context.set_state(off_state)
    context.operation()
    context.set_state(on_state)
    context.operation()
    