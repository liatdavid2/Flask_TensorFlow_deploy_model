from flask import Flask,request
from flask_restful import Resource,Api

import sys
sys.path.append("./classes") # Adds higher directory to python modules path.
from Tf_classification_model import Tf_classification_model
from SvmKernelRbf import SvmKernelRbf
from LogisticRegression import LogisticRegression
from RandomForestClassifier import RandomForestClassifier
from KNeighborsClassifier import KNeighborsClassifier
app= Flask(__name__)
api =Api(app)

api.add_resource(LogisticRegression,'/LogisticRegression')
api.add_resource(SvmKernelRbf,'/SvmKernelRbf')
api.add_resource(RandomForestClassifier,'/RandomForestClassifier')
api.add_resource(KNeighborsClassifier,'/KNeighborsClassifier')
api.add_resource(Tf_classification_model,'/Tf_classification_model')
if __name__=="__main__":
    app.run(debug=True,port=7777)