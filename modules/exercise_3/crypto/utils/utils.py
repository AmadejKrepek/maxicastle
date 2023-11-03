import os


def generate_key():
    key = os.urandom(32)
    return key


def generateIV():
    # Generate a 256-bit IV (32 bytes)
    iv = os.urandom(32)
    return iv
