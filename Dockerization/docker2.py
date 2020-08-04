from flask import Flask, request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)

pickle_in = open("regressor.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"



@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    variance=request.args.get("experience")
    skewness=request.args.get("test_score(out of 10)")
    curtosis=request.args.get("interview_score(out of 10)")
    #entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis]])
    print(prediction)
    return "Hello The answer is"+str(prediction)    



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)


