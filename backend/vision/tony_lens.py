import cv2

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow(
        "TONY Lens Intelligence",
        annotated_frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()