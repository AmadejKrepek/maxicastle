import tkinter as tk
from tkinter import ttk
import hashlib
import hmac
import os
import binascii

def generate_salt(length=16):
    return os.urandom(length)

def sha256_hash(password, salt):
    hashed_password = hashlib.sha256(salt + password.encode('utf-8')).hexdigest()
    return hashed_password

def sha512_hash(password, salt):
    hashed_password = hashlib.sha512(salt + password.encode('utf-8')).hexdigest()
    return hashed_password

def generate_hmac(key, message):
    return hmac.new(key, message.encode('utf-8'), hashlib.sha256).hexdigest()

def pbkdf2(password, salt, iterations=10000, key_length=32):
    derived_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations, key_length)
    return binascii.hexlify(derived_key).decode('utf-8')

def create_tab4_controls(tab4):
    # Functions for UI controls on Tab 4
    def calculate_hashes():
        password = password_entry.get()
        salt = generate_salt()

        sha256_result.set(sha256_hash(password, salt))
        sha512_result.set(sha512_hash(password, salt))

    def calculate_hmac():
        key = hmac_key_entry.get()
        message = hmac_message_entry.get()
        hmac_result.set(generate_hmac(key.encode('utf-8'), message))

    def calculate_pbkdf2():
        password = pbkdf2_password_entry.get()
        salt = generate_salt()

        pbkdf2_result.set(pbkdf2(password, salt))

    # UI controls on Tab 4
    ttk.Label(tab4, text="Password:").grid(column=0, row=0, padx=10, pady=10)
    password_entry = ttk.Entry(tab4, show="*")
    password_entry.grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(tab4, text="SHA-256 Result:").grid(column=0, row=1, padx=10, pady=10)
    sha256_result = tk.StringVar()
    ttk.Label(tab4, textvariable=sha256_result).grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(tab4, text="SHA-512 Result:").grid(column=0, row=2, padx=10, pady=10)
    sha512_result = tk.StringVar()
    ttk.Label(tab4, textvariable=sha512_result).grid(column=1, row=2, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate Hashes", command=calculate_hashes).grid(column=0, row=3, columnspan=2, pady=10)

    ttk.Separator(tab4, orient=tk.HORIZONTAL).grid(column=0, row=4, columnspan=2, sticky="ew", pady=10)

    ttk.Label(tab4, text="HMAC Key:").grid(column=0, row=5, padx=10, pady=10)
    hmac_key_entry = ttk.Entry(tab4)
    hmac_key_entry.grid(column=1, row=5, padx=10, pady=10)

    ttk.Label(tab4, text="HMAC Message:").grid(column=0, row=6, padx=10, pady=10)
    hmac_message_entry = ttk.Entry(tab4)
    hmac_message_entry.grid(column=1, row=6, padx=10, pady=10)

    ttk.Label(tab4, text="HMAC Result:").grid(column=0, row=7, padx=10, pady=10)
    hmac_result = tk.StringVar()
    ttk.Label(tab4, textvariable=hmac_result).grid(column=1, row=7, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate HMAC", command=calculate_hmac).grid(column=0, row=8, columnspan=2, pady=10)

    ttk.Separator(tab4, orient=tk.HORIZONTAL).grid(column=0, row=9, columnspan=2, sticky="ew", pady=10)

    ttk.Label(tab4, text="PBKDF2 Password:").grid(column=0, row=10, padx=10, pady=10)
    pbkdf2_password_entry = ttk.Entry(tab4, show="*")
    pbkdf2_password_entry.grid(column=1, row=10, padx=10, pady=10)

    ttk.Label(tab4, text="PBKDF2 Result:").grid(column=0, row=11, padx=10, pady=10)
    pbkdf2_result = tk.StringVar()
    ttk.Label(tab4, textvariable=pbkdf2_result).grid(column=1, row=11, padx=10, pady=10)

    ttk.Button(tab4, text="Calculate PBKDF2", command=calculate_pbkdf2).grid(column=0, row=12, columnspan=2, pady=10)
