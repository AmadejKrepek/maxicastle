import tkinter as tk
from tkinter import ttk, filedialog
import os

# Slovenian alphabet
slovenian_alphabet = "ABCČDEFGHIJKLMNOPRSŠTUZŽ"


# Hill cipher encryption function for Slovenian alphabet
def encrypt(plaintext, key):
    key = key.replace(" ", "").upper()
    n = int(len(key) ** 0.5)
    # Ensure the key length is sufficient for a square matrix
    while len(key) < n * n:
        key += "A"  # You can use any character for padding

    matrix = [[slovenian_alphabet.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]
    encrypted_text = ""

    for i in range(0, len(plaintext), n):
        block = [slovenian_alphabet.index(char) for char in plaintext[i:i + n]]
        result = [sum(matrix[i][j] * block[j] for j in range(n)) % len(slovenian_alphabet) for i in range(n)]
        encrypted_text += ''.join(slovenian_alphabet[char] for char in result)

    return encrypted_text


# Hill cipher decryption function for Slovenian alphabet
def decrypt(ciphertext, key):
    key = key.replace(" ", "").upper()
    n = int(len(key) ** 0.5)
    matrix = [[slovenian_alphabet.index(char) for char in key[i:i + n]] for i in range(0, len(key), n)]
    matrix_inverse = [[0] * n for _ in range(n)]

    det = sum(matrix[0][i] * (
                matrix[1][(i + 1) % n] * matrix[2][(i + 2) % n] - matrix[1][(i + 2) % n] * matrix[2][(i + 1) % n]) for i
              in range(n))
    det %= len(slovenian_alphabet)

    for i in range(n):
        for j in range(n):
            cofactor = matrix[(j + 1) % n][(i + 1) % n] * matrix[(j + 2) % n][(i + 2) % n] - matrix[(j + 2) % n][
                (i + 1) % n] * matrix[(j + 1) % n][(i + 2) % n]
            matrix_inverse[i][j] = (cofactor * det) % len(slovenian_alphabet)

    decrypted_text = ""

    for i in range(0, len(ciphertext), n):
        block = [slovenian_alphabet.index(char) for char in ciphertext[i:i + n]]
        result = [sum(matrix_inverse[i][j] * block[j] for j in range(n)) % len(slovenian_alphabet) for i in range(n)]
        decrypted_text += ''.join(slovenian_alphabet[char] for char in result)

    return decrypted_text


def create_tabs(root):
    def open_file(file_var):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            file_var.set(file_path)

    def update_preview(file_var, text_widget):
        file_path = file_var.get()
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert(tk.END, content)
            except Exception as e:
                text_widget.delete(1.0, tk.END)
                text_widget.insert(tk.END, f"Error reading file: {str(e)}")

    def save_encrypted():
        input_file = input_file_var.get()
        key = key_var.get()

        with open(input_file, 'r', encoding='utf-8') as f:
            plaintext = f.read()

        encrypted_text = encrypt(plaintext, key)

        # Automatically choose a name for the output file
        input_file_name = os.path.basename(input_file)
        output_file_encrypted = os.path.splitext(input_file_name)[0] + "_encrypted.txt"

        with open(output_file_encrypted, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)

        update_preview(output_file_encrypted_var, preview_text_box_encrypted)

    def save_decrypted():
        input_file = input_file_var.get()
        key = key_var.get()

        with open(input_file, 'r', encoding='utf-8') as f:
            ciphertext = f.read()

        decrypted_text = decrypt(ciphertext, key)

        # Automatically choose a name for the output file
        input_file_name = os.path.basename(input_file)
        output_file_decrypted = os.path.splitext(input_file_name)[0] + "_decrypted.txt"

        with open(output_file_decrypted, 'w', encoding='utf-8') as f:
            f.write(decrypted_text)

        update_preview(output_file_decrypted_var, preview_text_box_decrypted)

    # Create a ttk.Notebook
    tabControl = ttk.Notebook(root)

    # Create tab frames
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    # Add tabs to the Notebook
    tabControl.add(tab1, text='Exercise 1')
    tabControl.add(tab2, text='Exercise 2')

    # Configure padding and styling for the tabs
    style = ttk.Style()
    style.configure('TNotebook.Tab', padding=(20, 15))  # Adjust the padding as needed

    # Pack the Notebook to fill the available space
    tabControl.pack(expand=1, fill="both")

    # Labels for the tabs
    ttk.Label(tab1, text="Exercise 1").grid(column=0, row=0, padx=60, pady=30)
    ttk.Label(tab2, text="Exercise 2").grid(column=0, row=0, padx=60, pady=30)

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

    # Encryption controls
    ttk.Label(encryption_frame, text="Input File").grid(column=0, row=0, padx=10, pady=5, sticky="w")
    ttk.Entry(encryption_frame, textvariable=input_file_var, width=40).grid(column=1, row=0, padx=10, pady=5,
                                                                            columnspan=2)
    ttk.Label(encryption_frame, text="Encryption Key").grid(column=0, row=1, padx=10, pady=5, sticky="w")
    ttk.Entry(encryption_frame, textvariable=key_var, width=20).grid(column=1, row=1, padx=10, pady=5)
    ttk.Button(encryption_frame, text="Add File for Encryption", command=lambda: open_file(input_file_var)).grid(
        column=2, row=0, padx=10, pady=5)
    ttk.Button(encryption_frame, text="Encrypt File", command=save_encrypted).grid(column=1, row=2, padx=10, pady=5)

    # Decryption controls
    ttk.Label(decryption_frame, text="Input File").grid(column=0, row=0, padx=10, pady=5, sticky="w")
    ttk.Entry(decryption_frame, textvariable=input_file_var, width=40).grid(column=1, row=0, padx=10, pady=5,
                                                                            columnspan=2)
    ttk.Label(decryption_frame, text="Decryption Key").grid(column=0, row=1, padx=10, pady=5, sticky="w")
    ttk.Entry(decryption_frame, textvariable=key_var, width=20).grid(column=1, row=1, padx=10, pady=5)
    ttk.Button(decryption_frame, text="Add File for Decryption", command=lambda: open_file(input_file_var)).grid(
        column=2, row=0, padx=10, pady=5)
    ttk.Button(decryption_frame, text="Decrypt File", command=save_decrypted).grid(column=1, row=2, padx=10, pady=5)

    # Create text boxes for file previews
    ttk.Label(tab1, text="Preview of Encrypted File").grid(column=0, row=2, padx=60, pady=10)
    preview_text_box_encrypted = tk.Text(tab1, wrap=tk.WORD, height=10, width=40)
    preview_text_box_encrypted.grid(column=0, row=3, padx=60, pady=10)

    ttk.Label(tab1, text="Preview of Decrypted File").grid(column=1, row=2, padx=60, pady=10)
    preview_text_box_decrypted = tk.Text(tab1, wrap=tk.WORD, height=10, width=40)
    preview_text_box_decrypted.grid(column=1, row=3, padx=60, pady=10)