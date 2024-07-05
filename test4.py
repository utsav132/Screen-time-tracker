# my test
import win32gui,time,threading,wmi

title = ""

def main():
    global title
    w = wmi.WMI()
    watcher = w.Win32_PowerManagementEvent.watch_for("modification")

    while True:
        try:
            event = watcher()
            if event.EventType == 7:  # System resume from sleep
                title="Opened"
                print("Opened")
            elif event.EventType == 4:  # System going to sleep
                title = "Closed"
                print("Closed")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

t = threading.Thread(target=main)
t.start()
t.join()
while True:
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    if not title:
        title = 'Desktop'
    print(title)
    time.sleep(5)


# time - window
# time - window