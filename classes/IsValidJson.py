from flask import jsonify
from flask import request
iris_fields = ['sepal_l','sepal_w','petal_l','petal_w']
class IsValidJson():    
    def check(some_json):
        for key, value in some_json.items():
        # each of json fields must be float
            if not isinstance(value, float):
                return ("Error: "+key+" value ("+str(value)+") must be float!"),500 
        # each of json fields must be bitween 0 and 10 
            if(value <0 or value >10):
                return ("Error: "+key+" value ("+str(value)+") must be bitween 0 and 10!"),500      
        # all iris fields exists
        for field in iris_fields:
            if field not in some_json:
                return ("Error:missed "+field+" field!"),500       
        return some_json,200

