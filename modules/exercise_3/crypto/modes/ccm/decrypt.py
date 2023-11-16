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
    counter_bytes = b'\x00\x00\x00\x01'
    counter_64_bit = counter_bytes + b'\x00\x00\x00\x00'
    counter_block = nonce + counter_64_bit

    # Decrypt each block separately
    decrypted_blocks = []
    with tqdm(total=len(blocks), desc='Decrypting', unit='blocks') as pbar:
        for block in blocks:
            decrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
            decrypted_blocks.append(decrypted_block)
            pbar.update(1)  # Update the progress bar

    # Combine decrypted blocks to get the plaintext
    plaintext = b''.join(decrypted_blocks)

    return plaintext

