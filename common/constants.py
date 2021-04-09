# Info for MongoDB database
MONGO_CONNECTION_STRING="mongodb://localhost:27017"
DEFAULT_DATABASE_NAME="BarterDB"

# Secret key files for server
PRIVATE_KEY_FILE="privatetestkey.pem"
PUBLIC_KEY_FILE="publictestkey.ssh"

# Whether the initial load should come from a database or a file
INIT_FROM_DB = False

# Whether rest operations should use the database or json file
USE_DB = False

COLLECTIONS = [
    "ITEMS",
    "TRADES",
    "STORIES",
    "HUBS",
    "PLAYERS"
]

# File name for local files
COLLECTIONS_JSON_FILE = "localDB/testDatabases/lemonade.json" # = "localDB/collections.json"

# Info for server ports
DEFAULT_PORT=4999