from flask_restful import Resource
from flask import request

import numpy as np
import pandas as pd
import joblib

from joblib import dump, load
from IsValidJson import IsValidJson
from SklearnPredictor import SklearnPredictor

class SvmKernelRbf(Resource):

    # http://127.0.0.1:7777/SvmKernelRbf
    # body:{"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4,"petal_w":0.2}
    # result -> "Iris-setosa"
    def post(self):        
        #post body must be in valid json format
        try:        
            some_json = request.get_json()
        except:
            return "not a valid json format",500  
        res,status_code = IsValidJson.check(some_json)
        if status_code != 200: return res,500
        svm_SVC_model = load('models/sklearn/SvmKernelRbf.joblib') 
        results = SklearnPredictor.Predict(svm_SVC_model,res)
        return results