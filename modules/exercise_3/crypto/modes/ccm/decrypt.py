import pyaes
from tqdm import tqdm

from modules.exercise_3.crypto.modes.ccm.encrypt import calculate_cbc_mac
from modules.exercise_3.crypto.modes.counter.decrypt import aes_ctr_decrypt_ccm


def aes_ccm_decrypt(ciphertext, key, nonce):
    mac = ciphertext[:16]
    increased_nonce = nonce + bytes(8)

    xored_mac = bytes(x ^ y for x, y in zip(mac, increased_nonce))

    decrypted_data = aes_ctr_decrypt_ccm(ciphertext[16:], key, nonce)

    decrypted_mac = calculate_cbc_mac(decrypted_data)

    if xored_mac != decrypted_mac:
        raise ValueError("MAC is not verified!")

    return decrypted_data

