from flask_restful import Resource
from flask import request

import numpy as np
import pandas as pd
import joblib

from joblib import dump, load

class RandomForestClassifier(Resource):

    def return_prediction(self,model,sample_json):    
        # if json has a lot of field loop throught the fields
        s_len = sample_json["sepal_l"]
        s_wid = sample_json["sepal_w"]
        p_len = sample_json["petal_l"]
        p_wid = sample_json["petal_w"]
        
        flower = [[s_len,s_wid,p_len,p_wid]]
        classes = np.array(['Iris-setosa','Iris-versicolor','Iris-virginica'])
        class_id = model.predict(np.array(flower) )
        return classes[class_id[0]]
    # http://127.0.0.1:7777/RandomForestClassifier
    # body:{"sepal_l":5.1,"sepal_w":3.5,"petal_l":1.4,"petal_w":0.2}
    # result -> "Iris-setosa"
    def post(self):        
        some_json = request.get_json()
        RandomForestClassifier_model = load('models/sklearn/RandomForestClassifier.joblib') 
        results = self.return_prediction(RandomForestClassifier_model,some_json)
        return results