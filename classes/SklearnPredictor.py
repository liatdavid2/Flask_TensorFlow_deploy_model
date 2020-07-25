import numpy as np

class SklearnPredictor():
    def Predict(model,sample_json):    
        # if json has a lot of field loop throught the fields
        s_len = sample_json["sepal_l"]
        s_wid = sample_json["sepal_w"]
        p_len = sample_json["petal_l"]
        p_wid = sample_json["petal_w"]
        
        flower = [[s_len,s_wid,p_len,p_wid]]
        classes = np.array(['Iris-setosa','Iris-versicolor','Iris-virginica'])
        class_id = model.predict(np.array(flower) )
        return classes[class_id[0]]