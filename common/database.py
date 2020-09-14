import common.constants as CONSTANTS
import pymongo

# Init database

mongoClient = pymongo.MongoClient(CONSTANTS.MONGO_CONNECTION_STRING)
mongoDatabase = mongoClient[CONSTANTS.DEFAULT_DATABASE_NAME]
mongoCollections = {}

for collectionName in CONSTANTS.COLLECTIONS:
    mongoCollections[collectionName] = mongoDatabase[collectionName]