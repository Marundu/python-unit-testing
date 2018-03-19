# $ python basicfunction.ut.py -v (verbose output)

import unittest
from project.basicfunction import BasicFunction

class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func=BasicFunction()    
    
    def test1(self):
        self.assertTrue(True)
    
    def test2(self):
        self.assertTrue(True)
    
    def test3(self):
        self.assertEqual(self.func.state, 0) # checks initialization of BasicFunction class
    
    def test4(self):
        self.func.increment_state()
        self.assertEqual(self.func.state, 1)
    
    def test5(self):
        self.func.increment_state()
        self.func.increment_state()
        self.func.clear_state()
        self.assertEqual(self.func.state, 0)

if __name__=='__main__':
    unittest.main()
