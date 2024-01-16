from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, NameResolutionError
import json
from datetime import datetime as dt

# ff. imports are for getting secret values from .env file
from pathlib import Path
import os

from modelling.utilities.loaders import load_model

# # configure location of build file and the static html template file
app = Flask(__name__, template_folder='static')

# since simple html from url http://127.0.0.1:5000 requests to
# api endpoint at http://127.0.0.1:5000/ we must set the allowed
# origins or web apps with specific urls like http://127.0.0.1:5000
# to be included otherwise it will be blocked by CORS policy
CORS(app, origins=["http://localhost:5173", "http://127.0.0.1:5000",])

model_names = []
scaler = None
encoder = None

def load_models():
    """
    prepares and loads sample input and custom model in
    order to use trained weights/parameters/coefficients
    """

    # recreate model architecture
    saved_lgbm = load_model('./modelling/saved/models/lgbm.pkl')
    model_names.append(type(saved_lgbm).__name__)

def load_preprocessors():
    """
    prepares and loads the saved encoders, normalizers of
    the dataset to later transform raw user input from
    client-side
    """
    
    global saved_bc_scaler, saved_bc_Y_le
    saved_bc_scaler = load_model('./modelling/misc/saved/bc_scaler.pkl')
    saved_bc_Y_le = load_model('./modelling/misc/saved/bc_Y_le.pkl')

load_models()
load_preprocessors()



# upon loading of client side fetch the model names
@app.route('/model-names', methods=['GET'])
def retrieve_model_names():
    """
    flask app will run at http://127.0.0.1:5000 if /
    in url succeeds another string <some string> then
    app will run at http://127.0.0.1:5000/<some string>

    returns json object of all model names loaded upon
    start of server and subsequent request of client to
    this view function
    """

    data = {
        'model_names': model_names
    }

    # return data at once since no error will most likely
    # occur on mere loading of the model
    return jsonify(data)

@app.route('/predict', methods=['POST'])
def predict():
    raw_data = request.json
    print(raw_data)



    return jsonify({})

# write here function that will take in all user input from client