import os
import secrets


def generate_key():
    key = os.urandom(16)
    return key


def generateIV():
    # Generate a 256-bit IV (32 bytes)
    iv = os.urandom(32)
    return iv


def pad(m):
    pad_length = 16 - len(m) % 16
    padding = bytes([pad_length] * pad_length)
    return m + padding + bytes([16] * 16)


def split_blocks(data, block_size):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]


def generate_nonce(size: object = 12) -> object:
    """
    Generate a random nonce for cryptographic use.

    Parameters:
    - size (int): The size of the nonce in bytes. Default is 12 bytes.

    Returns:
    - bytes: A random nonce.
    """
    return secrets.token_bytes(size)
