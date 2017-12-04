'''
Created on Mar 31, 2016

@author: walchen
'''
from SimpleXMLRPCServer import SimpleXMLRPCServer

def twice(x):
    return x*2

if __name__ == '__main__':
    server = SimpleXMLRPCServer(('', 4242))
    server.register_function(twice)
    server.serve_forever()