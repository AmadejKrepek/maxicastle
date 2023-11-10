import pyaes


def aes_ctr_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    q = (m - 1) // block_size + 1
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode
    counter_block = nonce + b'\x00\x00\x00\x01'  # Assuming 32-bit counter
    encrypted_blocks = [bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block)) for block in blocks]
    ciphertext = b''.join(encrypted_blocks)

    return ciphertext
