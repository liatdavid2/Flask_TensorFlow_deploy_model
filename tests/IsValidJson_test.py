import unittest
import sys
sys.path.append("../classes") # Adds higher directory to python modules path.
from IsValidJson import IsValidJson 
from unittest.mock import Mock

class IsValidJson_test(unittest.TestCase):

    def test_postIris_whenIrisIsValid_receiveOk(self):
        res,status_code = IsValidJson.check({"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4,"petal_w":0.2})
        self.assertEqual(status_code, 200)

    def test_postIris_whenIrisNotFloat_receiveBadRequset(self):
        res,status_code = IsValidJson.check({"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4,"petal_w":"0.2"})
        self.assertEqual(status_code, 500)
        
    def test_postIris_whenIrisNotBitween0_10_receiveBadRequset(self):
        res,status_code = IsValidJson.check({"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4,"petal_w":-0.2})
        self.assertEqual(status_code, 500)
    
    def test_postIris_whenIrisHasAllFields_receiveBadRequset(self):
        res,status_code = IsValidJson.check({"sepal_w":3.5,"petal_l":1.4,"petal_w":0.2})
        self.assertEqual(status_code, 500)
        res,status_code = IsValidJson.check({"sepal_l":5.1,"petal_l":1.4,"petal_w":0.2})
        self.assertEqual(status_code, 500)
        res,status_code = IsValidJson.check({"sepal_l":5.1,"sepal_w":3.5,"petal_w":0.2})
        self.assertEqual(status_code, 500)
        res,status_code = IsValidJson.check({"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4})
        self.assertEqual(status_code, 500)

if __name__=="__main__":
    unittest.main()