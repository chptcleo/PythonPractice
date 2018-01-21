from abc import ABCMeta, abstractmethod

class Node:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def accept(self, visitor):
        pass
    
class Visitor:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def visit(self, node):
        pass

class NodeA(Node):
    
    def accept(self, visitor):
        visitor.visit(self)
        
    def operation(self):
        print 'NodeA operation'
        
class NodeB(Node):
    
    def accept(self, visitor):
        visitor.visit(self)

    def operation(self):
        print 'NodeB operation'
        
class VisitorA(Visitor):
    
    def visit(self, node):
        node.operation()
        
class VisitorB(Visitor):
    
    def visit(self, node):
        node.operation()
        
class ObjectStructure:
    
    def __init__(self):
        self.nodes = []
        
    def add_node(self, node):
        self.nodes.append(node)
        
    def process(self, visitor):
        for node in self.nodes:
            node.accept(visitor)
            
if __name__ == '__main__':
    
    os = ObjectStructure()
    node_a = NodeA()
    node_b = NodeB()
    os.add_node(node_a)
    os.add_node(node_b)
    visitor_a = VisitorA()
    os.process(visitor_a)
    visitor_b = VisitorB()
    os.process(visitor_b)