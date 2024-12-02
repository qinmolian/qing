import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import shutil


for version in range(1,8,+1):
    arcigs_version = f""
home_path = os.path.expanduser("~")
mytoolboxes_path = os.path.join(home_path, "AppData","Roaming", "ESRI","Desktop10.8","ArcToolbox","My Toolboxes")

def import_data():
    # Open file dialog to select a file
    global file_path
    file_path = filedialog.askopenfilename(title="Select a File")
    print(file_path)
    global file_name
    file_name = file_path.split("/")[-1]
    # Insert the file name into the Treeview
    tree.insert("", "end", values=(file_name, "2"))

def install_data():
    in_path = os.path.join(mytoolboxes_path,file_name)
    shutil.copy(file_path,in_path)
    
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

# Create a small frame to display the data name
small_frame = tk.Frame(root, width=100, height=100, bg="red")
small_frame.pack(pady=0.5)

# Create the Treeview to display multiple columns of data
tree = ttk.Treeview(small_frame, columns=("Column 1", "Column 2", "Column 3"), show="headings", height=20)

# Define column headings
tree.heading("Column 1", text="Data path")
tree.heading("Column 2", text="Data name")

# Set column widths
tree.column("Column 1", width=300)
tree.column("Column 2", width=300)

# Add the Treeview to the window
tree.pack(fill=tk.BOTH, expand=True)

# Create the "Import Data" button (left button)
import_button = tk.Button(root, text="Import Data", command=import_data, font=("Arial", 14))
import_button.place(x=25,y=450)  # Align the button to the left with padding

# Create the "Install Toolboxes" button (right button)
install_toolboxes = tk.Button(root, text="Install Toolboxes", command=install_data, font=("Arial", 14))
install_toolboxes.place(x=450,y=450)  # Align the button to the right with padding

# Start the main loop of the application
root.mainloop()
