"""
In this we just creating home page and taking input data from client through get mothod
"""
from flask import Flask, request
import numpy as np
import pickle
import pandas as pd


app=Flask(__name__)


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict():
    var = "akash"
    var1 = request.args.get('var1')
    var2 = request.args.get('var2')
    var3 = request.args.get('var3')
    var4 = request.args.get('var4')
    return "Welcome to prediction" +" "+ var + "   "+ var1 +"   "+ var2+ "   "+ var3



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    