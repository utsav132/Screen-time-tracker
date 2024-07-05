# normal window and website title on chrome no install
import win32gui
import win32process
import psutil
import time
import re

def get_active_window_info():
    try:
        window = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(window)
        process = psutil.Process(pid[-1])
        process_name = process.name().lower()
        window_title = win32gui.GetWindowText(window)
        return process_name, window_title
    except:
        return "Unknown", "Unknown"

def extract_website_from_chrome_title(title):
    # Remove " - Google Chrome" from the end
    title = re.sub(r" - Google Chrome$", "", title)
    
    # Common patterns for website titles
    patterns = [
        r"^(.*?) - .*$",  # "YouTube - ..."
        r"^(.*?)$",       # "YouTube"
    ]
    
    for pattern in patterns:
        match = re.match(pattern, title)
        if match:
            return match.group(1)
    
    return "Unknown website"

def main():
    while True:
        process_name, window_title = get_active_window_info()
        
        if "chrome" in process_name:
            website = extract_website_from_chrome_title(window_title)
            print(process_name)
            print(f"User is browsing: {website}")
        elif process_name in ["explorer.exe", "shellexperiencehost.exe"]:
            print("User is on desktop")
        else:
            print(f"User is using: {process_name}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()