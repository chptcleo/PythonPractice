'''
Created on Dec 6, 2017

@author: walchen
'''
from abc import ABCMeta, abstractmethod

class Target(object):

    __metaclass__ = ABCMeta
    
    def __init__(self):
        print 'Target init'

    @abstractmethod
    def operation(self):
        print 'abstractmethod Target operation'
        pass