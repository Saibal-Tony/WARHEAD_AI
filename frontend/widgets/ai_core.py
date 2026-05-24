from PyQt6.QtWidgets import QWidget

from PyQt6.QtCore import (
    QTimer,
    Qt
)

from PyQt6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QFont
)

from math import (
    cos,
    sin,
    radians
)

class AICore(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(
            400,
            400
        )

        self.rotation = 0

        self.pulse = 0

        self.pulse_direction = 1

        # ---------------- TIMER ----------------

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animate
        )

        self.timer.start(30)

    # ---------------- ANIMATION ----------------

    def animate(self):

        self.rotation += 2

        if self.rotation >= 360:

            self.rotation = 0

        self.pulse += (
            self.pulse_direction * 3
        )

        if self.pulse >= 100:

            self.pulse_direction = -1

        elif self.pulse <= 20:

            self.pulse_direction = 1

        self.update()

    # ---------------- PAINT ----------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        width = self.width()

        height = self.height()

        center_x = width // 2

        center_y = height // 2

        # BACKGROUND

        painter.fillRect(
            self.rect(),
            QColor(0, 0, 0, 0)
        )

        # ---------------- OUTER RING ----------------

        outer_radius = 140

        pen = QPen(
            QColor(
                0,
                255,
                255,
                180
            )
        )

        pen.setWidth(4)

        painter.setPen(pen)

        painter.drawEllipse(
            center_x - outer_radius,
            center_y - outer_radius,
            outer_radius * 2,
            outer_radius * 2
        )

        # ---------------- MIDDLE RING ----------------

        middle_radius = 100

        middle_pen = QPen(
            QColor(
                0,
                180,
                255,
                180
            )
        )

        middle_pen.setWidth(3)

        painter.setPen(middle_pen)

        painter.drawEllipse(
            center_x - middle_radius,
            center_y - middle_radius,
            middle_radius * 2,
            middle_radius * 2
        )

        # ---------------- INNER CORE ----------------

        inner_radius = 45 + self.pulse

        painter.setBrush(
            QColor(
                0,
                255,
                255,
                80
            )
        )

        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            center_x - inner_radius,
            center_y - inner_radius,
            inner_radius * 2,
            inner_radius * 2
        )

        # ---------------- ROTATING NODE ----------------

        angle = radians(
            self.rotation
        )

        node_x = int(
            center_x +
            cos(angle) * outer_radius
        )

        node_y = int(
            center_y +
            sin(angle) * outer_radius
        )

        painter.setBrush(
            QColor(
                0,
                255,
                255
            )
        )

        painter.drawEllipse(
            node_x - 10,
            node_y - 10,
            20,
            20
        )

        # ---------------- TEXT ----------------

        painter.setPen(
            QColor(
                255,
                255,
                255
            )
        )

        painter.setFont(
            QFont(
                "Segoe UI",
                24
            )
        )

        painter.drawText(
            center_x - 35,
            center_y + 10,
            "TONY"
        )