"""
In this we just creating home page and predict page 
"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd


app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict():
    var = "akash"

    return "Welcome to prediction" +" "+ var 



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
    