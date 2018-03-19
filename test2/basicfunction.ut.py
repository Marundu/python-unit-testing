# $ python basicfunction.ut.py -v (verbose output)

import unittest
from basicfunction import BasicFunction

class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func=BasicFunction()    
    
    def test1(self):
        self.assertTrue(True)
    
    def test2(self):
        self.assertTrue(True)
    
    def test3(self):
        self.assertEqual(self.func.state, 0) # checks initialization of BasicFunction class

if __name__=='__main__':
    unittest.main()
