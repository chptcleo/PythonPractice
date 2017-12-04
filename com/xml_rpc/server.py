'''
Created on Apr 1, 2016

@author: walchen
'''
from urlparse import urlparse
from xmlrpclib import ServerProxy, Fault
from os.path import join, isfile, abspath
from SimpleXMLRPCServer import SimpleXMLRPCServer
import sys

SimpleXMLRPCServer.allow_reuse_address = 1

MAX_HISTORY_LENGTH = 6
UNHANDLED = 100
ACCESS_DENIED = 200

class UnhandledQuery(Fault):
    '''
    An exception that doesn't handled.
    '''
    def __init__(self, msg='Could not handle the exception'):
        Fault.__init__(self, UNHANDLED, msg)
        
class AccessDenied(Fault):
    '''
    An excetion raised when a user want to access file but doesn't have authority.
    '''
    def __init__(self, msg='Access denied'):
        Fault.__init__(self, ACCESS_DENIED, msg)

def inside(the_dir, name):
    '''
    Check the file is inside the directory.
    '''
    directory = abspath(the_dir)
    file_name = abspath(name)
    return file_name.startwith(join(directory, ' '))

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
        return 0
    
    def _handle(self, query):
        '''
        Handle queries
        '''
        the_dir = self.dirname
        name = join(the_dir, query)
        if not isfile(name):
            raise UnhandledQuery
        if not inside(the_dir, name):
            raise AccessDenied
        
        return open(name).read()
    
    def query(self, query, history=[]):
        '''
        Query for a file, return as a string.
        '''
        
        try:
            return self.__handle(query)
        except UnhandledQuery:
            history = history + [self.url]
            if len(history) > MAX_HISTORY_LENGTH:
                raise
            return self._broadcast(query, history)
        
    def fetch(self, query, secret):
        '''
        Get the file and write it.
        '''
        if secret != self.secret:
            raise AccessDenied
        result = self.query(query)
        f = open(join(self.dirname, query), 'w')
        f.write(result)
        f.close()
        return 0
            
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
                return s.query(query, history)
            except Fault, f:
                if f.faultCode == UnhandledQuery:
                    pass
                else:
                    self.known.remove(other)
            except:
                self.known.remove(other)
        raise UnhandledQuery
    
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
