import database
from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def upAndRunning():
    return {'request data': request.data }