import tkinter as tk

window = tk.Tk()

# Create label
welcome_label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

hex_label = tk.Label(
    text="Hello guys",
    foreground="#ffffff",
    background="black"
)

# Add widget with Label class to window
welcome_label.pack()
hex_label.pack()

window.mainloop()
