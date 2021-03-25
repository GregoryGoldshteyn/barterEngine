from tools.placer.placer import app as placerApp
from server.app import app as serverApp
import common.database as db
import common.constants as CONSTANTS

db.localCollections = db.loadCollectionsFromFile(CONSTANTS.COLLECTIONS_JSON_FILE)

# placerApp.run()
serverApp.run(port=4999)