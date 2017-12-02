from abc import ABCMeta, abstractmethod

class Parent:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def work(self):
        pass
    
class Son(Parent):
    
    def work(self):
        print 'Son work'
    
    def speak(self, words):
        print 'Son speak:', words
        
person = Son()
person.work()
person.speak('Hello World')
# person = Parent()
# person.work()