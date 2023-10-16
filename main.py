from ttkthemes import ThemedTk


from modules.gui.gui import prepare_gui
from modules.gui.style.style import create_style

root = ThemedTk()
root.set_theme("black")

create_style()

prepare_gui(root)

root.mainloop()
