from common import database
from flask import request
from flask import render_template
from flask_api import FlaskAPI
from datetime import datetime

import json

app = FlaskAPI(__name__)

# Test route to prove app is running
# Just echos back the request data

@app.route("/", methods=['GET', 'POST'])
def echoData():
    return {'request data': request.data }

# Returns all of the local collections

@app.route("/everything", methods=['GET'])
def getEverything():
    return database.localCollections

# Saves the local collections to file

@app.route("/save", methods=['GET'])
def saveToFile():
    return database.writeCollectionsToFile()

# Item operations

@app.route("/item/<id>", methods=['GET'])
def getItemById(id):
    return render_template('itemViewer.html.j2', item=database.getObjectFromCollectionById('ITEMS', id))

@app.route("/item", methods=['GET','POST'])
def addItem():
    if request.method == 'POST':
        record = database.addObjectToCollection('ITEMS', parseItemFromArgs(request.form.to_dict()))
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

    setDefaultPropertiesIfNotSet(retDict)

    if retDict['long'] == '':
        retDict['long'] = "This is a " + retDict['name']
    if retDict['img_small'] == '':
        retDict['img_small'] = retDict['name'] + "_small.png"
    if retDict['img_large'] == '':
        retDict['img_large'] = retDict['name'] + "_large.png"

    return retDict

# Trade operations

@app.route("/trade/<id>", methods=['GET'])
def getTradeById(id):
    return render_template('tradeViewer.html.j2', trade=database.getObjectFromCollectionById('TRADES', id))

@app.route("/trade", methods=['GET','POST'])
def addTrade():
    if request.method == 'POST':
        record = database.addObjectToCollection('TRADES', parseTradeFromArgs(request.form.to_dict()))
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

    setDefaultPropertiesIfNotSet(retDict)

    return retDict

# Story operations

@app.route("/story/<id>", methods=['GET'])
def getStoryById(id):
    return render_template('storyViewer.html.j2', story=database.getObjectFromCollectionById('STORIES', id))

@app.route("/story", methods=['GET','POST'])
def addStory():
    if request.method == 'POST':
        record = database.addObjectToCollection('STORIES', parseStoryFromArgs(request.form.to_dict()))
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

    setDefaultPropertiesIfNotSet(retDict)

    if retDict['long'] == '':
        retDict['long'] = "This is the story of " + retDict['name']

    formatListStringInDictAsJson(retDict, 'stories')

    return retDict

# Hub operations

@app.route("/hub/<id>", methods=['GET'])
def getHubById(id):
    return render_template('hubViewer.html.j2', hub=database.getObjectFromCollectionById('HUBS', id))

@app.route("/hub", methods=['GET','POST'])
def addHub():
    if request.method == 'POST':
        record = database.addObjectToCollection('HUBS', parseHubFromArgs(request.form.to_dict()))
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

    setDefaultPropertiesIfNotSet(retDict)

    if retDict['long'] == '':
        retDict['long'] = "This is the hub called " + retDict['name']
    if retDict['time'] == '':
        retDict['time'] = 0

    formatListStringInDictAsJson(retDict, 'stories')
    formatListStringInDictAsJson(retDict, 'hubs')

    return retDict

# Player operations

@app.route("/player/<id>", methods=['GET'])
def getPlayerById(id):
    return render_template('playerViewer.html.j2', player=database.getObjectFromCollectionById('PLAYERS', id))

@app.route("/player", methods=['GET','POST'])
def addPlayer():
    if request.method == 'POST':
        record = database.addObjectToCollection('PLAYERS', parsePlayerFromArgs(request.form.to_dict()))
        return { 'inserted_id:' : record }
    else:
        return database.getAllObjectsInCollection('PLAYERS')

@app.route("/playerplacer", methods=['GET'])
def playerplacer():
    return render_template('playerPlacer.html.j2')

def parsePlayerFromArgs(args):
    retDict = {}

    for arg in args:
        retDict[arg] = args[arg]

    formatListStringInDictAsJson(retDict, 'inventory')
    formatListStringInDictAsJson(retDict, 'stories')
    formatListStringInDictAsJson(retDict, 'hubs')

    print(retDict)

    return retDict

def formatListStringInDictAsJson(retDict, key):
    if retDict[key] != '':
        retDict[key] = json.loads(retDict[key])

# By default, all objects have a name, short description, and visibility
def setDefaultPropertiesIfNotSet(retDict):
    if retDict['name'] == '':
        retDict['name'] = retDict['_id']
    if retDict['short'] == '':
        retDict['short'] = retDict['name']
    if retDict['visibility'] == '':
        retDict['visibility'] = 'never'