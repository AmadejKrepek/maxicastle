import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils

def create_tab5_controls(tab5):
    def generate_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def sign_file(private_key, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(public_key, file_path, signature):
        with open(file_path, 'rb') as file:
            data = file.read()
        try:
            public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except utils.InvalidSignature:
            return False

    def browse_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            entry_file_path.delete(0, tk.END)
            entry_file_path.insert(0, file_path)

    def sign_file_action():
        private_key, _ = generate_key_pair()
        file_path = entry_file_path.get()
        signature = sign_file(private_key, file_path)
        result_text.set(f"File signed successfully!\nSignature: {signature.hex()}")

    def verify_signature_action():
        _, public_key = generate_key_pair()
        file_path = entry_file_path.get()
        signature_hex = entry_signature.get()
        signature = bytes.fromhex(signature_hex)
        is_valid = verify_signature(public_key, file_path, signature)
        result_text.set(f"Signature verification: {'Valid' if is_valid else 'Invalid'}")

    # GUI elements
    tk.Label(tab5, text="File Path:").grid(row=0, column=0, padx=10, pady=10)
    entry_file_path = tk.Entry(tab5, width=40)
    entry_file_path.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(tab5, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

    tk.Label(tab5, text="Signature:").grid(row=1, column=0, padx=10, pady=10)
    entry_signature = tk.Entry(tab5, width=40)
    entry_signature.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(tab5, text="Sign File", command=sign_file_action).grid(row=2, column=0, columnspan=3, pady=10)
    tk.Button(tab5, text="Verify Signature", command=verify_signature_action).grid(row=3, column=0, columnspan=3, pady=10)

    tk.Label(tab5, text="Result:").grid(row=4, column=0, padx=10, pady=10)
    result_text = tk.StringVar()
    result_label = tk.Label(tab5, textvariable=result_text, wraplength=400, justify=tk.LEFT)
    result_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10)