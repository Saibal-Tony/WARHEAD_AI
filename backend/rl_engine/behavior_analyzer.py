import json
from collections import Counter

MEMORY_FILE = "rl_engine/behavior_memory.json"

def analyze_behavior():

    try:

        with open(MEMORY_FILE, "r") as file:

            data = json.load(file)

    except:

        print("No behavior data found.")

        return

    app_counter = Counter()

    for entry in data:

        apps = entry["apps"]

        for app in apps:

            app_counter[app] += 1

    print("\n=== MOST USED APPS ===\n")

    for app, count in app_counter.most_common():

        print(f"{app} -> {count} times")