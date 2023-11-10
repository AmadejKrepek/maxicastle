import pyaes


def aes_ecb_encrypt(data, key):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    q = (m - 1) // block_size + 1
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Electronic Codebook
    ciphertext = b''
    for block in blocks:
        encrypted_block = aes.encrypt(block)
        ciphertext += bytes(encrypted_block)

    return ciphertext
