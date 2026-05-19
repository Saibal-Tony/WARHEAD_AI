import pygetwindow as gw
import time

from rl_engine.session_detector import (
    detect_session
)

def get_active_window():

    try:

        window = gw.getActiveWindow()

        if window:

            return window.title

    except:
        pass

    return "Unknown"

def monitor_active_window():

    while True:

        active_window = get_active_window()

        session = detect_session(
            active_window
        )

        print(f"\nActive Window:\n{active_window}")

        print(f"\nDetected Session:\n{session}")

        time.sleep(5)