from tkinter import filedialog
import os
import tkinter as tk
from modules.exercise_1.crypto.decrypt import decrypt
from modules.exercise_1.crypto.encrypt import encrypt


def open_file(file_var):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_var.set(file_path)


def update_preview(encrypted_text, text_widget):
    if encrypted_text:
        try:
            if text_widget.get("1.0", "end-1c"):
                text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, encrypted_text)
        except Exception as e:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, f"Error reading: {str(e)}")


def is_valid_input_file(input_file):
    if not os.path.exists(input_file):
        return False
    return True


def save_encrypted(input_file_var, key_var, output_file_encrypted_var, preview_text_box_encrypted):
    input_file = input_file_var.get()
    key = key_var.get()

    if not is_valid_input_file(input_file):
        print("Invalid input file path")
        input_file_var.set(f"Error: Input file does not exist: {input_file}")
        return "Invalid input file path"

    with open(input_file, 'r', encoding='utf-8') as f:
        plaintext = f.read()

    valid, encrypted_text = encrypt(plaintext, key)

    # Automatically choose a name for the output file
    input_file_name = os.path.basename(input_file)
    output_file_encrypted = os.path.splitext(input_file_name)[0] + "_encrypted.txt"

    if valid:
        with open(output_file_encrypted, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

    update_preview(encrypted_text, preview_text_box_encrypted)


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
