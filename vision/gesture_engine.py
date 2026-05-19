import cv2
import mediapipe as mp
import os
import time
from config import AI_NAME

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

camera = cv2.VideoCapture(0)

TIP_IDS = [4, 8, 12, 16, 20]

last_gesture = -1
last_action_time = 0

COOLDOWN = 3

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

    if results.multi_hand_landmarks:

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

            # Other Fingers

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

            # Gesture Cooldown

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

                    print("Opening Chrome")

                    os.system("start chrome")

                elif total_fingers == 2:

                    print("Opening VS Code")

                    os.system("code")

                elif total_fingers == 3:

                    print("Opening Notepad")

                    os.system("start notepad")

                elif total_fingers == 5:

                    print("Stopping WARHEAD")

                    camera.release()

                    cv2.destroyAllWindows()

                    exit()

    else:

        # Reset Gesture Only After Delay

        if current_time - last_action_time > 1:

            last_gesture = -1

    cv2.imshow(
        f"{AI_NAME} Gesture Intelligence",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()