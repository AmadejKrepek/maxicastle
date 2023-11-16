import pyaes


def aes_ccm_decrypt(ciphertext, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // block_size + 1
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode
    counter_bytes = b'\x00\x00\x00\x01'
    counter_64_bit = counter_bytes + b'\x00\x00\x00\x00'
    counter_block = nonce + counter_64_bit

    # Counter Mode encryption
    encrypted_blocks = [aes.encrypt(counter_block) for _ in range(q)]

    # Calculate CBC-MAC
    mac = encrypted_blocks[-1]  # The last block is the MAC

    # Decrypt the ciphertext using Counter Mode
    decrypted_blocks = [bytes(x ^ y for x, y in zip(e_block, block)) for e_block, block in zip(encrypted_blocks[:-1], blocks)]

    # Combine decrypted blocks to get plaintext
    plaintext = b''.join(decrypted_blocks)

    # Verify MAC (optional but recommended for security)
    calculated_mac = aes.encrypt(nonce + counter_bytes)  # Calculate MAC based on nonce and counter
    if calculated_mac != mac:
        raise ValueError("MAC verification failed. The message may have been tampered with.")

    return plaintext

