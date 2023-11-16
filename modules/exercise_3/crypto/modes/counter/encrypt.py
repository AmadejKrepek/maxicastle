import pyaes



def aes_ctr_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    q = (m - 1) // block_size + 1
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode
    encrypted_blocks = []
    for block_num, block in enumerate(blocks, start=1):
        # Increment the counter for each block
        counter_64_bytes = block_num.to_bytes(8, byteorder='little', signed=False)
        counter_block = nonce + counter_64_bytes
        encrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
        encrypted_blocks.append(encrypted_block)

    ciphertext = b''.join(encrypted_blocks)

    return ciphertext
