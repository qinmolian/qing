import os

home_path = os.path.expanduser("~")  # Get the home path (e.g., C:\Users\Username)
toolboxes_path = None

# Loop through the versions from 10.8 to 10.1
for version in range(10, 0, -1):  # This will go from 10.8 to 10.1
    desktop_version = f"Desktop10.{version}"
    potential_path = os.path.join(home_path, "AppData", "Roaming", "ESRI", desktop_version, "ArcToolbox", "My Toolboxes")
    
    if os.path.exists(potential_path):
        toolboxes_path = potential_path
        print(f"Found My Toolboxes at: {toolboxes_path}")
        break  # Exit the loop once the folder is found

if toolboxes_path is None:
    print("My Toolboxes folder not found for any version.")
