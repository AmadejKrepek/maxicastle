import pyaes
from tqdm import tqdm

from modules.exercise_3.crypto.utils.utils import unpad, unpad_data


def aes_cbc_decrypt(ciphertext, key, iv):
    aes = pyaes.AES(key)
    block_size = 16

    blocks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]

    plaintext = b''
    previous_block = iv
    with tqdm(total=len(blocks), desc='Decrypting', unit='blocks') as pbar:
        for block in blocks:
            decrypted_block = aes.decrypt(block)
            xored_block = bytes(x ^ y for x, y in zip(decrypted_block, previous_block))
            plaintext += bytes(xored_block)
            previous_block = block
            pbar.update(1)

    unpadded_plaintext = unpad_data(plaintext)

    return unpadded_plaintext
