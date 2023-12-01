import tkinter as tk
from tkinter import ttk

from modules.exercise_1.tab.tab_1 import create_tab1_controls
from modules.exercise_2.tab.tab_2 import create_tab2_controls
from modules.exercise_3.tab.tab_3 import create_tab3_controls
from modules.exercise_4.tab.tab_4 import create_tab4_controls
from modules.exercise_5.tab.tab_5 import create_tab5_controls


def create_tabs(root):
    # Create a ttk.Notebook
    tabControl = ttk.Notebook(root)

    # Create tab frames
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    # Add tabs to the Notebook
    tabControl.add(tab1, text='Hill Cipher')
    tabControl.add(tab2, text='ChaCha20')
    tabControl.add(tab3, text='AES')
    tabControl.add(tab4, text='HASH/MAC')
    tabControl.add(tab5, text='Digital Signing')

    # Configure padding and styling for the tabs
    style = ttk.Style()
    style.configure('TNotebook.Tab', padding=(20, 15))  # Adjust the padding as needed

    # Pack the Notebook to fill the available space
    tabControl.pack(expand=1, fill="both")

    # Labels for the tabs
    ttk.Label(tab1, text="Hill Cipher", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)
    ttk.Label(tab2, text="ChaCha20", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)
    ttk.Label(tab3, text="AES", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)
    ttk.Label(tab4, text="HASH", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)
    ttk.Label(tab4, text="Digital Signing", font=("Helvetica", 16, "bold")).grid(column=0, row=0, padx=60, pady=30, columnspan=2)

    create_tab1_controls(tab1)
    create_tab2_controls(tab2)
    create_tab3_controls(tab3)
    create_tab4_controls(tab4)
    create_tab5_controls(tab5)
