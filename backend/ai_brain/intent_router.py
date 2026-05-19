def detect_intent(command):

    command = command.lower()

    # LOCAL AUTOMATION

    local_keywords = [

        "open",
        "close",
        "launch",
        "start",
        "shutdown"

    ]

    for keyword in local_keywords:

        if keyword in command:

            return "automation"

    # MEMORY

    memory_keywords = [

        "remember",
        "i like",
        "i love",
        "my name is",
        "what do i like"

    ]

    for keyword in memory_keywords:

        if keyword in command:

            return "memory"

    # VISION

    vision_keywords = [

        "camera",
        "vision",
        "look",
        "see"

    ]

    for keyword in vision_keywords:

        if keyword in command:

            return "vision"

    # DEFAULT

    return "ai"