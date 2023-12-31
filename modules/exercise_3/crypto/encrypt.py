import time

from modules.exercise_3.crypto.modes.cbc.encrypt import aes_cbc_encrypt
from modules.exercise_3.crypto.modes.counter.encrypt import aes_ctr_encrypt
from modules.exercise_3.crypto.modes.ccm.encrypt import aes_ccm_encrypt
from modules.exercise_3.crypto.modes.ecb.encrypt import aes_ecb_encrypt

from modules.exercise_3.crypto.modes.modes import MODE_CCM, MODE_ECB, MODE_CBC, MODE_CTR
from modules.exercise_3.crypto.utils.speed import measure_speed


def aes_encrypt_file(input_file, key, iv, CURRENT_MODE):
    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted_data = []

    start_time = time.time()
    if MODE_CCM == CURRENT_MODE:
        nonce = iv
        encrypted_data = aes_ccm_encrypt(data, key, nonce)
    elif MODE_CTR == CURRENT_MODE:
        nonce = iv
        encrypted_data = aes_ctr_encrypt(data, key, nonce)
    elif MODE_CBC == CURRENT_MODE:
        encrypted_data = aes_cbc_encrypt(data, key, iv)
    elif MODE_ECB == CURRENT_MODE:
        encrypted_data = aes_ecb_encrypt(data, key)

    measure_speed(start_time, data)

    return True, encrypted_data
