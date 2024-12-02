import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def install_data():
    print("Installing toolboxes...")

root = ttk.Window(themename="flatly")
root.geometry("600x500")

install_toolboxes = ttk.Button(root, text="Install Toolboxes", command=install_data, bootstyle="success-outline", width=20)
install_toolboxes.place(x=400, y=450)

root.mainloop()
