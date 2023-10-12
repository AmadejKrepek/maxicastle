import tkinter as tk

window = tk.Tk()

# Create label
greeting = tk.Label(text="Hello, Tkinter")

# Add widget with Label class to window
greeting.pack()

window.mainloop()
