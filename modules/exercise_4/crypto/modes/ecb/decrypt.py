import pyaes
from tqdm import tqdm

from modules.exercise_3.crypto.utils.utils import unpad_data, unpad


def aes_ecb_decrypt(ciphertext, key):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)

    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    plaintext = b''
    with tqdm(total=len(blocks), desc='Decrypting', unit='blocks') as pbar:
        for block in blocks:
            decrypted_block = aes.decrypt(block)
            plaintext += bytes(decrypted_block)
            pbar.update(1)

    unpadded_plaintext = unpad(plaintext)

    return unpadded_plaintext
