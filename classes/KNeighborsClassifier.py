from flask_restful import Resource
from flask import request, abort, jsonify
import json

import numpy as np
import pandas as pd
import joblib
from joblib import dump, load
from SklearnPredictor import SklearnPredictor

import sys
#sys.path.append("/Exceptions")
from IsValidJson import IsValidJson

class KNeighborsClassifier(Resource):

    # http://127.0.0.1:7777/KNeighborsClassifier
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
        KNeighborsClassifier_model = load('models/sklearn/KNeighborsClassifier.joblib') 
        results = SklearnPredictor.Predict(KNeighborsClassifier_model,some_json)
        return results,200