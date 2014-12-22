'''
Created on Dec 22, 2014

@author: cienet
'''
import unittest

class TruthTest(unittest.TestCase):
    '''
    classdocs
    '''
    def testFailIf(self):
        self.failIf(False)

    def testFailUnless(self):
        self.failUnless(True)
        
    def testAssertTrue(self):
        self.assertTrue(True)
        
    def testAssertFalse(self):
        self.assertFalse(False)
        
if __name__ == '__main__':
    unittest.main()