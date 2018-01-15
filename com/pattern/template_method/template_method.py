from abc import ABCMeta, abstractmethod

class AbstractClass:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def step1(self):
        pass
    
    @abstractmethod
    def step2(self):
        pass
    
    def step3(self):
        print 'AbstractClass step3'
        
    def operation(self):
        self.step1()
        self.step2()
        self.step3()
        
class SubClass(AbstractClass):
    
    def step1(self):
        print 'SubClass step1'
        
    def step2(self):
        print 'SubClass step2'
        
if __name__ == '__main__':
    
    actor = SubClass()
    actor.operation()
        
    