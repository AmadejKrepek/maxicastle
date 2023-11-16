import pyaes

from modules.exercise_3.crypto.utils.utils import unpad


def aes_ctr_decrypt(ciphertext, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // block_size + 1
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    decrypted_blocks = []
    for block_num, block in enumerate(blocks, start=1):
        # Increment the counter for each block
        counter_bytes = (block_num).to_bytes(8, byteorder='little', signed=False)
        counter_block = nonce + counter_bytes
        decrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
        decrypted_blocks.append(decrypted_block)

    plaintext = b''.join(decrypted_blocks)

    return plaintext
