import pyaes
from tqdm import tqdm


def aes_ccm_decrypt(ciphertext, key, nonce):
    # Create an AES cipher object with the provided key
    aes = pyaes.AES(key)

    # Set the block size (standard for AES)
    block_size = 16

    # Calculate the number of blocks needed
    m = len(ciphertext)
    q = (m - 1) // block_size + 1

    # Divide the ciphertext into blocks
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode (CTR) Decryption

    # Initialize tqdm for decryption progress
    with tqdm(total=len(blocks), desc='Decrypting', unit='blocks') as pbar:
        decrypted_blocks = []
        for i in range(q):
            counter_64_bit = i.to_bytes(8, byteorder='big')
            counter_block = nonce + counter_64_bit

            decrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), blocks[i]))
            decrypted_blocks.append(decrypted_block)
            pbar.update(1)

    # Combine decrypted blocks to get the plaintext
    plaintext = b''.join(decrypted_blocks)

    return plaintext

