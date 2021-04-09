from common import constants
import jwt
import os
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

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