import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry(fg="yellow", bg="blue", width=50)

label.pack()
entry.pack()

window.mainloop()
