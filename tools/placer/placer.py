from common import database
from flask import request
from flask import render_template
from flask_api import FlaskAPI
from datetime import datetime

app = FlaskAPI(__name__)

# Test route to prove app is running
# Just echos back the request data

@app.route("/", methods=['GET', 'POST'])
def echoData():
    return {'request data': request.data }

# Item operations

@app.route("/item/<int:id>", methods=['GET'])
def getItemById(id):
    return render_template('itemViewer.html.j2', item=database.getObjectFromCollectionById('ITEMS', id))

@app.route("/item", methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        record = database.addObjectToCollection('ITEMS', parseItemFromArgs(request.args))
        return { 'inserted_id:' : record }
    else:
        return database.getAllObjectsInCollection('ITEMS')

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
    return render_template('tradeViewer.html.j2', trade=database.getObjectFromCollectionById('TRADES', id))

@app.route("/trade", methods=['GET','POST'])
def addTrade():
    if request.method == 'POST':
        record = addObjectToCollection('TRADES', parseItemFromArgs(request.args))
        return { 'inserted_id:' : record }
    else:
        return database.getAllObjectsInCollection('TRADES')

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
    return render_template('storyViewer.html.j2', story=database.getObjectFromCollectionById('STORIES', id))

@app.route("/story", methods=['GET','POST'])
def addStory():
    if request.method == 'POST':
        record = addObjectToCollection('STORIES', parseItemFromArgs(request.args))
        return { 'inserted_id:' : record }
    else:
        return database.getAllObjectsInCollection('STORIES')

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
    return render_template('hubViewer.html.j2', hub=database.getObjectFromCollectionById('HUBS', id))

@app.route("/hub", methods=['GET','POST'])
def addHub():
    if request.method == 'POST':
        record = addObjectToCollection('HUBS', parseItemFromArgs(request.args))
        return { 'inserted_id:' : record }
    else:
        return database.getAllObjectsInCollection('HUBS')

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