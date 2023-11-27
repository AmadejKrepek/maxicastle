import pyaes
from tqdm import tqdm


def aes_ctr_encrypt(data, key, nonce):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]

    # Counter Mode
    encrypted_blocks = []
    with tqdm(total=len(blocks), desc='Encrypting', unit='blocks') as pbar:
        for block_num, block in enumerate(blocks, start=1):
            counter_64_bytes = block_num.to_bytes(8, byteorder='little', signed=False)
            counter_block = nonce + counter_64_bytes
            encrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
            encrypted_blocks.append(encrypted_block)
            pbar.update(1)

    ciphertext = b''.join(encrypted_blocks)

    return ciphertext


def aes_ctr_encrypt_ccm(data, key, nonce, mac_blocks):
    aes = pyaes.AES(key)
    block_size = 16
    m = len(data)
    blocks = [data[i:i + block_size] for i in range(0, m, block_size)]
    # Counter Mode
    encrypted_blocks = []
    with tqdm(total=len(blocks), desc='Encrypting', unit='blocks') as pbar:
        for block_num, block in enumerate(blocks, start=1):
            counter_64_bytes = block_num.to_bytes(8, byteorder='little', signed=False)
            counter_block = nonce + counter_64_bytes
            encrypted_block = bytes(x ^ y for x, y in zip(aes.encrypt(counter_block), block))
            encrypted_blocks.append(encrypted_block)
            pbar.update(1)

    ciphertext = b''.join([mac_blocks] + encrypted_blocks)

    return ciphertext
