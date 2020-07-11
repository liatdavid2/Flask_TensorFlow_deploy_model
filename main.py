from flask import Flask,request
from flask_restful import Resource,Api

import sys
sys.path.append("./classes") # Adds higher directory to python modules path.
from calc import calc
from Tf_classification_model import Tf_classification_model



app= Flask(__name__)
api =Api(app)

#api.add_resource(calc,'/')
api.add_resource(Tf_classification_model,'/Tf_classification_model')
if __name__=="__main__":
    app.run(debug=True,port=7777)