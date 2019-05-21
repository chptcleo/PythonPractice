'''
Created on 2019年5月21日

@author: chenhuaping
'''
import unittest


class MyTestCase(unittest.TestCase):
    '''
    classdocs
    '''

    def __init__(self, *args, **kw):
        print('__init__')
        unittest.TestCase.__init__(self, *args, **kw)
        
    def startUp(self):
        print('startUp')
        
    def tearDown(self):
        print('tearDown')
        
    def test_first(self):
        print('test_first')
        self.assertEqual(1, 2, '1!=2')

        
if __name__ == '__main__':
    unittest.main()
        
