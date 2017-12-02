'''
@author: Wallace Chen
'''
from subprocess import Popen, PIPE

def test_tidy():
    text = open('messy.html').read()
    tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    
    tidy.stdin.write(text)
    tidy.stdin.close()
    
    print tidy.stdout.read()

if __name__ == '__main__':
    test_tidy()