import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def create_tab5_controls(tab5):
    # Variables to store message digest and signature
    global message_digest, signature

    def generate_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=3096,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def save_keys(private_key, public_key):
        with open("private_key.pem", "wb") as private_key_file:
            private_key_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            private_key_file.write(private_key_pem)

        with open("public_key.pem", "wb") as public_key_file:
            public_key_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            public_key_file.write(public_key_pem)

    def load_keys():
        with open("private_key.pem", "rb") as private_key_file:
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=None,
                backend=default_backend()
            )

        with open("public_key.pem", "rb") as public_key_file:
            public_key = serialization.load_pem_public_key(
                public_key_file.read(),
                backend=default_backend()
            )

        return private_key, public_key

    def sign_and_save_file(private_key, file_path):
        global message_digest, signature

        with open(file_path, 'rb') as file:
            data = file.read()

        # Compute the message digest
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(data)
        message_digest = digest.finalize()

        # Sign the data
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        # Save the data along with the signature
        signed_data = data + b'\nSIGNATURE:' + signature
        signed_file_path = file_path + ".signed"
        with open(signed_file_path, 'wb') as signed_file:
            signed_file.write(signed_data)

        return signed_file_path

    def verify_signed_file(public_key, signed_file_path):
        # Extract the original data and signature from the signed file
        with open(signed_file_path, 'rb') as signed_file:
            signed_data = signed_file.read()

        data, _, signature_from_file = signed_data.partition(b'\nSIGNATURE:')

        result_text.set(result_text.get() + "\n")
        result_text.set(result_text.get() + f"Signature: \n{signature_from_file.hex()}")
        result_text.set(result_text.get() + "\n")

        # Verify the stored signature
        try:
            public_key.verify(
                signature_from_file,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            return True
        except Exception as e:
            return False

    def verify_signature_action():
        _, public_key = load_keys()
        file_path = entry_file_path.get()

        result_text.set(result_text.get() + "\n=============VERIFICATION PROCESS=============\n")
        result_text.set(result_text.get() + "\n")
        # Append the computed message digest
        result_text.set(result_text.get() + f"Computed Message Digest: {message_digest.hex()}\n")
        result_text.set(result_text.get() + "\n")

        # Verify the stored signature
        if verify_signed_file(public_key, file_path + ".signed"):
            result_text.set(result_text.get() + "\n")
            result_text.set(result_text.get() +
                            "Signature is valid!\n")
            result_text.set(result_text.get() + "\n")
        else:
            result_text.set(result_text.get() + "\n")
            result_text.set(result_text.get() + "Signature is NOT valid!\n")
            result_text.set(result_text.get() + "\n")

    def browse_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            entry_file_path.delete(0, tk.END)
            entry_file_path.insert(0, file_path)

    def generate_keys_action():
        private_key, public_key = generate_key_pair()
        save_keys(private_key, public_key)
        result_text.set("Key pair generated and saved successfully!\n")

    def sign_file_action():
        private_key, _ = load_keys()
        file_path = entry_file_path.get()

        # Clear all text before signing
        result_text.set("")

        signed_file_path = sign_and_save_file(private_key, file_path)
        result_text.set(result_text.get() + "\n=============SIGNED PROCESS=============\n")
        result_text.set(result_text.get() + f"Message Digest: {message_digest.hex()}\nSignature: {signature.hex()}\n\n"
                        f"File signed successfully!\nSigned File: {signed_file_path}")
        result_text.set(result_text.get() + "\n")

    # GUI elements
    tk.Label(tab5, text="File Path:").grid(row=0, column=0, padx=10, pady=10)
    entry_file_path = tk.Entry(tab5, width=40)
    entry_file_path.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(tab5, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

    tk.Button(tab5, text="Generate Keys", command=generate_keys_action).grid(row=1, column=0, columnspan=3, pady=10)
    tk.Button(tab5, text="Sign File", command=sign_file_action).grid(row=2, column=0, columnspan=3, pady=10)
    tk.Button(tab5, text="Verify Signature", command=verify_signature_action).grid(row=5, column=0, columnspan=3, pady=10)

    tk.Label(tab5, text="Result:").grid(row=3, column=0, padx=10, pady=10)
    result_text = tk.StringVar()
    result_label = tk.Label(tab5, textvariable=result_text, wraplength=400, justify=tk.LEFT)
    result_label.grid(row=3, column=1, columnspan=2, padx=10, pady=10)