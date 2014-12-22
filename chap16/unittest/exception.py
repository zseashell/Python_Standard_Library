'''
Created on Dec 22, 2014

@author: cienet
'''
import unittest

def raise_error(*args, **kwds):
    raise ValueError('Invalid Value: ' + str(args) + str(kwds))

class ExceptionTest(unittest.TestCase):
    '''
    classdocs
    '''
    def testTrapLocally(self):
        try:
            raise_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')
            
    def testFailUnlessRaises(self):
        self.failUnlessRaises(ValueError, raise_error, 'a', b='c')


if __name__ == '__main__':
    unittest.main()
