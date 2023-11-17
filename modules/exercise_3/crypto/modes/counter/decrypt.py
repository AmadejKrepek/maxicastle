import pyaes
from tqdm import tqdm


def aes_ctr_decrypt(ciphertext, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    decrypted_blocks = []
    with tqdm(total=len(blocks), desc='Decrypting', unit='blocks') as pbar:
        for block_num, block in enumerate(blocks, start=1):
            counter_bytes = block_num.to_bytes(8, byteorder='little', signed=False)
            counter_block = nonce + counter_bytes
            decrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
            decrypted_blocks.append(decrypted_block)
            pbar.update(1)

    plaintext = b''.join(decrypted_blocks)

    return plaintext
