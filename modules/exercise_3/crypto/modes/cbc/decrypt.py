import pyaes


def aes_cbc_decrypt(ciphertext, key, iv):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // block_size + 1
    blocks = [ciphertext[i:i+block_size] for i in range(0, m, block_size)]

    # Cipher Block Chaining
    plaintext = b''
    previous_block = iv
    for block in blocks:
        decrypted_block = aes.decrypt(block)
        xored_block = bytes(x ^ y for x, y in zip(decrypted_block, previous_block))
        plaintext += bytes(xored_block)
        previous_block = block

    return plaintext
