'''
Created on Dec 7, 2016

@author: walchen
'''
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser('argparse test')
    parser.add_argument('-x', '--xml')
    parser.add_argument('-e', '--ne', default='bsc')
    args = parser.parse_args()
    print 'The args: ', args
