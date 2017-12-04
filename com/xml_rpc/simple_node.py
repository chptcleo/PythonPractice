'''
Created on Apr 1, 2016

@author: walchen
'''
from urlparse import urlparse
from xmlrpclib import ServerProxy
from os.path import join, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys

MAX_HISTORY_LENGTH = 6
OK = 1
FAIL = 2
EMPTY = ' '

def get_port(url):
    '''
    get the port from url
    '''
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])


class Node:
    '''
    peer-to-peer node in the network
    '''
    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()
        
    def hello(self, other):
        '''
        Introduce one node to other
        '''
        self.known.add(other)
        return OK
    
    def _handle(self, query):
        '''
        Handle queries
        '''
        the_dir = self.dirname
        name = join(the_dir, query)
        if not isfile(name):
            return FAIL, EMPTY
        return OK, open(name).read() 
    
    def query(self, query, history=[]):
        '''
        Query for a file, return as a string.
        '''
        code, data = self._handle(query)
        if code == OK:
            return code, data
        else:
            history = history + [self.url]
            if len(history) > MAX_HISTORY_LENGTH:
                return FAIL, EMPTY
            return self._broadcast(query, history)
        
    def fetch(self, query, secret):
        '''
        Get the file and write it.
        '''
        if secret != self.secret:
            return FAIL
        code, data = self.query(query)
        if code == OK:
            f = open(join(self.dirname, query), 'w')
            f.write(data)
            f.close()
            return OK
        else:
            return FAIL
            
    def _broadcast(self, query, history):
        '''
        Broadcast a query to all nodes
        '''
        for other in self.known.copy():
            print '_broadcast loop'
            if other in history:
                print 'other in history'
                continue
            try:
                s = ServerProxy(other)
                code, data = s.query(query, history)
                if code == OK:
                    return code, data
            except:
                self.known.remove(other)
        
        return FAIL, EMPTY
    
    def _start(self):
        '''
        start xml-rpc server
        '''
        s = SimpleXMLRPCServer(('', get_port(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()
        
def main():
    '''
    Launch the program.
    '''
    url, directory, secret = sys.argv[1:]
    node = Node(url, directory, secret)
    node._start()
        
if __name__ == '__main__':
    main()
