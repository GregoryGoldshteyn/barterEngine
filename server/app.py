import common.database
from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def helloWorld():
    return {'request data': request.data }