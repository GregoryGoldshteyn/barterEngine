from common import database
from flask import Flask
from flask import request
from flask import render_template
from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from datetime import datetime

import json

app = FlaskAPI(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Test route to prove app is running
# Just echos back the request data

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def echoData():
    return { 'request data': request.data }