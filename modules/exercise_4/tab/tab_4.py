import tkinter as tk
from tkinter import ttk
import hashlib
import hmac
import os
import binascii


def generate_salt(length=16):
    return os.urandom(length)


def generate_key(length=32):
    return os.urandom(length)


def sha256_hash(password, salt):
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    return hashed_password


def sha512_hash(password, salt):
    hashed_password = hashlib.sha512(salt + password.encode('utf-8')).hexdigest()
    return hashed_password


def xor_bytes(b1, b2):
    return bytes(x ^ y for x, y in zip(b1, b2))


def generate_hmac(key, message):
    block_size = 64  # Block size for SHA-256
    opad = bytes(x ^ 0x5c for x in range(256))
    ipad = bytes(x ^ 0x36 for x in range(256))

    # Ensure the key is less than the block size
    if len(key) > block_size:
        key = hashlib.sha256(key).digest()

    # Pad the key if it is less than the block size
    key = key.ljust(block_size, b'\x00')

    # XOR the key with ipad and opad
    key_ipad = xor_bytes(key, ipad)
    key_opad = xor_bytes(key, opad)

    # Calculate inner hash
    inner_hash = hashlib.sha256(key_ipad + message.encode('utf-8')).digest()

    # Calculate outer hash
    outer_hash = hashlib.sha256(key_opad + inner_hash).hexdigest()

    return outer_hash



def pbkdf2(password, salt, iterations=10000, key_length=32):
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, key_length)
    return binascii.hexlify(derived_key).decode('utf-8')


def create_tab4_controls(tab4):
    # Functions for UI controls on Tab 4
    def calculate_hashes():
        password = password_entry.get()
        salt = generate_salt()
        sha256_result.set(sha256_hash(password, salt))

    def calculate_hmac():
        key = hmac_key_entry.get()
        message = password_entry.get()  # Use the same input for HMAC message
        hmac_result.set(generate_hmac(key.encode('utf-8'), message))

    def calculate_pbkdf2():
        password = password_entry.get()
        salt = generate_salt()
        pbkdf2_result.set(pbkdf2(password, salt))

    def generate_salt_and_key():
        salt_entry.delete(0, tk.END)
        salt_entry.insert(0, generate_salt().hex())

        hmac_key_entry.delete(0, tk.END)
        hmac_key_entry.insert(0, generate_key().hex())

    # UI controls on Tab 4
    ttk.Label(tab4, text="Password:").grid(column=0, row=0, padx=10, pady=10)
    password_entry = ttk.Entry(tab4, show="*")
    password_entry.grid(column=1, row=0, padx=10, pady=10)

    ttk.Button(tab4, text="Generate Salt & Key", command=generate_salt_and_key).grid(column=0, row=2, columnspan=2, pady=10)

    ttk.Label(tab4, text="Salt:").grid(column=0, row=3, padx=10, pady=10)
    salt_entry = ttk.Entry(tab4)
    salt_entry.grid(column=1, row=3, padx=10, pady=10)

    ttk.Label(tab4, text="SHA-256 Result:").grid(column=0, row=4, padx=10, pady=10)
    sha256_result = tk.StringVar()
    ttk.Label(tab4, textvariable=sha256_result).grid(column=1, row=4, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate Hashes", command=calculate_hashes).grid(column=0, row=5, columnspan=2, pady=10)

    ttk.Separator(tab4, orient=tk.HORIZONTAL).grid(column=0, row=6, columnspan=2, sticky="ew", pady=10)

    ttk.Label(tab4, text="HMAC Key:").grid(column=0, row=7, padx=10, pady=10)
    hmac_key_entry = ttk.Entry(tab4)
    hmac_key_entry.grid(column=1, row=7, padx=10, pady=10)

    ttk.Label(tab4, text="HMAC Message:").grid(column=0, row=8, padx=10, pady=10)
    ttk.Label(tab4, text="Uses the same input as Password").grid(column=1, row=8, padx=10, pady=10)

    ttk.Label(tab4, text="HMAC Result:").grid(column=0, row=9, padx=10, pady=10)
    hmac_result = tk.StringVar()
    ttk.Label(tab4, textvariable=hmac_result).grid(column=1, row=9, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate HMAC", command=calculate_hmac).grid(column=0, row=10, columnspan=2, pady=10)

    ttk.Separator(tab4, orient=tk.HORIZONTAL).grid(column=0, row=11, columnspan=2, sticky="ew", pady=10)

    ttk.Label(tab4, text="PBKDF2 Result:").grid(column=0, row=12, padx=10, pady=10)
    pbkdf2_result = tk.StringVar()
    ttk.Label(tab4, textvariable=pbkdf2_result).grid(column=1, row=12, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate PBKDF2", command=calculate_pbkdf2).grid(column=0, row=13, columnspan=2, pady=10)