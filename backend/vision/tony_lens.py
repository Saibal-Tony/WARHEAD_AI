import cv2
import time

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

previous_time = 0

while True:

    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    detections = results[0].boxes

    object_count = 0

    # ---------------- HUD PANEL ----------------

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (0, 0),
        (350, 120),
        (20, 20, 20),
        -1
    )

    alpha = 0.6

    frame = cv2.addWeighted(
        overlay,
        alpha,
        frame,
        1 - alpha,
        0
    )

    # ---------------- TITLE ----------------

    cv2.putText(
        frame,
        "TONY LENS AI",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Vision Intelligence Active",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # ---------------- OBJECTS ----------------

    for box in detections:

        x1, y1, x2, y2 = map(
            int,
            box.xyxy[0]
        )

        confidence = float(box.conf[0])

        class_id = int(box.cls[0])

        class_name = model.names[class_id]

        object_count += 1

        # BOX

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 255),
            2
        )

        # LABEL

        label = (
            f"{class_name.upper()} "
            f"{int(confidence * 100)}%"
        )

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

    # ---------------- STATUS ----------------

    cv2.putText(
        frame,
        f"Objects Detected: {object_count}",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 135),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    # ---------------- DISPLAY ----------------

    cv2.imshow(
        "TONY Cinematic Vision",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()