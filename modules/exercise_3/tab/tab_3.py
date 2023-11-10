import os
from tkinter import ttk
import tkinter as tk

from modules.exercise_3.crypto.utils.file_manager import save_encrypted, save_decrypted
from modules.exercise_3.crypto.utils.utils import generate_key
from modules.uitls.utils import open_file


def create_tab3_controls(tab1):
    # Create a sub-frame for encryption controls
    encryption_frame = ttk.LabelFrame(tab1, text="Encryption")
    encryption_frame.grid(column=0, row=1, padx=60, pady=10, sticky="w")

    # Create a sub-frame for decryption controls
    decryption_frame = ttk.LabelFrame(tab1, text="Decryption")
    decryption_frame.grid(column=1, row=1, padx=60, pady=10, sticky="e")

    # Create variables to hold the file path and encryption key
    input_file_var = tk.StringVar()
    output_file_encrypted_var = tk.StringVar()
    output_file_decrypted_var = tk.StringVar()
    key_var = tk.StringVar()

    # Create a sub-frame for key controls
    key_frame = ttk.LabelFrame(tab1, text="Key")
    key_frame.grid(column=0, row=0, padx=60, pady=10, columnspan=2, sticky="w")

    # Create variables to hold the IV file path
    iv_file_var = tk.StringVar()

    # Create a function to generate an IV and save it to a file
    def generate_and_save_iv():
        iv = os.urandom(16)  # Generate an 8-byte IV (64 bits)
        iv_file_path = "iv.txt"  # Specify the path where you want to save the IV
        with open(iv_file_path, 'wb') as iv_file:
            iv_file.write(iv)
        # Update the iv_file_var to hold the IV file path
        iv_file_var.set(iv_file_path)

    # Create a function to upload an IV from a file
    def upload_iv():
        iv_file_path = open_file(iv_file_var)
        if iv_file_path:
            # Update the iv_file_var to hold the IV file path
            iv_file_var.set(iv_file_path)

    # IV controls
    ttk.Button(key_frame, text="Generate IV and Save to File", command=generate_and_save_iv).grid(
        column=6, row=0, padx=10, pady=5, columnspan=3, sticky="w")
    ttk.Button(key_frame, text="Upload IV", command=upload_iv).grid(
        column=9, row=0, padx=10, pady=5, columnspan=3, sticky="e")
    ttk.Label(key_frame, text="IV file path").grid(column=6, row=1, padx=5, pady=5, sticky="w")
    ttk.Entry(key_frame, textvariable=iv_file_var, width=40).grid(column=7, row=1, padx=10, pady=5, columnspan=5)

    # Create a function to generate a key and save it to a file as bytes
    def generate_and_save_key():
        key = generate_key()  # Call your generate_key function to get the key
        key_file_path = "key.txt"  # Specify the path where you want to save the key
        with open(key_file_path, 'wb') as key_file:
            key_file.write(key)

    # Create a function to upload a key from a file
    def upload_key():
        key_file_path = open_file(key_var)
        if key_file_path:
            # Update the input_file_var to hold the key file path
            input_file_var.set(key_file_path)

    # Key controls
    ttk.Button(key_frame, text="Generate Key and Save to File", command=generate_and_save_key).grid(
        column=0, row=0, padx=10, pady=5, columnspan=3, sticky="w")
    ttk.Button(key_frame, text="Upload Key", command=upload_key).grid(
        column=3, row=0, padx=10, pady=5, columnspan=3, sticky="e")
    ttk.Label(key_frame, text="Key file path").grid(column=0, row=1, padx=5, pady=5, sticky="w")
    ttk.Entry(key_frame, textvariable=input_file_var, width=40).grid(column=1, row=1, padx=10, pady=5, columnspan=5)

    # Encryption controls
    ttk.Button(encryption_frame, text="Add File for Encryption", command=lambda: open_file(input_file_var)).grid(
        column=0, row=0, padx=10, pady=5, columnspan=3, sticky="w")
    ttk.Label(encryption_frame, text="Input File").grid(column=0, row=1, padx=10, pady=5, sticky="w")
    ttk.Entry(encryption_frame, textvariable=input_file_var, width=40).grid(column=1, row=1, padx=10, pady=5,
                                                                            columnspan=2)
    ttk.Label(encryption_frame, text="Encryption Key").grid(column=0, row=2, padx=10, pady=5, sticky="w")
    ttk.Entry(encryption_frame, textvariable=key_var, width=20).grid(column=1, row=2, padx=10, pady=5)

    # Decryption controls
    ttk.Button(decryption_frame, text="Add File for Decryption", command=lambda: open_file(input_file_var)).grid(
        column=0, row=0, padx=10, pady=5, columnspan=3, sticky="w")
    ttk.Label(decryption_frame, text="Input File").grid(column=0, row=1, padx=10, pady=5, sticky="w")
    ttk.Entry(decryption_frame, textvariable=input_file_var, width=40).grid(column=1, row=1, padx=10, pady=5,
                                                                            columnspan=2)
    ttk.Label(decryption_frame, text="Decryption Key").grid(column=0, row=2, padx=10, pady=5, sticky="w")
    ttk.Entry(decryption_frame, textvariable=key_var, width=20).grid(column=1, row=2, padx=10, pady=5)

    ttk.Button(tab1, text="Encrypt File",
               command=lambda: save_encrypted(input_file_var, key_var, output_file_encrypted_var,
                                              iv_file_var)
               ).grid(column=0, row=4, padx=10, pady=5)

    ttk.Button(tab1, text="Decrypt File",
               command=lambda: save_decrypted(input_file_var, key_var, output_file_decrypted_var,
                                              iv_file_var)
               ).grid(column=1, row=4, padx=10, pady=5)
