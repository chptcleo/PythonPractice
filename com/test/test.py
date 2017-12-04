'''
Created on May 20, 2016

@author: walchen
'''

if __name__ == '__main__':
    a_list = ['a', 'b', 'c']
    b_list = ['a', 'b']
    if [x for x in b_list if x not in a_list]:
        print 'no'
    else:
        c='xyz'
        print 'yes'
    print c
    s = '/var/lib/jenkins/jobs/SAT_Nightly_BSC_AOM/builds/148/robot-plugin/NeVe-TA_output.xml'
    l = s.split('/')
    print l[5], l[7], l[9]
        