import cv2

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import (
    QTimer,
    Qt
)

from PyQt6.QtGui import (
    QImage,
    QPixmap,
    QFont
)

class VisionPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(
            400,
            300
        )

        layout = QVBoxLayout()

        title = QLabel(
            "AI VISION"
        )

        title.setFont(
            QFont(
                "Segoe UI",
                18
            )
        )

        title.setStyleSheet(
            """
            color: cyan;
            font-weight: bold;
            """
        )

        self.video_label = QLabel()

        self.video_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.video_label.setStyleSheet(
            """
            border:
            1px solid cyan;

            border-radius: 15px;

            background-color:
            rgba(0, 0, 0, 180);
            """
        )

        layout.addWidget(title)

        layout.addWidget(
            self.video_label
        )

        self.setLayout(layout)

        # CAMERA

        self.camera = cv2.VideoCapture(0)

        # TIMER

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_frame
        )

        self.timer.start(30)

    # ---------------- FRAME ----------------

    def update_frame(self):

        success, frame = self.camera.read()

        if not success:
            return

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        height, width, channel = rgb.shape

        bytes_per_line = (
            channel * width
        )

        image = QImage(
            rgb.data,
            width,
            height,
            bytes_per_line,
            QImage.Format.Format_RGB888
        )

        pixmap = QPixmap.fromImage(
            image
        )

        self.video_label.setPixmap(
            pixmap.scaled(
                self.video_label.width(),
                self.video_label.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            )
        )

    # ---------------- CLEANUP ----------------

    def closeEvent(self, event):

        self.camera.release()

        event.accept()