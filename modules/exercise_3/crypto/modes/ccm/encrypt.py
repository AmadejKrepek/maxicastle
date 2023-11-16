import pyaes


def aes_ccm_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)

    # Calculate the number of blocks needed
    q = (m - 1) // block_size + 1

    # Divide the data into blocks
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode (CTR) Encryption
    counter_bytes = b'\x00\x00\x00\x01'
    counter_64_bit = counter_bytes + b'\x00\x00\x00\x00'
    counter_block = nonce + counter_64_bit

    # Encrypt each block separately
    encrypted_blocks = [aes.encrypt(counter_block) for _ in range(q)]

    # XOR each encrypted block with the corresponding plaintext block
    ciphertext_blocks = [bytes(x ^ y for x, y in zip(e_block, block)) for e_block, block in
                         zip(encrypted_blocks, blocks)]

    # Combine encrypted blocks to get the ciphertext
    ciphertext = b''.join(ciphertext_blocks)

    return ciphertext
