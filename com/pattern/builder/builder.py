from abc import ABCMeta, abstractmethod

class Builder:
    
    __metaclass = ABCMeta

    @abstractmethod        
    def build_part1(self):
        pass
       
    @abstractmethod 
    def build_part2(self):
        pass
        