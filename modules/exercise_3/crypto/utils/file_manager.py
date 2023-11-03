import os

from modules.exercise_3.crypto.encrypt import aes_encrypt_file
from modules.exercise_3.crypto.decrypt import aes_decrypt_file
from modules.uitls.utils import is_valid_input_file, update_preview


def save_encrypted(input_file_var, key_var, output_file_encrypted_var, preview_text_box_encrypted, iv_file_var):
    input_file = input_file_var.get()
    key = key_var.get()
    iv_path = iv_file_var.get()
    key_bytes = None

    iv_bytes = None

    try:
        with open(iv_path, 'rb') as key_file:
            iv_bytes = key_file.read()
    except FileNotFoundError:
        print(f"IV file not found at {key}")

    try:
        with open(key, 'rb') as key_file:
            key_bytes = key_file.read()
    except FileNotFoundError:
        print(f"Key file not found at {key}")
    else:
        # Wrap the key with b''
        key_bytes = b'' + key_bytes

    if not is_valid_input_file(input_file):
        print("Invalid input file path")
        input_file_var.set(f"Error: Input file does not exist: {input_file}")
        return "Invalid input file path"

    valid, encrypted_data = aes_encrypt_file(input_file, output_file_encrypted_var, key_bytes, iv_bytes)
    # Automatically choose a name for the output file
    input_file_name = os.path.basename(input_file)
    output_file_encrypted = os.path.splitext(input_file_name)[0] + "_encrypted.zip"

    if valid:
        with open(output_file_encrypted, 'wb') as f:
            f.write(bytes(encrypted_data))

    # update_preview(encrypted_data, preview_text_box_encrypted)


def save_decrypted(input_file_var, key_var, output_file_decrypted_var, preview_text_box_decrypted, iv_file_var):
    input_file = input_file_var.get()
    iv_path = iv_file_var.get()
    key = key_var.get()
    key_bytes = None
    iv_bytes = None

    try:
        with open(iv_path, 'rb') as key_file:
            iv_bytes = key_file.read()
    except FileNotFoundError:
        print(f"IV file not found at {key}")

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

    print("Input File:", input_file)
    print("Decryption Key:", key)

    if not is_valid_input_file(input_file):
        print("Invalid input file path")
        input_file_var.set(f"Error: Input file does not exist: {input_file}")
        return "Invalid input file path"

    valid, decrypted_text = aes_decrypt_file(input_file, output_file_decrypted_var, key_bytes, iv_bytes)

    # Automatically choose a name for the output file
    input_file_name = os.path.basename(input_file)
    output_file_decrypted = os.path.splitext(input_file_name)[0] + "_decrypted.zip"

    with open(output_file_decrypted, 'wb') as f:
        f.write(bytes(decrypted_text))

    # update_preview(decrypted_text, preview_text_box_decrypted)
