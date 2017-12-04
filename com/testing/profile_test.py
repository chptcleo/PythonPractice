'''
Created on Feb 19, 2016

@author: walchen
'''
import profile,pstats
from my_math import square

if __name__ == '__main__':
    profile.run('square(22,22)','my_math.profile')
    print pstats.Stats('my_math.profile')