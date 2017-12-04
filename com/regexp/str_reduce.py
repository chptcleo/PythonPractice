'''
Created on Jun 7, 2017

@author: walchen
'''
import re

if __name__ == '__main__':
    
    result = '[omc@sprintlab364vm16 ~]$'
    pattern = r'\[|-bash'
    try:
        x = [m.start() for m in re.finditer(pattern,result)][-1]
    except Exception, e:
        x = -1
        
    print x
    print result[:x]
    for m in re.finditer(r'-bash|\[',result):
        print m.start()
        
#     print result.rfind('-bash')