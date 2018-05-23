'''
Created on May 8, 2018

@author: walchen
'''
import subprocess


def execute():
    res = subprocess.Popen(["ip" "add"], stdout=subprocess.PIPE).communicate()[0]
    print res

if __name__ == '__main__':
    execute()
