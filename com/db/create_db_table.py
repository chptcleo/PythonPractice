'''
Created on Nov 21, 2015

@author: walchen
'''
import sqlite3

if __name__ == '__main__':
    print 'Start creating sqlite tables'
    connection = sqlite3.connect('coachdata.sqlite')