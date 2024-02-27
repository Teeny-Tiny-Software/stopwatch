import time
import sys

def start_tracking():
    active = True
    total_active_time = 0
    print("Screen time tracking started. Press Ctrl+C to stop.")

    try:
        while active:
            time.sleep(1)  # Check every second
            total_active_time += 1
            sys.stdout.write(f"\rTotal screen time: {total_active_time // 60} minutes")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print(f"\nScreen time tracking stopped. Final screen time: {total_active_time // 60} minutes")

if __name__ == "__main__":
    start_tracking()
