import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk


from modules.gui.gui import prepare_gui

root = ThemedTk()
root.set_theme("black")

# Create a custom style for widgets
style = ttk.Style()
style.configure("TButton", foreground="white", background="blue", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 14))
style.map("TButton", background=[("active", "gray")])

prepare_gui(root)

root.mainloop()
