import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 170)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"WARHEAD: {text}")

    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)

        print(f"You: {command}")

        return command.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak("Network error")

        return ""