'''
Created on Apr 5, 2016

@author: walchen
'''
from xmlrpclib import ServerProxy

def send_request():
    mypeer = ServerProxy('http://localhost:4242')
    code, data = mypeer.query('test.txt')
    print code
    print data
    
    otherpeer = ServerProxy('http://localhost:4243')
    code, data = otherpeer.query('test.txt')
    print code
    print data
    
    mypeer.hello('http://localhost:4243')
    code, data = mypeer.query('test.txt')
    print code
    print data
    
    mypeer.fetch('test.txt', 'secret1')

if __name__ == '__main__':
    send_request()