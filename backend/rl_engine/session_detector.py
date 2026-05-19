from backend.config import AI_NAME


def detect_session(active_window):

    window = active_window.lower()

    if (
        "visual studio code" in window
        or "pycharm" in window
        or "github" in window
    ):

        return "Coding Session"

    elif (
        "youtube" in window
        or "netflix" in window
        or "spotify" in window
    ):

        return "Entertainment Session"

    elif (
        "chatgpt" in window
        or "ollama" in window
        or AI_NAME.lower() in window
    ):

        return "AI Development Session"

    elif (
        "leetcode" in window
        or "geeksforgeeks" in window
    ):

        return "Study Session"

    return "General Usage"