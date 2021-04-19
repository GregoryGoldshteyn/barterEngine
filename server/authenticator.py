from common import constants
from common import database as db

import jwt
import os
import time

from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

from flask import Blueprint, abort, jsonify, request
from flask_cors import CORS, cross_origin

authenticator = Blueprint('authenticator', __name__, template_folder='templates')

@authenticator.route("/login", methods=['POST'])
@cross_origin()
def loginRoute():
    if 'private_key'not in keyDict:
        init()

    if "player_id" not in request.data:
        abort(404, description="no player id in request body")

    player_id = request.data["player_id"]
    player = db.getPlayerById(player_id)
    if 'Error' in player:
        abort(404, description="player not found")

    # The time the token expires at from current epoch in seconds
    expires_at = int(time.time()) + constants.TOKEN_EXPIRY

    token = jwt.encode({'algorithm': 'RS256', 'expiresAt' : expires_at, 'player_id': player_id}, keyDict["private_key"], algorithm="RS256")
    return {
        'idToken' : token,
        'expiresAt' : expires_at
    }

@authenticator.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Method for validating a token against a player id
def validateToken(request, playerId):
    if 'private_key'not in keyDict:
        init()

    token = request.headers.get('Authorization')
    
    if token == None:
        return {'Error' : 'User is not logged in', 'status' : 401}
    
    try:
        decoded_token = jwt.decode(token, keyDict['public_key'], algorithms=["RS256"])
    except jwt.DecodeError:
        return {'Error' : 'Token is invalid, could not be parsed', 'status' : 400}

    
    if 'player_id' not in decoded_token:
        return {'Error' : 'Token is invalid, no player_id issued in token', 'status' : 400}
    if 'expiresAt' not in decoded_token:
        return {'Error' : 'Token is invalid, no expiry issued in token', 'status' : 400}

    if(decoded_token['player_id'] != playerId):
        return {'Error' : 'Unauthorized; player is attempting to make request on other player behalf', 'status' : 403}
    if(int(decoded_token['expiresAt']) < int(time.time())):
        return {'Error' : 'Token expired. Please login again', 'status' : 401}

    return {'Success'}


# Stores keys once generated or loaded from file
keyDict = {}

# Functions for dealing with RSA keys
def save_private_key(key, filename):
    pem = key.private_bytes(
        encoding=crypto_serialization.Encoding.PEM,
        format=crypto_serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=crypto_serialization.NoEncryption()
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def save_public_key(key, filename):
    pem = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    with open(filename, 'wb') as pem_out:
        pem_out.write(pem)

def load_private_key(filename):
    with open(filename, 'rb') as keyFile:
        return crypto_serialization.load_pem_private_key(
            keyFile.read(),
            password=None
        )

def load_public_key(filename):
    with open(filename, 'rb') as keyFile:
        return crypto_serialization.load_ssh_public_key(
            keyFile.read()
        )

def generate_key():
    return rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )

# Inits the authenticator
# Loads keys from file if possible or generates and saves if not
def init():
    if not os.path.isfile(constants.PRIVATE_KEY_FILE):
        key = generate_key()
        save_private_key(key, constants.PRIVATE_KEY_FILE)
        save_public_key(key, constants.PUBLIC_KEY_FILE)

    private_key = load_private_key(constants.PRIVATE_KEY_FILE)
    public_key = load_public_key(constants.PUBLIC_KEY_FILE)

    keyDict['private_key'] = private_key
    keyDict['public_key'] = public_key

# Test methods
def testEncode(private_key):
    print(private_key)
    return jwt.encode({'test_key': 'test_val'}, private_key, algorithm="RS256")

def testDecode(public_key, message):
    return jwt.decode(message, public_key, algorithms=["RS256"])