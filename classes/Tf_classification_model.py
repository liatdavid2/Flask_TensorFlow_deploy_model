from flask_restful import Resource
from flask import request

import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from keras import backend as K
import tensorflow as tf

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('models/tensorflow/final_iris_model.h5')
class Tf_classification_model(Resource):

    def return_prediction(self,model,scaler,sample_json):    
        # if json has a lot of field loop throught the fields
        s_len = sample_json["sepal_l"]
        s_wid = sample_json["sepal_w"]
        p_len = sample_json["petal_l"]
        p_wid = sample_json["petal_w"]
        
        flower = [[s_len,s_wid,p_len,p_wid]]
        classes = np.array(['Iris-setosa','Iris-versicolor','Iris-virginica'])
        flower = scaler.transform(flower)
        with graph.as_default():
            class_id = model.predict_classes(flower)[0]
        return classes[class_id]
    # http://127.0.0.1:7777/Tf_classification_model
    # body:{"sepal_l":6.3,"sepal_w":2.7,"petal_l":4.9,"petal_w":1.8}
    def post(self):        
        some_json = request.get_json()
        flower_scaler = joblib.load('models/tensorflow/iris_scaler.pkl')
        results = self.return_prediction(model,flower_scaler,some_json)
        return results

    def get(self):  
        return 1