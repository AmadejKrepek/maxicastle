import os

from modules.exercise_2.crypto.encrypt import chacha20_encrypt_file
from modules.uitls.utils import is_valid_input_file, update_preview


def generateIV():
    # Generate a 256-bit IV (32 bytes)
    iv = os.urandom(32)
    return iv


def save_encrypted(input_file_var, key_var, output_file_encrypted_var, preview_text_box_encrypted):
    input_file = input_file_var.get()
    key = key_var.get()
    key_bytes = None
    try:
        with open(key, 'rb') as key_file:
            key_bytes = key_file.read()
    except FileNotFoundError:
        print(f"Key file not found at {key}")
    else:
        # Wrap the key with b''
        key_bytes = b'' + key_bytes

        # Now key_bytes contains the key as bytes
        print("Wrapped Key:", key_bytes)

    if not is_valid_input_file(input_file):
        print("Invalid input file path")
        input_file_var.set(f"Error: Input file does not exist: {input_file}")
        return "Invalid input file path"

    # Generate a 256-bit IV (32 bytes)
    iv = generateIV()
    valid, encrypted_data = chacha20_encrypt_file(input_file, output_file_encrypted_var, key_bytes, iv)

    # Automatically choose a name for the output file
    input_file_name = os.path.basename(input_file)
    output_file_encrypted = os.path.splitext(input_file_name)[0] + "_encrypted.zip"

    if valid:
        with open(output_file_encrypted, 'wb') as f:
            f.write(bytes(encrypted_data))

    update_preview(encrypted_data, preview_text_box_encrypted)


def save_decrypted(input_file_var, key_var, output_file_decrypted_var, preview_text_box_decrypted):
    input_file = input_file_var.get()
    key = key_var.get()

    print("Input File:", input_file)
    print("Decryption Key:", key)

    if not is_valid_input_file(input_file):
        print("Invalid input file path")
        input_file_var.set(f"Error: Input file does not exist: {input_file}")
        return "Invalid input file path"

    with open(input_file, 'r', encoding='utf-8') as f:
        ciphertext = f.read()

    decrypted_text = decrypt(ciphertext, key)

    # Automatically choose a name for the output file
    input_file_name = os.path.basename(input_file)
    output_file_decrypted = os.path.splitext(input_file_name)[0] + "_decrypted.txt"

    with open(output_file_decrypted, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

    update_preview(decrypted_text, preview_text_box_decrypted)
