from modules.exercise_3.crypto.modes.cbc.encrypt import aes_cbc_encrypt
from modules.exercise_3.crypto.modes.counter.encrypt import aes_ctr_encrypt
from modules.exercise_3.crypto.modes.ccm.encrypt import aes_ccm_encrypt
from modules.exercise_3.crypto.modes.ecb.encrypt import aes_ecb_encrypt

from modules.exercise_3.crypto.utils.utils import generate_nonce

from modules.exercise_3.crypto.modes.modes import MODE_CCM, MODE_ECB, MODE_CBC, MODE_CTR


def aes_encrypt_file(input_file, output_file, key, iv, position=0):
    with open(input_file, 'rb') as f:
        data = f.read()

    CURRENT_MODE = 0

    encrypted_data = []

    if MODE_CCM == CURRENT_MODE:
        nonce = generate_nonce(12)
        encrypted_data = aes_ccm_encrypt(data, key, nonce)
    elif MODE_CTR == CURRENT_MODE:
        nonce = generate_nonce(12)
        encrypted_data = aes_ctr_encrypt(data, key, nonce)
    elif MODE_CBC == CURRENT_MODE:
        encrypted_data = aes_cbc_encrypt(data, key, iv)
    elif MODE_ECB == CURRENT_MODE:
        encrypted_data = aes_ecb_encrypt(data, key)

    return True, encrypted_data
