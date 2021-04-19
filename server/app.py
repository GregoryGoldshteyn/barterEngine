from common import database as db
from flask import Flask, request, render_template, abort
from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
from datetime import datetime

from functools import lru_cache
from server.authenticator import validateToken

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

@app.route("/makeTrade", methods=['POST'])
@cross_origin()
def makeTradeRoute():
    if tradeRequestIsValid(request.data):
        playerId = request.data["playerId"]
        validation = validateToken(request, playerId)
        print(validation)
        if 'Error' in validation:
            abort(validation['status'], description=validation['Error'])
        attemptedTrade = makeTrade(playerId,request.data["tradeId"],request.data["storyId"])
        if attemptedTrade != False:
            return attemptedTrade
    abort(400, description='Could not process trade')

@app.route("/getInitialState/<id>", methods=['GET'])
@cross_origin()
def getInitialStateRoute(id):
    validation = validateToken(request, playerId)
    print(validation)
    if 'Error' in validation:
        abort(validation['status'], description=validation['Error'])
    return getInitialState(id)

# A trade requires that the player has the required items in inventory
# If not, this function returns false
# If the story is not a store trade:
#   Update the story states
#   Return new stories, hubs, trades, items that are unlocked
def makeTrade(playerId, tradeId, storyId):
    # Init the dicts
    playerDict = db.getPlayerById(playerId)
    tradeDict = db.getTradeById(tradeId)
    storyDict = db.getStoryById(storyId)

    # Make the trade if possible
    if not tryMakeTrade(playerDict["inventory"], tradeDict["items_in"], tradeDict["items_out"]):
        return False

    # The object returned that adds new trades, stories, hubs
    retDict = {}

    # The new story id from the trade
    newStoryId = storyDict["trade_to_story"][tradeId]

    getAllItemsForStory(newStoryId, retDict)

    return retDict

# Get initial state for a new player
def getInitialState(playerId):
    playerDict = db.getPlayerById(playerId)

    retDict = {"PLAYER" : playerDict}

    # Get info for all hubs
    for hubId in playerDict["hub_states"]:
        getAllItemsForHub(hubId, retDict)

    # Get info for all stories
    for storyId in playerDict["story_states"]:
        getAllItemsForStory(storyId, retDict)

    # Get info for all items in inventory
    for itemId in playerDict["inventory"]:
        getItemInfo(itemId, retDict)

    return retDict

def getAllItemsForHub(hubId, retDict = {}):
    # Init stories in retDict if not exist
    if "HUBS" not in retDict:
        retDict["HUBS"] = {}

    newHub = db.getHubById(hubId)

    for storyId in newHub["stories"]:
        getAllItemsForStory(storyId, retDict)

    for hubId in newHub["hubs"]:
        getHubInfo(hubId, retDict)

    retDict["HUBS"][hubId] = newHub

    return retDict

# Gets the info about a single hub
# Required to get populate hub data for hubs that point to hubs
def getHubInfo(hubId, retDict = {}):
    # Init hubs in retDict if not exist
    if "HUBS" not in retDict:
        retDict["HUBS"] = {}

    newHub = db.getHubById(hubId)

    retDict["HUBS"][hubId] = newHub

    return retDict

def getAllItemsForStory(storyId, retDict = {}):
    # Init stories in retDict if not exist
    if "STORIES" not in retDict:
        retDict["STORIES"] = {}

    newStory = db.getStoryById(storyId)

    for tradeId in newStory["trade_to_story"]:
        getAllItemsForTrade(tradeId, retDict)

    retDict["STORIES"][storyId] = newStory

    return retDict

# Modifies a retdict to contain a trade and all items for a trade
def getAllItemsForTrade(tradeId, retDict = {}):
    # Init trades and items if they do not exist
    if "TRADES" not in retDict:
        retDict["TRADES"] = {}
    if "ITEMS" not in retDict:
        retDict["ITEMS"] = {}
    
    # Get trade
    newTrade = db.getTradeById(tradeId)

    # Get all items for trade
    for itemId in newTrade["items_in"]:
        getItemInfo(itemId, retDict)
    for itemId in newTrade["items_out"]:
        getItemInfo(itemId, retDict)

    retDict["TRADES"][tradeId] = newTrade

    return retDict

def getItemInfo(itemId, retDict = {}):
    # Init items if they do not exist
    if "ITEMS" not in retDict:
        retDict["ITEMS"] = {}
    
    retDict["ITEMS"][itemId] = db.getItemById(itemId)

    return retDict

# Returns false if the trade cannot be made
# Else, makes the trade and returns true
def tryMakeTrade(inventory, items_in, items_out):
    # Check if can make trade
    for item, number_of_item in items_in.items():
        if inventory[item] < number_of_item:
            return False
    
    # Remove items into the trade
    for item, number_of_item in items_in.items():
        inventory[item] -= number_of_item

    # Add items out of the trade
    for item, number_of_item in items_out.items():
        if item in inventory:
            inventory[item] += number_of_item
        else:
            inventory[item] = number_of_item
    
    return True

def tradeRequestIsValid(data):
    if "storyId" not in data:
        return False
    if "playerId" not in data:
        return False
    if "tradeId" not in data:
        return False
    return True