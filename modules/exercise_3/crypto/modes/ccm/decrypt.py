import pyaes


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
    decrypted_blocks = [bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block)) for block in blocks]

    # Combine decrypted blocks to get the plaintext
    plaintext = b''.join(decrypted_blocks)

    return plaintext

