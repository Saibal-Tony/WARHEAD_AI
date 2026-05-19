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

import cv2
import mediapipe as mp
import speech_recognition as sr
import threading
import time
from config import AI_NAME
from brain.core import state

# ---------------- VOICE ----------------

# activate_gesture_mode = False

def listen_for_tony():

    recognizer = sr.Recognizer()

    microphone = sr.Microphone()

    # ONE-TIME CALIBRATION

    with microphone as source:

        print("\nCalibrating microphone...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        print("Microphone calibrated.")

    while True:

        with microphone as source:

            print(f"\nListening for {AI_NAME}...")

            try:

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            except sr.WaitTimeoutError:

                continue

        try:

            text = recognizer.recognize_google(
                audio
            ).lower()

            print(f"You Said: {text}")

            if AI_NAME.lower() in text:

                state.gesture_mode = True

                print(
                    f"\n{AI_NAME} Gesture Mode Activated"
                )

        except:
            pass

# ---------------- VISION ----------------

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

camera = cv2.VideoCapture(0)

TIP_IDS = [4, 8, 12, 16, 20]

last_gesture = -1
last_action_time = 0

COOLDOWN = 3

# ---------------- THREAD ----------------

voice_thread = threading.Thread(
    target=listen_for_tony
)

voice_thread.daemon = True

voice_thread.start()

# ---------------- MAIN LOOP ----------------

while True:

    current_time = time.time()

    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = hands.process(rgb_frame)

    status = (
        f"{AI_NAME} ACTIVE"
        if state.gesture_mode
        else f"{AI_NAME} WAITING"
    )

    cv2.putText(
        frame,
        f"Gesture Mode: {status}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    if (
        state.gesture_mode
        and results.multi_hand_landmarks
    ):

        for hand_landmarks in (
            results.multi_hand_landmarks
        ):

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            fingers = []

            # Thumb

            if (
                landmarks[TIP_IDS[0]].x <
                landmarks[TIP_IDS[0] - 1].x
            ):

                fingers.append(1)

            else:

                fingers.append(0)

            # Other fingers

            for tip_id in TIP_IDS[1:]:

                if (
                    landmarks[tip_id].y <
                    landmarks[tip_id - 2].y
                ):

                    fingers.append(1)

                else:

                    fingers.append(0)

            total_fingers = fingers.count(1)

            cv2.putText(
                frame,
                f"Fingers: {total_fingers}",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            if (
                total_fingers != last_gesture
                and current_time - last_action_time > COOLDOWN
            ):

                last_gesture = total_fingers
                last_action_time = current_time

                print(
                    f"Gesture Detected: {total_fingers}"
                )

                # COMMANDS

                if total_fingers == 1:

                    os.system("start chrome")

                elif total_fingers == 2:

                    os.system("code")

                elif total_fingers == 5:

                    print(f"Stopping {AI_NAME}")

                    camera.release()

                    cv2.destroyAllWindows()

                    exit()

                state.gesture_mode = False

    else:

        if current_time - last_action_time > 1:

            last_gesture = -1

    cv2.imshow(
        f"{AI_NAME} Fusion Intelligence",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()