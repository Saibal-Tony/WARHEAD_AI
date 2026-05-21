import json
import os

MEMORY_FILE = "memory/memory.json"

# ---------------- LOAD ----------------

def load_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return {}

    with open(
        MEMORY_FILE,
        "r"
    ) as file:

        return json.load(file)

# ---------------- SAVE ----------------

def save_memory(data):

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )

# ---------------- REMEMBER ----------------

def remember(category, key, value):

    memory = load_memory()

    if category not in memory:

        memory[category] = {}

    memory[category][key] = value

    save_memory(memory)

# ---------------- RECALL ----------------

def recall(category, key):

    memory = load_memory()

    if (
        category in memory
        and key in memory[category]
    ):

        return memory[category][key]

    return None

# ---------------- GET CATEGORY ----------------

def get_category(category):

    memory = load_memory()

    return memory.get(
        category,
        {}
    )