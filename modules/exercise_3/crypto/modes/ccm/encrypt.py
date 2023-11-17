import pyaes
from tqdm import tqdm

from modules.exercise_3.crypto.modes.counter.encrypt import aes_ctr_encrypt, aes_ctr_encrypt_ccm
from modules.exercise_3.crypto.utils.utils import pad_data, pad


def calculate_cbc_mac(data):
    block_size = 16
    iv = [0] * 16
    padded_data = pad_data(data, block_size)

    blocks = [padded_data[i:i + block_size] for i in range(0, len(padded_data), block_size)]

    cbc_mac_operation = iv

    with tqdm(total=len(blocks), desc='Calculating MAC', unit='blocks') as pbar:
        for block in blocks:
            xored_block = bytes(x ^ y for x, y in zip(block, cbc_mac_operation))
            cbc_mac_operation = xored_block
            pbar.update(1)

    return cbc_mac_operation


def aes_ccm_encrypt(data, key, nonce):
    mac = calculate_cbc_mac(data)

    increased_nonce = nonce + bytes(8)

    mac_encrypted = bytes(x ^ y for x, y in zip(increased_nonce, mac))

    ciphertext = aes_ctr_encrypt_ccm(data, key, nonce, mac_encrypted)

    return ciphertext
