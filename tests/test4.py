# detect desktop no install
import win32gui
import win32process
import psutil
import time

def get_active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return psutil.Process(pid[-1]).name()
    except:
        return "Unknown"

def is_on_desktop():
    active_window = get_active_window_process_name().lower()
    print(active_window)
    return active_window in ["explorer.exe", "shellexperiencehost.exe"]

def main():
    while True:
        if is_on_desktop():
            print("User is on desktop")
        else:
            print(f"User is on: {get_active_window_process_name()}")
        time.sleep(5)

if __name__ == "__main__":
    main()