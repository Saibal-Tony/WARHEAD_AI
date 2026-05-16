import webbrowser
import os
from datetime import datetime

def execute_command(command, speak):

    if "open chrome" in command:
        speak("Opening Chrome")

        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        os.startfile(chrome_path)

    elif "open youtube" in command:
        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")

        speak(f"The time is {current_time}")

    elif "open vscode" in command:
        speak("Opening VS Code")

        code_path = os.path.expandvars(
            r"%LocalAppData%\Programs\Microsoft VS Code\Code.exe"
        )

        os.startfile(code_path)

    elif "shutdown" in command:
        speak("Shutting down system")

        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting system")

        os.system("shutdown /r /t 5")

    else:
        return False

    return True