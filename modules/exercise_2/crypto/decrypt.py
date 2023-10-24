from modules.exercise_2.crypto.encrypt import chacha20_encrypt_file


def chacha20_decrypt_file(input_file, output_file, key, iv, position=0):
    chacha20_encrypt_file(input_file, output_file, key, iv, position)  # Encryption and decryption are the same
