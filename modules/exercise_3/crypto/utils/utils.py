import os
import secrets


def generate_key():
    key = os.urandom(16)
    return key


def generateIV():
    # Generate a 256-bit IV (32 bytes)
    iv = os.urandom(32)
    return iv


def pad(text):
    padding_len = 16 - (len(text) % 16)
    for i in range(padding_len):
        text += bytes([padding_len])
    return text


def pad_data(data, block_size):
    padding_size = block_size - (len(data) % block_size)
    if padding_size == 0:
        padding_size = block_size
    padded_data = data + bytes([padding_size] * padding_size)
    return padded_data


def unpad_data(data):
    padding_size = data[-1]
    return data[:-padding_size]


def unpad(padded_message):
    # Extract the last byte to determine the length of the padding
    pad_length = padded_message[-1]

    # Verify that the padding is valid
    if pad_length == 0 or pad_length > len(padded_message):
        raise ValueError("Invalid padding")

    # Extract the padded portion of the message
    padded_portion = padded_message[-pad_length:]

    # Verify that the padded portion has the correct structure
    if not all(byte == pad_length for byte in padded_portion):
        raise ValueError("Invalid padding structure")

    # Remove the padding
    unpadded_message = padded_message[:-pad_length]

    return unpadded_message


def split_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]


def generate_nonce(size: object = 12) -> object:
    """
    Generate a random nonce for cryptographic use.

    Parameters:
    - size (int): The size of the nonce in bytes. Default is 12 bytes.

    Returns:
    - bytes: A random nonce.
    """
    return secrets.token_bytes(size)
