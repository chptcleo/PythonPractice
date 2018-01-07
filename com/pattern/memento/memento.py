class Memento:
    
    def __init__(self, state):
        self.__state = state
        
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state
        
class Originator:
    
    def __init__(self):
        self.__state = None
        
    def create_memento(self):
        return Memento(self.__state)
    
    def restore_memento(self, memento):
        self.__state = memento.get_state()
        
    def get_state(self):
        return self.__state
    
    def set_state(self, state):
        self.__state = state
        
class Caretaker:
    
    def __init__(self):
        self.__memento = None
        
    def 
        
