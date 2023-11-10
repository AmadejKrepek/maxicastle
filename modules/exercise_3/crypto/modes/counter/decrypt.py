import pyaes


def aes_ctr_decrypt(ciphertext, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // block_size + 1
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode
    counter_block = nonce + b'\x00\x00\x00\x01'  # Assuming 32-bit counter
    decrypted_blocks = [bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block)) for block in blocks]
    plaintext = b''.join(decrypted_blocks)

    return plaintext
