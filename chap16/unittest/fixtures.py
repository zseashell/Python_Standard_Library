'''
Created on Dec 22, 2014

@author: cienet
'''
import unittest

class FixturesTest(unittest.TestCase):
    '''
    classdocs
    '''

    def setUp(self):
        print 'in setup()...'
        self.fixture = range(1, 10)
        
    def tearDown(self):
        print 'in teardown()...'
        del self.fixture
        
    def test(self):
        print 'in test()...'
        self.failUnlessEqual(self.fixture, range(1, 10))
        
    
if __name__ == '__main__':
    unittest.main()

