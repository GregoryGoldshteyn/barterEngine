from common import database
from flask import request
from flask import render_template
from flask_api import FlaskAPI
from datetime import datetime

app = FlaskAPI(__name__)

@app.route("/", methods=['GET', 'POST'])
def placerRunning():
    return {'request data': request.data }

# Item operations

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

# Trade operations

@app.route("/trade/<int:id>", methods=['GET'])
def getTradeById(id):
    return render_template('tradeViewer.html.j2', trade=database.mongoCollections['TRADES'].find_one( {'_id' : id} ))

@app.route("/trade", methods=['GET','POST'])
def addTrade():
    record = database.mongoCollections['TRADES'].insert_one( parseTradeFromArgs(request.args) )
    return { 'inserted_id:' : record.inserted_id }

@app.route("/tradeplacer", methods=['GET'])
def tradeplacer():
    return render_template('tradePlacer.html.j2')

def parseTradeFromArgs(args):
    retDict = {}

    for arg in args:
        retDict[arg] = args[arg]
    retDict['_id'] = int(retDict['_id'])

    if retDict['short'] == '':
        retDict['short'] = retDict['name']
    if retDict['visibility'] == '':
        retDict['visibility'] = 'never'

    return retDict

# Story operations

@app.route("/story/<int:id>", methods=['GET'])
def getStoryById(id):
    return render_template('storyViewer.html.j2', story=database.mongoCollections['STORIES'].find_one( {'_id' : id} ))

@app.route("/story", methods=['GET','POST'])
def addStory():
    record = database.mongoCollections['STORIES'].insert_one( parseStoryFromArgs(request.args) )
    return { 'inserted_id:' : record.inserted_id }

@app.route("/storyplacer", methods=['GET'])
def storyplacer():
    return render_template('storyPlacer.html.j2')

def parseStoryFromArgs(args):
    retDict = {}

    for arg in args:
        retDict[arg] = args[arg]
    retDict['_id'] = int(retDict['_id'])

    if retDict['short'] == '':
        retDict['short'] = retDict['name']
    if retDict['long'] == '':
        retDict['long'] = "This is the story of " + retDict['name']
    if retDict['visibility'] == '':
        retDict['visibility'] = 'never'

    return retDict

# Hub operations

@app.route("/hub/<int:id>", methods=['GET'])
def getHubById(id):
    return render_template('hubViewer.html.j2', hub=database.mongoCollections['HUBS'].find_one( {'_id' : id} ))

@app.route("/hub", methods=['GET','POST'])
def addHub():
    record = database.mongoCollections['HUBS'].insert_one( parseHubFromArgs(request.args) )
    return { 'inserted_id:' : record.inserted_id }

@app.route("/hubplacer", methods=['GET'])
def hubplacer():
    return render_template('hubPlacer.html.j2')

def parseHubFromArgs(args):
    retDict = {}

    for arg in args:
        retDict[arg] = args[arg]
    retDict['_id'] = int(retDict['_id'])

    if retDict['short'] == '':
        retDict['short'] = retDict['name']
    if retDict['long'] == '':
        retDict['long'] = "This is the hub called " + retDict['name']
    if retDict['time'] == '':
        retDict['time'] = 0
    if retDict['visibility'] == '':
        retDict['visibility'] = 'never'

    return retDict