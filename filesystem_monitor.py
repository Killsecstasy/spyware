import os
import time

def monitor_directory(directory):
    while True:
        for root, dirs, files in os.walk(directory):
            for name in files:
                print(f"File changed: {os.path.join(root, name)}")
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    directory = input("Enter the directory to monitor: ")
    monitor_directory(directory)