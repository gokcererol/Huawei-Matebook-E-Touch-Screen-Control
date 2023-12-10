import subprocess
import pystray
from pystray import MenuItem as item
from PIL import Image
import os


# Function to handle menu actions
def on_action_selected(action):
    if action == 'DisableTouchScreen':
        subprocess.run(["powershell", "-File", r"C:\Users\gokcer\Documents\GitHub\OpenCV\Disable.ps1"], shell=True)
    elif action == 'EnableTouchScreen':
        subprocess.run(["powershell", "-File", r"C:\Users\gokcer\Documents\GitHub\OpenCV\Enable.ps1"], shell=True)
    elif action == 'Quit':
        icon.stop()
    else:
        print('ERROR: Invalid action')

# Create the tray icon
def create_tray_icon():
    # Load your icon
    icon_image = Image.open(r"C:\Users\gokcer\Documents\GitHub\OpenCV\Device-Touch-Screen-256.ico")

    # Create menu items
    menu = (item('Disable Touchscreen', lambda: on_action_selected("DisableTouchScreen")),
            item('Enable Touchscreen', lambda: on_action_selected("EnableTouchScreen")),
            item('Quit', lambda: on_action_selected("Quit")))

    # Create the tray icon
    global icon
    icon = pystray.Icon("Touchscreen", icon=icon_image, title="Touchscreen Control created by Ciel", menu=menu)

    # Run the application
    icon.run()

if __name__ == "__main__":
    create_tray_icon()
