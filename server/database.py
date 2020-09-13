import constants
import pymongo

# Init database

mongoClient = pymongo.MongoClient(constants.MONGO_CONNECTION_STRING)
mongoDatabase = mongoClient[constants.DEFAULT_DATABASE_NAME]
mongoCollections = {}

for collectionName in constants.COLLECTIONS:
    mongoCollections[collectionName] = mongoDatabase[collectionName]

