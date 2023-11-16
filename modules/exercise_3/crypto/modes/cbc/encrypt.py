import pyaes

from modules.exercise_3.crypto.utils.utils import pad, pad_data


def aes_cbc_encrypt(data, key, iv):
    aes = pyaes.AES(key)
    block_size = 16

    padded_data = pad_data(data, block_size)
    blocks = [padded_data[i:i+block_size] for i in range(0, len(padded_data), block_size)]

    # Cipher Block Chaining
    ciphertext = b''
    previous_block = iv
    for block in blocks:
        xored_block = bytes(x ^ y for x, y in zip(block, previous_block))
        encrypted_block = aes.encrypt(xored_block)
        ciphertext += bytes(encrypted_block)
        previous_block = encrypted_block

    return ciphertext
