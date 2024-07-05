# laptop opne or close no install
import wmi
import time
from datetime import datetime

def log_event(event_type):
    print(event_type)
    # with open("screen_time_log.txt", "a") as log_file:
    #     log_file.write(f"{event_type}: {datetime.now()}\n")

def main():
    w = wmi.WMI()
    watcher = w.Win32_PowerManagementEvent.watch_for("modification")

    while True:
        try:
            event = watcher()
            if event.EventType == 7:  # System resume from sleep
                log_event("Opened")
            elif event.EventType == 4:  # System going to sleep
                log_event("Closed")
            
            
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    main()
