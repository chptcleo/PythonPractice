'''
@author: Wallace Chen
'''
import pexpect
import sys

child = pexpect.spawn('ssh wallace@192.168.1.106')
fout = file('./log.txt', 'w')
child.logfile = fout
# child.logfile = sys.stdout
# child.expect('(?i)Are you sure you')
# child.sendline('yes')
child.expect('(?i)password:')
child.sendline('3035188')
child.expect('$')
child.sendline('ls /home')
child.expect('$')
print child.before
print child.after