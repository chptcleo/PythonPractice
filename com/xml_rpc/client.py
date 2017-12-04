from xmlrpclib import ServerProxy, Fault
from threading import Thread
from cmd import Cmd
from random import choice
from string import lowercase
from server import Node, UNHANDLED
from time import sleep
import sys

HEAD_START = 0.1
SECRET_LENGTH = 100

def randomString(length):
    '''
    Return a random string with specified length.
    '''
    chars = []
    letters = lowercase[:26]
    while length > 0:
        length -= 1
        chars.append(choice(letters))
    return ''.join(chars)

class Client(Cmd):
    '''
    A text-based client interface.
    '''
    prompt = '>'
    
    def __init__(self, url, dirname, urlfile):
        '''
        Initialize the node and start the Node server in a seperate thread.
        '''
        Cmd.__init__(self)
        self.secret = randomString(SECRET_LENGTH)
        n = Node(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            self.server.hello(line.strip())

    def do_fetch(self, arg):
        '''
        Fetch the specified file.
        '''
        try:
            self.server.fetch(arg, self.secret)
        except Fault, f:
            if f.faultCode !=UNHANDLED:
                raise
            print 'Could not find ', arg
            
    def do_exit(self, arg):
        '''
        Exit the program
        '''
        print 
        sys.exit()
        
    do_EOF = do_exit

def main():
    urlfile, directory, url = sys.argv[1:]
    client = Client(url, directory, urlfile)
    client.cmdloop()

if __name__ == '__main__':
    main()
