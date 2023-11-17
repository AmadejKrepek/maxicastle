import pyaes
from tqdm import tqdm


def aes_ccm_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)

    # Calculate the number of blocks needed
    q = (m - 1) // block_size + 1

    # Divide the data into blocks
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode (CTR) Encryption

    # Initialize tqdm for combined progress
    tqdm_combined = tqdm(total=q * 2, desc="Encrypting and XORing", unit="block")

    # Encrypt each block separately and XOR with the corresponding plaintext block
    encrypted_blocks = []
    for i in range(q):
        counter_64_bit = i.to_bytes(8, byteorder='big')
        counter_block = nonce + counter_64_bit

        encrypted_block = aes.encrypt(counter_block)
        ciphertext_block = bytes(x ^ y for x, y in zip(encrypted_block, blocks[i]))
        encrypted_blocks.append(ciphertext_block)
        tqdm_combined.update(2)  # Update progress for both encryption and XOR

    # Close tqdm for combined progress
    tqdm_combined.close()

    # Combine encrypted blocks to get the ciphertext
    ciphertext = b''.join(encrypted_blocks)

    return ciphertext
