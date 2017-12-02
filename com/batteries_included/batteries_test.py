'''
@author: Wallace Chen
'''
from com.batteries_included import hello2
import copy
import os

if __name__ == '__main__':
    hello2.say_hello()
    print dir(copy)
    print dir(copy.__all__)
    help(copy.copy)
    print copy.copy.__doc__
    print copy.__file__
    print os.environ['PYTHONPATH']
    print os.sep
    print os.pathsep
    os.system(r'C:\"Program Files\Google\Chrome\Application\chrome.exe')
    
