from voice.voice_engine import speak, listen
from automation.command_engine import execute_command
from ai_brain.chatbot import get_ai_response

WAKE_WORD = "warhead"

speak("WARHEAD initialized and online")

while True:

    command = listen()

    if command == "":
        continue

    if WAKE_WORD in command:

        command = command.replace(WAKE_WORD, "").strip()

        if command == "":
            speak("Yes Saibal")
            continue

        if "exit" in command:
            speak("Shutting down")
            break

        handled = execute_command(command, speak)

        if handled:
            continue

        speak("Thinking")

        response = get_ai_response(command)

        print(f"WARHEAD AI: {response}")

        speak(response)