import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
import shutil


for version in range(1,10,+1):
    arcgis_version = f"Desktop{version}]"
    home_path = os.path.expanduser("~")
    mytoolboxes_path = os.path.join(home_path, "AppData","Roaming", "ESRI",f"Desktop10.{version}","ArcToolbox","My Toolboxes")

    if os.path.exists(mytoolboxes_path):
        arcgis_real = mytoolboxes_path
        break

def open_folder():
    os.startfile(arcgis_real)
    
def import_data():
    # Open file dialog to select a file
    global file_path
    file_path = filedialog.askopenfilenames(title="Select a File")
    global file_name
    for file_path in file_path:
        file_name = file_path.split("/")[-1]  # 获取文件名
    # Insert the file name into the Treeview
        tree.insert("", "end", values=(file_path, file_name))

def install_data():
    in_path = os.path.join(mytoolboxes_path,file_name)
    for in_paths in file_path:
        shutil.copy(in_paths,in_path)
    messagebox.showinfo("成功导入工具箱")
    
# Create the main window
root = tk.Tk()
root.title("Data Import Window")
root.geometry("800x500")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Get the window width and height
window_width = 600
window_height = 500
# Calculate the position to center the window on the screen
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
# Set the window position
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Set the appearance mode (light, dark, or system default)
ctk.set_appearance_mode("system")

# Set the default color theme (e.g., blue, green, dark-blue)
ctk.set_default_color_theme("blue")



# Create a small frame to display the data name
small_frame = tk.Frame(root, width=100, height=100)
small_frame.pack(pady=0.5)

# Create the Treeview to display multiple columns of data
tree = ttk.Treeview(small_frame, columns=("Column 1", "Column 2", "Column 3"), show="headings", height=20)

# Define column headings
tree.heading("Column 1", text="Data path")
tree.heading("Column 2", text="Data name")

# Set column widths
tree.column("Column 1", width=400,anchor="center")
tree.column("Column 2", width=200,anchor="center")

# Add the Treeview to the window
tree.pack(fill=tk.BOTH, expand=True)

# Create the "open folder path" button (left button)
import_button = ctk.CTkButton(root, text="Open Folder", command=open_folder, font=("Arial", 20))
import_button.place(x=10,y=450)  # Align the button to the left with padding

# Create the "Import Data" button (left button)
import_button = ctk.CTkButton(root, text="Import Data", command=import_data, font=("Arial", 20))
import_button.place(x=230,y=450)  # Align the button to the left with padding

# Create the "Install Toolboxes" button (right button)
install_toolboxes = ctk.CTkButton(root, text="Install Boxes", command=install_data, font=("Arial", 20))
install_toolboxes.place(x=450,y=450)  # Align the button to the right with padding

# Start the main loop of the application
root.mainloop()
