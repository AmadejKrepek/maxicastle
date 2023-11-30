import tkinter as tk
from tkinter import ttk
import hashlib
import os
import struct


def sha256(message):
    return hashlib.sha256(message).digest()


def hmac_sha256(key, message):
    block_size = 64
    if len(key) > block_size:
        key = sha256(key)
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00')

    o_key_pad = bytes(x ^ 0x5c for x in key)
    i_key_pad = bytes(x ^ 0x36 for x in key)

    inner_hash = sha256(i_key_pad + message)
    outer_hash = sha256(o_key_pad + inner_hash)

    return outer_hash


def pbkdf2(password, salt, iterations, dklen):
    hlen = len(sha256(b''))  # SHA-256 hash length
    c = (dklen + hlen - 1) // hlen

    derived_key = b''
    for i in range(1, c + 1):
        u = prf_hmac_sha256(password, salt + struct.pack('>I', i))
        derived_key += u

    return derived_key[:dklen]


def prf_hmac_sha256(key, data):
    return hmac_sha256(key, data)


def create_tab4_controls(tab4):
    # Password entry
    password_label = ttk.Label(tab4, text="Password:")
    password_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

    password_entry = ttk.Entry(tab4, show="*")
    password_entry.grid(row=0, column=1, padx=10, pady=5)

    # Salt entry
    salt_label = ttk.Label(tab4, text="Salt:")
    salt_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

    salt_entry = ttk.Entry(tab4)
    salt_entry.grid(row=1, column=1, padx=10, pady=5)

    # Calculate Hash button
    hash_button = ttk.Button(tab4, text="Calculate Hash",
                             command=lambda: calculate_hash_tab4(tab4, password_entry.get(), salt_entry.get()))
    hash_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Calculate HMAC button
    hmac_button = ttk.Button(tab4, text="Calculate HMAC",
                             command=lambda: calculate_hmac_tab4(tab4, password_entry.get(), salt_entry.get()))
    hmac_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Calculate PBKDF2 button
    pbkdf2_button = ttk.Button(tab4, text="Calculate PBKDF2",
                               command=lambda: calculate_pbkdf2_tab4(tab4, password_entry.get(), salt_entry.get()))
    pbkdf2_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Result labels
    result_label = ttk.Label(tab4, text="Result:")
    result_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

    result_text = tk.Text(tab4, height=10, width=40)
    result_text.grid(row=5, column=1, padx=10, pady=5)


def calculate_hash_tab4(tab, password, salt):
    hash_result = sha256((password + salt).encode()).hex()

    result_str = f"Password: {password}\nSalt: {salt}\nHash Result: {hash_result}"

    result_text = tab.winfo_children()[-1]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result_str)


def calculate_hmac_tab4(tab, password, salt):
    hmac_result = hmac_sha256(password.encode(), salt.encode()).hex()

    result_str = f"Password: {password}\nSalt: {salt}\nHMAC Result: {hmac_result}"

    result_text = tab.winfo_children()[-1]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result_str)


def calculate_pbkdf2_tab4(tab, password, salt):
    derived_key = pbkdf2(password.encode(), salt.encode(), iterations=1000, dklen=32)

    result_str = f"Password: {password}\nSalt: {salt}\nPBKDF2 Result: {derived_key.hex()}"

    result_text = tab.winfo_children()[-1]
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result_str)
