import psutil
import time
import json
from datetime import datetime

USEFUL_KEYWORDS = [
    "chrome",
    "code",
    "spotify",
    "discord",
    "steam",
    "obs",
    "python",
    "ollama",
    "edge",
    "vlc",
]

MEMORY_FILE = "rl_engine/behavior_memory.json"

def get_running_apps():

    apps = []

    for process in psutil.process_iter(['name']):

        try:

            app_name = process.info['name']

            if app_name:

                lower_name = app_name.lower()

                for keyword in USEFUL_KEYWORDS:

                    if keyword in lower_name:

                        apps.append(app_name)

                        break

        except:
            pass

    return sorted(list(set(apps)))

def save_behavior(apps):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = {
        "time": timestamp,
        "apps": apps
    }

    try:

        with open(MEMORY_FILE, "r") as file:

            data = json.load(file)

    except:

        data = []

    data.append(log_entry)

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)

def monitor_behavior():

    while True:

        running_apps = get_running_apps()

        print("\n=== ACTIVE USER APPS ===\n")

        for app in running_apps:

            print(app)

        save_behavior(running_apps)

        print("\nBehavior saved.\n")

        time.sleep(15)