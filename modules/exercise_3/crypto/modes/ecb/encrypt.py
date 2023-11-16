import pyaes

from modules.exercise_3.crypto.utils.utils import pad_data


def aes_ecb_encrypt(data, key):
    aes = pyaes.AES(key)
    block_size = 16

    padded_data = pad_data(data, block_size)
    blocks = [padded_data[i:i + block_size] for i in range(0, len(padded_data), block_size)]

    # Electronic Codebook
    ciphertext = b''
    for block in blocks:
        encrypted_block = aes.encrypt(block)
        ciphertext += bytes(encrypted_block)

    return ciphertext
