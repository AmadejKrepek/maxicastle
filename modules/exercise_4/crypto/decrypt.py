

import time

from modules.exercise_3.crypto.utils.speed import measure_speed


def aes_decrypt_file(input_file, key, iv, CURRENT_MODE):
    with open(input_file, 'rb') as f:
        data = f.read()

    decrypted_data = []

    start_time = time.time()
    if MODE_CCM == CURRENT_MODE:
        nonce = iv
        decrypted_data = aes_ccm_decrypt(data, key, nonce)
    elif MODE_CTR == CURRENT_MODE:
        nonce = iv
        decrypted_data = aes_ctr_decrypt(data, key, nonce)
    elif MODE_CBC == CURRENT_MODE:
        decrypted_data = aes_cbc_decrypt(data, key, iv)
    elif MODE_ECB == CURRENT_MODE:
        decrypted_data = aes_ecb_decrypt(data, key)

    measure_speed(start_time, data)

    return True, decrypted_data
