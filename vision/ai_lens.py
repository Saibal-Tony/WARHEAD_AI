from ultralytics import YOLO

import cv2

# ---------------- MODEL ----------------

model = YOLO(
    "yolov8n.pt"
)

# ---------------- CAMERA ----------------

camera = cv2.VideoCapture(0)

# ---------------- LOOP ----------------

while True:

    success, frame = camera.read()

    if not success:
        break

    # ---------------- DETECTION ----------------

    results = model(frame)

    annotated_frame = results[0].plot()

    # ---------------- OBJECT LIST ----------------

    detected_objects = []

    for box in results[0].boxes:

        class_id = int(box.cls[0])

        label = model.names[class_id]

        detected_objects.append(label)

    unique_objects = list(
        set(detected_objects)
    )

    # ---------------- DISPLAY ----------------

    y = 30

    for obj in unique_objects:

        cv2.putText(
            annotated_frame,
            f"Detected: {obj}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        y += 30

    cv2.imshow(
        "TONY AI LENS",
        annotated_frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# ---------------- CLEANUP ----------------

camera.release()

cv2.destroyAllWindows()