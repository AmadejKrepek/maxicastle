from modules.exercise_3.crypto.modes.cbc.decrypt import aes_cbc_decrypt
from modules.exercise_3.crypto.modes.ccm.decrypt import aes_ccm_decrypt
from modules.exercise_3.crypto.modes.counter.decrypt import aes_ctr_decrypt
from modules.exercise_3.crypto.modes.ecb.decrypt import aes_ecb_decrypt
from modules.exercise_3.crypto.modes.modes import MODE_CCM, MODE_CBC, MODE_ECB, MODE_CTR
from modules.exercise_3.crypto.utils.utils import generate_nonce, unpad, unpad_data


def aes_decrypt_file(input_file, key, iv, CURRENT_MODE):
    with open(input_file, 'rb') as f:
        data = f.read()

    decrypted_data = []

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

    return True, decrypted_data
