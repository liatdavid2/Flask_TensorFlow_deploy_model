from flask_restful import Resource

class calc(Resource):




    def add(self,x,y):
        return x + y

        # url:http://127.0.0.1:7777/
    def get(self):
        return {'aa':self.add(7,7)}

    