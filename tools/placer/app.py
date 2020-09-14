import common.database as database
from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def upAndRunning():
    return {'request data': request.data }

@app.route("/item/<int:id>", methods=['GET'])
def getItemById():
    return database.mongoCollections['ITEMS'].find( {'_id' : id} )

@app.route("/item", methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        return database.mongoCollections['ITEMS'].insertOne( request.data )
    else:
        return database.mongoCollections['ITEMS'].find()