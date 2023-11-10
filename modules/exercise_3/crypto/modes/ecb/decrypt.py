import pyaes


def aes_ecb_decrypt(ciphertext, key):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // block_size + 1
    blocks = [ciphertext[i:i + block_size] for i in range(0, m, block_size)]

    # Electronic Codebook
    plaintext = b''
    for block in blocks:
        decrypted_block = aes.decrypt(block)
        plaintext += bytes(decrypted_block)

    return plaintext
