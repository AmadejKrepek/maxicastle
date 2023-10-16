import tkinter as tk
from tkinter import ttk

from modules.uitls.utils import open_file, save_encrypted, save_decrypted


def create_tabs(root):
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

    # Create text boxes for file previews with a single vertical scrollbar
    ttk.Label(tab1, text="Preview of Encrypted File").grid(column=0, row=2, padx=60, pady=10)
    preview_text_box_encrypted = tk.Text(tab1, wrap=tk.WORD, height=15, width=50)
    preview_text_box_encrypted.grid(column=0, row=3, padx=60, pady=10, sticky="nsew")

    ttk.Label(tab1, text="Preview of Decrypted File").grid(column=1, row=2, padx=60, pady=10)
    preview_text_box_decrypted = tk.Text(tab1, wrap=tk.WORD, height=15, width=50)
    preview_text_box_decrypted.grid(column=1, row=3, padx=60, pady=10, sticky="nsew")

    scrollbar = tk.Scrollbar(tab1, command=lambda *args: on_scrollbar_move(args, preview_text_box_encrypted,
                                                                           preview_text_box_decrypted))
    scrollbar.grid(column=2, row=3, sticky="ns")

    preview_text_box_encrypted.config(yscrollcommand=scrollbar.set)
    preview_text_box_decrypted.config(yscrollcommand=scrollbar.set)

    # Allow the text boxes and scrollbar to expand when the window is resized
    tab1.columnconfigure(0, weight=1)
    tab1.columnconfigure(1, weight=1)
    tab1.columnconfigure(2, weight=0)
    tab1.rowconfigure(3, weight=1)

    # Function to handle scrollbar movement
    def on_scrollbar_move(args, *text_boxes):
        for text_box in text_boxes:
            text_box.yview(*args)

    # Define button with lambda function to pass arguments
    ttk.Button(tab1, text="Encrypt File",
               command=lambda: save_encrypted(input_file_var, key_var, output_file_encrypted_var,
                                              preview_text_box_encrypted)
               ).grid(column=0, row=4, padx=10, pady=5)

    ttk.Button(tab1, text="Decrypt File",
               command=lambda: save_decrypted(input_file_var, key_var, output_file_decrypted_var,
                                              preview_text_box_decrypted)
               ).grid(column=1, row=4, padx=10, pady=5)
