import pyaes

from modules.exercise_3.crypto.utils.utils import unpad


def aes_cbc_decrypt(ciphertext, key, iv):
    aes = pyaes.AES(key)
    block_size = 16

    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]

    plaintext = b''
    previous_block = iv
    for block in blocks:
        decrypted_block = aes.decrypt(block)
        xored_block = bytes(x ^ y for x, y in zip(decrypted_block, previous_block))
        plaintext += bytes(xored_block)
        previous_block = block

    unpadded_plaintext = unpad(plaintext)

    return unpadded_plaintext
