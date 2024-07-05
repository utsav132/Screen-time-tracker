import wmi
import time
from datetime import datetime,date
import win32gui,win32process,psutil
import threading

def get_active_window_process_name():
    try:
        pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
        return psutil.Process(pid[-1]).name()
    except:
        return "Unknown"

def is_on_desktop():
    active_window = get_active_window_process_name().lower()
    return active_window in ["explorer.exe",]# "shellexperiencehost.exe"]

def log_event(event_type,date):
    current_time = datetime.now()
    current_time = current_time.strftime('%H:%M:%S')
    month = date.strftime("%B")
    year = date.year
    #path = f"Data\\{year}-{month}\\{date}.txt"
    path = f"Data\\{date}.txt"
    with open(path, "a") as log_file:
        log_file.write(f"{current_time} -> {event_type}\n")


def focus_window():
    today = date.today()
    old_title = ""
    while True:
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        if not title:
            if is_on_desktop():
                title = "Desktop"
            else:
                continue
        if old_title != title:
            log_event(title,today)
            old_title=title
        time.sleep(1)

def main():
    today = date.today()
    current_time = datetime.now()
    current_time = current_time.strftime('%H:%M:%S')

    w = wmi.WMI()
    watcher = w.Win32_PowerManagementEvent.watch_for("modification")

    threading.Thread(target=focus_window).start()

    while True:
        try:
            event = watcher()
            if event.EventType == 7:  # System resume from sleep
                log_event("Opened",today)
            elif event.EventType == 4:  # System going to sleep
                log_event("Closed",today)
            

        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)




if __name__ == '__main__':
	main()
