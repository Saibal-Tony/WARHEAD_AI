from backend.config import AI_NAME
import face_recognition
import cv2

known_image = face_recognition.load_image_file(
    "vision/faces/saibal.jpg"
)

known_encoding = face_recognition.face_encodings(
    known_image
)[0]

camera = cv2.VideoCapture(0)

while True:

    success, frame = camera.read()

    if not success:
        break

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    face_locations = face_recognition.face_locations(
        rgb_frame
    )

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            [known_encoding],
            face_encoding
        )

        name = "Unknown"

        if True in matches:
            name = "Saibal"

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        f"{AI_NAME} Face Recognition",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()