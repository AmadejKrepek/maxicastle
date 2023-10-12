import tkinter as tk

window = tk.Tk()

# Create label
welcome_label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",
    background="black",
    width=35,
    height=5
)

hex_label = tk.Label(
    text="Hello guys",
    foreground="#ffffff",
    background="black",
    width=35,
    height=5
)

# Add widget with Label class to window
welcome_label.pack()
hex_label.pack()

window.mainloop()
