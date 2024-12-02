import customtkinter as ctk
import tkinter as tk

def install_data():
    print("Installing toolboxes...")

# Create the main window
root = tk.Tk()
root.geometry("600x500")

# Set the appearance mode (light, dark, or system default)
ctk.set_appearance_mode("light")

# Set the default color theme (e.g., blue, green, dark-blue)
ctk.set_default_color_theme("blue")

# Create a rounded button using customtkinter
install_toolboxes = ctk.CTkButton(root, text="Install Toolboxes", command=install_data, font=("Arial", 14), width=200, height=40, corner_radius=10)
install_toolboxes.place(x=400, y=450)

root.mainloop()
