'''
Created on Dec 22, 2014

@author: cienet
'''
import unittest

class OutPutsTest(unittest.TestCase):
    '''
    classdocs
    '''
    def testPass(self):
        return
    
    def testFail(self):
        self.failIf(True, 'failure message goes here!')
        
    def testError(self):
        raise RuntimeError('Test error!')
    
if __name__ == '__main__':
    unittest.main()
