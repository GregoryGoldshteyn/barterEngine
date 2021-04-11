from tools.placer.placer import app as placerApp
from server.app import app as serverApp
from threading import Thread
from server import authenticator
import common.database as db
import common.constants as CONSTANTS
import argparse

db.localCollections = db.loadCollectionsFromFile(CONSTANTS.COLLECTIONS_JSON_FILE)

def runPlacer(port):
    placerApp.run(port=port)

def runServer(port):
    serverApp.run(port=port)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--target", help="The target app to run. Valid options are 'server' or 'placer'. Defaults to server")
    parser.add_argument("--port", help="The port on which to run the app. Defaults to " + str(CONSTANTS.DEFAULT_PORT), type=int)
    
    args = parser.parse_args()
    
    port = args.port if args.port else CONSTANTS.DEFAULT_PORT
    
    if not args.target or args.target == "server":
        runServer(port)
    elif args.target == "placer":
        runPlacer(port)
    else:
        print("Invalid target " + args.target)
        exit(1)