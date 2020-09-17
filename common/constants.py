# Info for MongoDB database
MONGO_CONNECTION_STRING="mongodb://localhost:27017"
DEFAULT_DATABASE_NAME="BarterDB"

# Whether the initial load should come from a database or a file
INIT_FROM_DB = False

# Whether rest operations should use the database or json file
USE_DB = False

COLLECTIONS = [
    "ITEMS",
    "TRADES",
    "STORIES",
    "HUBS"
]

# File name for local files
COLLECTIONS_JSON_FILE = "localDB/collections.json"