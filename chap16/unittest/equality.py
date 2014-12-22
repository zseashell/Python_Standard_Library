'''
Created on Dec 22, 2014

@author: cienet
'''
import unittest

class EqualTest(unittest.TestCase):
    '''
    classdocs
    '''

    def testExpectEqual(self):
        self.failUnlessEqual(1, 3-2)
        
    def testExpectEqualFails(self):
        self.failUnlessEqual(2, 3-2)
        
    def testExpectNotEqual(self):
        self.failIfEqual(2, 3-2)

    def testExpectNotEqualFails(self):
        self.failIfEqual(1, 3-2)
        
if __name__ == '__main__':
    unittest.main()
