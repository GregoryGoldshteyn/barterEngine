from common import database
from flask import request
from flask import render_template
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def placerRunning():
    print(request.args) 
    return {'request data': request.data }

@app.route("/item/<int:id>", methods=['GET'])
def getItemById(id):
    return render_template('itemViewer.html.j2', item=database.mongoCollections['ITEMS'].find_one( {'_id' : id} ))

@app.route("/item", methods=['GET','POST'])
def addItem():
    record = database.mongoCollections['ITEMS'].insert_one( parseItemFromArgs(request.args) )
    return { 'inserted_id:' : record.inserted_id }

@app.route("/itemplacer", methods=['GET'])
def itemplacer():
    return render_template('itemPlacer.html.j2')

def parseItemFromArgs(args):
    retDict = {}

    for arg in args:
        retDict[arg] = args[arg]
    retDict['_id'] = int(retDict['_id'])

    if retDict['short'] == '':
        retDict['short'] = retDict['name']
    if retDict['long'] == '':
        retDict['long'] = "This is a " + retDict['name']
    if retDict['img_small'] == '':
        retDict['img_small'] = retDict['name'] + "_small.png"
    if retDict['img_large'] == '':
        retDict['img_large'] = retDict['name'] + "_large.png"
    if retDict['visibility'] == '':
        retDict['visibility'] = 'never'

    return retDict