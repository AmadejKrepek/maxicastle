import pyaes


def aes_ccm_decrypt(ciphertext, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(ciphertext)
    q = (m - 1) // 16 + 1
    blocks = [ciphertext[i:i+block_size] for i in range(0, m, block_size)]

    # Counter Mode
    counter_block = nonce + b'\x00\x00\x00\x01'  # Assuming 32-bit counter
    encrypted_blocks = [aes.encrypt(counter_block) for _ in range(q)]

    decrypted_blocks = [bytes(x ^ y for x, y in zip(e_block, block)) for e_block, block in zip(encrypted_blocks, blocks)]
    plaintext = b''.join(decrypted_blocks)

    return plaintext

