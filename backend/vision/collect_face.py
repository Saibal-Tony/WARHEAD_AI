from backend.config import AI_NAME
import cv2
import os

SAVE_PATH = "vision/faces"

PERSON_NAME = "saibal"

os.makedirs(SAVE_PATH, exist_ok=True)

camera = cv2.VideoCapture(0)

count = 0

while True:

    success, frame = camera.read()

    if not success:
        break

    cv2.imshow(
        f"{AI_NAME} Face Collection",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('s'):

        image_path = (
            f"{SAVE_PATH}/{PERSON_NAME}.jpg"
        )

        cv2.imwrite(image_path, frame)

        print(f"\nFace saved at:\n{image_path}")

        count += 1

    elif key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()