import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from voice.voice_engine import speak, listen

from config import AI_NAME

from automation.command_engine import execute_command

from ai_brain.chatbot import get_ai_response

from memory.memory_engine import (
    remember,
    recall
)

from ai_brain.intent_router import (
    detect_intent
)

WAKE_WORD = AI_NAME.lower()

speak(f"{AI_NAME} initialized and online")

while True:

    command = listen()

    if command == "":
        continue

    command = command.lower()

    intent = detect_intent(command)

    print(f"Intent: {intent}")

    if WAKE_WORD in command:

        command = command.replace(WAKE_WORD, "").strip()

        if command == "":
            speak("Yes Saibal")
            continue

        if "exit" in command:
            speak("Shutting down")
            break

        # ---------------- AUTOMATION ----------------

        if intent == "automation":

            handled = execute_command(
                command,
                speak
            )

            if handled:
                continue

        # ---------------- MEMORY ----------------

        elif intent == "memory":

            if "what do i love" in command:

                favorite = recall("favorite")

                if favorite:

                    speak(f"You love {favorite}")

                else:

                    speak("I do not know yet")

                continue

            if "i love" in command:

                thing = command.replace(
                    "i love",
                    ""
                ).strip()

                remember(
                    "favorite",
                    thing
                )

                speak(
                    f"I will remember that "
                    f"you love {thing}"
                )

                continue

        # ---------------- VISION ----------------

        elif intent == "vision":

            speak("Vision system ready")

            continue

        # ---------------- AI ----------------

        print(f"{AI_NAME} is thinking...")

        response = get_ai_response(command)

        print(f"{AI_NAME}: {response}")

        speak(response)

        if "what do i love" in command:

            favorite = get_memory("favorite")

            if favorite:

                speak(f"You love {favorite}")

            else:

                speak("I do not know yet")

            continue

        if "i love" in command:

            thing = command.replace("i love", "").strip()

            save_memory("favorite", thing)

            speak(f"I will remember that you love {thing}")

            continue

        print(f"{AI_NAME} is thinking...")

        response = get_ai_response(command)

        print(f"{AI_NAME}: {response}")

        speak(response)