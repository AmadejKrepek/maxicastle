import pyaes

from modules.exercise_3.crypto.utils.utils import pad


def aes_cbc_encrypt(data, key, iv):
    aes = pyaes.AES(key)
    block_size = 16
    data = pad(data)
    m = len(data)
    q = (m - 1) // block_size + 1
    blocks = [data[i:i+block_size] for i in range(0, m, block_size)]

    # Cipher Block Chaining
    ciphertext = b''
    previous_block = iv
    for block in blocks:
        xored_block = bytes(x ^ y for x, y in zip(block, previous_block))
        encrypted_block = aes.encrypt(xored_block)
        ciphertext += bytes(encrypted_block)
        previous_block = encrypted_block

    return ciphertext
