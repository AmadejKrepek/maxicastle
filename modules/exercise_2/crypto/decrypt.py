from modules.exercise_2.crypto.encrypt import chacha20_encrypt_file
from modules.exercise_2.crypto.utils.utils import chacha20_block


def chacha20_decrypt_file(input_file, output_file, key, iv, position=0):
    iv = None
    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted_data = []
    for i in range(0, len(data), 64):
        block = chacha20_block(key, iv, position)
        position += 1
        encrypted_block = bytes(a ^ b for a, b in zip(data[i:i + 64], block))
        encrypted_data.extend(encrypted_block)

    return True, encrypted_data
