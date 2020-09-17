import common.constants as CONSTANTS
import pymongo
import json

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

def writeCollectionsToFile(filename):
    with open(filename, 'w') as json_file:
        json.dump(localCollections, json_file)

def getObjectFromCollectionById(collection, id):
    if CONSTANTS.USE_DB:
        return mongoCollections[collection].find_one( {'_id' : id} )
    else:
        return localCollections[collection][str(id)]

def getAllObjectsInCollection(collection):
    if CONSTANTS.USE_DB:
        retDict = {}
        for entry in mongoCollections[collection].find():
            retDict[entry['_id']] = entry
        return retDict
    else:
        return localCollections[collection]

def addObjectToCollection(collection, obj):
    if CONSTANTS.USE_DB:
        database.mongoCollections[collection].insert_one( parseItemFromArgs(obj) )
    else:
        localCollections[collection][obj['_id']] = obj
    return obj['_id']