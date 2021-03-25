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

@app.route("/makeTrade", methods=['GET', 'POST'])
@cross_origin()
def makeTradeRoute():
    if tradeRequestIsValid(request.data):
        attemptedTrade = makeTrade(request.data["playerId"],request.data["tradeId"],request.data["storyId"])
        if attemptedTrade != False:
            return attemptedTrade
    return {'Error' : 'Could not process trade'}

# A trade requires that the player has the required items in inventory
# If not, this function returns false
# If the story is not a store trade:
#   Update the story states
#   Return new stories, hubs, trades, items that are unlocked
def makeTrade(playerId, tradeId, storyId):
    # Init the dicts
    playerDict = getPlayerById(playerId)
    tradeDict = getTradeById(tradeId)
    storyDict = getStoryById(storyId)

    # Make the trade if possible
    if not tryMakeTrade(playerDict["inventory"], tradeDict["items_in"], tradeDict["items_out"]):
        return False

    # The object returned that adds new trades, stories, hubs
    retDict = {
        "STORIES" : [],
        "TRADES" : [],
        "ITEMS" : [],
        "HUBS" : []
    }

    # The new story id from the trade
    print("-----")
    print(storyDict)
    print("-----")
    newStoryId = storyDict["trade_to_story"][tradeId]

    # Update story states if required (its trade_to_story isn't 0 or storyId)
    if newStoryId != "0" and newStoryId != storyId:
        # The new story
        newStory = getStoryById(newStoryId)
        playerDict["story_states"][storyId] = newStoryId

        retDict["STORIES"] += [newStory]

        for newTradeId in newStory["trade_to_story"]:
            newTrade = getTradeById(newTradeId)
            for itemId in newTrade["items_in"]:
                retDict["ITEMS"] += getItemById(itemId)
            for itemId in newTrade["items_out"]:
                retDict["ITEMS"] += getItemById(itemId)
            retDict["TRADES"] += newTrade

    return retDict


def getPlayerById(id):
    return database.getObjectFromCollectionById("PLAYERS", id)

def getStoryById(id):
    return database.getObjectFromCollectionById("STORIES", id)

def getTradeById(id):
    return database.getObjectFromCollectionById("TRADES", id)

def getItemById(id):
    return database.getObjectFromCollectionById("ITEMS", id)

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