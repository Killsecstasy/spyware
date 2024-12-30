import pyautogui
import time

def capture_screenshot(interval):
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f'screenshot_{time.strftime("%Y%m%d_%H%M%S")}.png')
        time.sleep(interval)

if __name__ == "__main__":
    interval = int(input("Enter the interval in seconds between screenshots: "))
    capture_screenshot(interval)