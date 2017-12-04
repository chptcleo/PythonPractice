'''
Created on Mar 31, 2016

@author: walchen
'''
from xmlrpclib import ServerProxy

if __name__ == '__main__':
    proxy = ServerProxy('http://10.68.127.125:4242')
    print proxy.twice(2)