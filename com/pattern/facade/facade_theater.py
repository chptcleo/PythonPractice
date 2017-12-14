'''
Created on Dec 14, 2017

@author: walchen
'''
from com.pattern.facade.dvd_player import DVDPlayer
from com.pattern.facade.light import Light

class FacadeTheater():
    
    def __init__(self):
        print 'FacadeTheater init'
        self.__dvd_player = DVDPlayer()
        self.__light = Light()
        
    def start_play(self):
        print 'FacadeTheater start play'
        self.__light.turn_off()
        self.__dvd_player.turn_on()
        
    def stop_play(self):
        print 'FacadeTheater stop play'
        self.__light.turn_on()
        self.__dvd_player.turn_off()
        
