import unittest
import sys
sys.path.append("../classes") # Adds higher directory to python modules path.

from calc import calc

class calc_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(self,10,5),15)
        self.assertEqual(calc.add(self,1,-1),0)
        self.assertEqual(calc.add(self,1,1),2)

    def test_add2(self):
        self.assertEqual(calc.add(self,10,5),15)
        self.assertEqual(calc.add(self,1,-1),0)
        self.assertEqual(calc.add(self,1,1),2)

if __name__=="__main__":
    unittest.main()