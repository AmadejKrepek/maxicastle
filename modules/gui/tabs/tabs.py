import tkinter as tk
from tkinter import ttk

from modules.exercise_1.tab.tab_1 import create_tab1_controls
from modules.exercise_2.tab.tab_2 import create_tab2_controls
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
    ttk.Label(tab1, text="Exercise 1", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)
    ttk.Label(tab2, text="Exercise 2", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)

    create_tab1_controls(tab1)
    create_tab2_controls(tab2)
