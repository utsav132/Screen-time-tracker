#normal window no install
import win32gui,time
while True:
    time.sleep(5)
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    print(title)

# time - window
# time - window