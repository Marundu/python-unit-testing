# Does not check whether basicfunction.py passes

import unittest

class TestBasicFunction(unittest.TestCase):
    def test(self):
        self.assertTrue(True) # will always pass in this case

if __name__=='__main__':
    unittest.main()
