import pyperclip
import time

def monitor_clipboard():
    while True:
        current_clipboard = pyperclip.paste()
        print(f"Clipboard content: {current_clipboard}")
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_clipboard()