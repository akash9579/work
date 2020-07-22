from flask import Flask, request
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

pickle_in = open("regressor.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    variance=request.args.get("experience")
    skewness=request.args.get("test_score")
    curtosis=request.args.get("interview_score")
    prediction=classifier.predict([[variance,skewness,curtosis]])
    print(prediction)
    return "Hello The answer is"+str(prediction)


if __name__=='__main__':
    app.run()