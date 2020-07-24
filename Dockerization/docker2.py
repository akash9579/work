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

@app.route('/predict')
def predict_note_authentication():
	search = request.args.get("search")
	page = request.args.get("page")

    return "Hello"


