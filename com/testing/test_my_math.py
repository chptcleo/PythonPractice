'''
Created on Feb 16, 2016

@author: walchen
'''
import my_math, unittest
from subprocess import Popen, PIPE

class SquareTestCase(unittest.TestCase):
    
    def startUp(self):
        print 'startUp'
        unittest.TestCase.setUp(self)
    
    def test_integer(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                p = my_math.square(x, y)
                self.failUnless(p == x * y, 'test integer failed')
                
    def testFloat(self):
        for x in xrange(-10, 10):
            for y in xrange(-10, 10):
                x = x / 10.0
                y = y / 10.0
                p = my_math.square(x, y)
                self.failUnless(p == x * y, 'test float failed')
                
    def test_pylint(self):
        cmd = 'pylint', '-rn', 'my_math'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), '')
                
    def tearDown(self):
        print 'tearDown'
        unittest.TestCase.tearDown(self)
    
if __name__ == '__main__':
    unittest.main()
