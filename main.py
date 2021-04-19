from tools.placer.placer import placer_tool as placer_blueprint
from server.app import app as serverApp
from threading import Thread
from server.authenticator import authenticator as authenticator_blueprint
import common.database as db
import common.constants as CONSTANTS
import argparse

db.localCollections = db.loadCollectionsFromFile(CONSTANTS.COLLECTIONS_JSON_FILE)

def runServer(port):
    serverApp.register_blueprint(placer_blueprint, url_prefix='/placer')
    serverApp.register_blueprint(authenticator_blueprint, url_prefix='/authenticator')
    serverApp.run(port=port)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="The port on which to run the app. Defaults to " + str(CONSTANTS.DEFAULT_PORT), type=int)
    
    args = parser.parse_args()
    
    port = args.port if args.port else CONSTANTS.DEFAULT_PORT

    runServer(port)