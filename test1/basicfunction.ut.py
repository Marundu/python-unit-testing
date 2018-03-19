# Does not check whether basicfunction.py passes
# $ python basicfunction.ut.py -v (verbose output)

import unittest

class TestBasicFunction(unittest.TestCase):
    def test1(self):
        self.assertTrue(True) # will always pass in this case
    
    def test2(self):
        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()
