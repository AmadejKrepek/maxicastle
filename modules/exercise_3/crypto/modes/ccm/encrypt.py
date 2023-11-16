import pyaes


def aes_ccm_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    q = (m - 1) // 16 + 1
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    counter_bytes = b'\x00\x00\x00\x01'
    # Pad the counter to make it 64 bits (8 bytes)
    counter_64_bit = counter_bytes + b'\x00\x00\x00\x00'
    counter_block = nonce + counter_64_bit
    encrypted_blocks = [aes.encrypt(counter_block) for _ in range(q)]
    ciphertext = b''.join(bytes(x ^ y for x, y in zip(encrypted_blocks[i], blocks[i])) for i in range(q))

    return ciphertext
