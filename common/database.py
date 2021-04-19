import common.constants as CONSTANTS
import pymongo
import json

from functools import lru_cache

# Init database

mongoClient = pymongo.MongoClient(CONSTANTS.MONGO_CONNECTION_STRING)
mongoDatabase = mongoClient[CONSTANTS.DEFAULT_DATABASE_NAME]
mongoCollections = {}

for collectionName in CONSTANTS.COLLECTIONS:
    mongoCollections[collectionName] = mongoDatabase[collectionName]

# Local caching and loading of database
# Stored in the format { "COLLECTION_NAME " : {"<ID>" : {<Entry>}, "<ID2>" : {<Entry2>} ... } ... }

localCollections = {}

def loadCollectionsFromDatabase():
    for collectionName in CONSTANTS.COLLECTIONS:
        localCollections[collectionName] = {}
        for entry in mongoCollections[collectionName].find():
            localCollections[collectionName][entry['_id']] = entry

def loadCollectionsFromFile(filename):
    return json.loads(open(filename).read())

def writeCollectionsToFile(filename=CONSTANTS.COLLECTIONS_JSON_FILE):
    with open(filename, 'w') as json_file:
        json.dump(localCollections, json_file, indent=2)
    return {"saveTo": filename}

def getObjectFromCollectionById(collection, id):
    if CONSTANTS.USE_DB:
        return mongoCollections[collection].find_one( {'_id' : id} )
    else:
        l = list(filter(lambda x: x['_id'] == id ,localCollections[collection]))
        if len(l) > 0:
            return l[0]
        else:
            return {"Error" : "Item not found"}

def getAllObjectsInCollection(collection):
    if CONSTANTS.USE_DB:
        retDict = {}
        for entry in mongoCollections[collection].find():
            retDict[entry['_id']] = entry
        return retDict
    else:
        return localCollections[collection] if collection in localCollections else {}

def addObjectToCollection(collection, obj):
    if CONSTANTS.USE_DB:
        mongoCollections[collection].insert_one( obj )
    else:
        localCollections[collection] += [obj]
    return obj['_id']

# Player objects CANNOT be cached
# This is because they should change during gameplay
def getPlayerById(id):
    return getObjectFromCollectionById("PLAYERS", id)

# Hubs, stories, trades, and items can be cached, because they should
# NOT change over the course of gameplay
@lru_cache(maxsize=None)
def getHubById(id):
    return getObjectFromCollectionById("HUBS", id)

@lru_cache(maxsize=None)
def getStoryById(id):
    return getObjectFromCollectionById("STORIES", id)

@lru_cache(maxsize=None)
def getTradeById(id):
    return getObjectFromCollectionById("TRADES", id)

@lru_cache(maxsize=None)
def getItemById(id):
    return getObjectFromCollectionById("ITEMS", id)