import os
from tkinter import filedialog
import customtkinter as ctk


def select():
    global select_1
    select_1 = filedialog.askopenfilenames(title="wk")


def import_2():
    for selects in select_1:
        print(selects)



# Create the main window
root = ctk.CTk()
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


# Create the "open folder path" button (left button)
import_button = ctk.CTkButton(root, text="select Folder", command=select, font=("Arial", 20))
import_button.pack(pady=20)  # Align the button to the left with padding

# Create the "open folder path" button (left button)
import_button = ctk.CTkButton(root, text="import Folder", command=import_2, font=("Arial", 20))
import_button.pack(pady=20)  # Align the button to the left with padding


# Start the main loop of the application
root.mainloop()