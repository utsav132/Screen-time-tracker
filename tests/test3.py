# install get window, another way of getting window
import time
import pygetwindow as gw
from pywinauto import Desktop

def get_active_window_title():
    window = gw.getActiveWindow()
    if window:
        return window.title
    return None

def is_desktop_active():
    # Check if the currently active window is the desktop
    active_window_title = get_active_window_title()
    if active_window_title:
        # List of possible desktop window titles, you may need to add more depending on your system
        desktop_titles = ["Program Manager", "Desktop"]
        return active_window_title in desktop_titles
    return False

def main():
    while True:
        if is_desktop_active():
            print("User is on the desktop")
        else:
            print("User is not on the desktop")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
