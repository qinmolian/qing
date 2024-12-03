import customtkinter as ctk
from tkinter import filedialog, Menu
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
import shutil

# acquire arcgis path
for version in range(1,10,+1):
    arcgis_version = f"Desktop{version}]"
    home_path = os.path.expanduser("~")
    mytoolboxes_path = os.path.join(home_path, "AppData","Roaming", "ESRI",f"Desktop10.{version}","ArcToolbox","My Toolboxes")

    if os.path.exists(mytoolboxes_path):
        arcgis_real = mytoolboxes_path
        break

# Center the main window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to handle the About menu
def show_about():
    about_window = ctk.CTkToplevel(root)
    about_window.title("About")
    about_window.geometry("300x150")
    center_window(about_window, 300, 150)
    label = ctk.CTkLabel(about_window, text="This is a CustomTkinter Example", font=("Arial", 14))
    label.pack(pady=30)

# Function to handle the Language menu
def choose_language():
    def set_language(language):
        lang_label.config(text=f"Language set to: {language}")
        popup.destroy()
    
    popup = ctk.CTkToplevel(root)
    popup.title("Select Language")
    popup.geometry("300x200")
    center_window(popup, 300, 200)
    label = ctk.CTkLabel(popup, text="Choose a language:", font=("Arial", 14))
    label.pack(pady=20)

    btn_chinese = ctk.CTkButton(popup, text="Chinese", command=lambda: set_language("Chinese"))
    btn_chinese.pack(pady=10)

    btn_english = ctk.CTkButton(popup, text="English", command=lambda: set_language("English"))
    btn_english.pack(pady=10)

# Function: Clear the display content
def clear_display():
    for widget in show_window_frame.winfo_children():
        widget.destroy()

# Function: Select functionality placeholder
def selects():
    global select_file,file
    select_file = filedialog.askopenfilenames(title="chosen file")
    if select_file:
        clear_display()
        select_label = ctk.CTkLabel(show_window_frame, text="Select feature triggered.", font=("Arial", 14))
        select_label.pack(pady=20)
        for file in select_file:
            file_item = ctk.CTkLabel(show_window_frame, text=file, font=("Arial", 14),anchor="center")
            file_item.pack(pady=20)

# Function: Install functionality placeholder
def install():
    if not select_file:
        messagebox.showwarning(message="please select file")
        return
    for selects_file in select_file:
        b_name = os.path.basename(selects_file)
        merge = os.path.join(mytoolboxes_path,b_name)
        shutil.copy(selects_file,merge)
        print(selects_file)
    messagebox.showwarning(message="alreally install") 

def open_file():
    os.startfile(mytoolboxes_path)


# Create the main window
root = ctk.CTk()
root.title("CustomTkinter Example")
center_window(root, 700, 400)  # Center the main window

# Create a menu button on the far left with "About" and "Language" options
menu_button = ctk.CTkButton(root, text="≡", width=30, command=None)
menu_button.pack(anchor="w", padx=20, pady=10)

menu = Menu(menu_button, tearoff=0)
menu.add_command(label="About", command=show_about)
menu.add_command(label="Language", command=choose_language)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

menu_button.bind("<Button-1>", show_menu)

# Create a frame for the "Show Window" below the buttons
show_window_frame = ctk.CTkFrame(root, width=600, height=200, corner_radius=10)
show_window_frame.pack(pady=20)
show_window_frame.pack_propagate(False)

# Create a frame for centered buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20)

# Add centered buttons: Selects, Install, and Clear
btn_selects = ctk.CTkButton(button_frame, text="Selects", command=selects)
btn_selects.grid(row=0, column=0, padx=10, pady=10)

btn_install = ctk.CTkButton(button_frame, text="Install", command=install)
btn_install.grid(row=0, column=1, padx=10, pady=10)

btn_clear = ctk.CTkButton(button_frame, text="Clear", command=clear_display)
btn_clear.grid(row=0, column=2, padx=10, pady=10)

btn_clear = ctk.CTkButton(button_frame, text="open file", command=open_file)
btn_clear.grid(row=0, column=3, padx=10, pady=10)


# Label for language setting
lang_label = ctk.CTkLabel(root, text="", font=("Arial", 12))
lang_label.pack()

# Run the main loop
root.mainloop()
