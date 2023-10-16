from tkinter import ttk


def create_style():
    # Create a custom style for widgets
    style = ttk.Style()
    style.configure("TButton", foreground="white", background="blue", font=("Helvetica", 12))
    style.configure("TLabel", font=("Helvetica", 14))
    style.map("TButton", background=[("active", "gray")])
