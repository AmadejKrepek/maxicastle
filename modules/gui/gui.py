from modules.gui.tabs.tabs import create_tabs
from modules.gui.win.win import define_window
from tkinter import ttk


def prepare_gui(root):
    root.title("Maxi Castle Cryptography")
    define_window(root)
    create_tabs(root)
