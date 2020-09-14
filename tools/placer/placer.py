from common import database
from flask import request
from flask import render_template
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def placerRunning():
    return {'request data': request.data }

@app.route("/item/<int:id>", methods=['GET'])
def getItemById(id):
    return render_template('itemViewer.html.j2', item=database.mongoCollections['ITEMS'].find_one( {'_id' : id} ))

@app.route("/item", methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        record = database.mongoCollections['ITEMS'].insert_one( request.data )
        return { 'inserted_id:' : record.inserted_id }
    else:
        return {'request data': request.data }

@app.route("/itemplacer", methods=['GET'])
def itemplacer():
    return render_template('itemPlacer.html.j2')