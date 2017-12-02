'''
@author: Wallace Chen
'''
from math import pi
from string import Template

def test_float():
    my_format = 'The value of pi is: %f'
    print my_format % pi, ' the end.'
    
def test_template():
    my_format = Template('A $name should not $action.')
    d = {}
    d['name'] = 'gentleman'
    d['action'] = 'show his socks'
    print my_format.substitute(d)

def test_width():
    my_format = 'My favorite player is %.4s'
    players = 'kobejameswade'
    print my_format % players
    
def test_join():
    dirs = '', 'opt', 'c4c', 'bin'
    sep = '/'
    print sep.join(dirs)
    
    

if __name__ == '__main__':
    test_float()
    test_template()
    test_width()
    test_join()