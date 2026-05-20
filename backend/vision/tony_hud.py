import random

import sys
from turtle import pen

import psutil
from datetime import datetime

from math import cos, sin, radians

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from PyQt6.QtGui import (
    QFont,
    QPainter,
    QColor,
    QPen
)

class TonyHUD(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "TONY HUD"
        )

        self.setGeometry(
            100,
            100,
            700,
            400
        )

        # TRANSPARENT WINDOW

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

        self.setWindowFlags(

            Qt.WindowType.FramelessWindowHint |

            Qt.WindowType.WindowStaysOnTopHint
        )

        # MAIN LAYOUT

        layout = QVBoxLayout()

        layout.setContentsMargins(
            30,
            30,
            30,
            30
        )

        layout.setSpacing(15)

        # TITLE

        self.title = QLabel(
            "TONY AI"
        )

        self.title.setFont(
            QFont("Segoe UI", 34)
        )

        self.title.setStyleSheet(
            """
            color: cyan;
            font-weight: bold;
            """
        )

        # STATUS

        self.status = QLabel(
            "SYSTEM ONLINE"
        )

        self.status.setFont(
            QFont("Consolas", 16)
        )

        self.status.setStyleSheet(
            """
            color: white;
            """
        )

        # FPS / INFO

        self.info = QLabel(
            "Vision Active"
        )

        self.system_info = QLabel()

        self.system_info.setFont(
            QFont("Consolas", 11)
        )

        self.system_info.setStyleSheet(
            """
            color: cyan;
            """
        )

        self.clock = QLabel()

        self.clock.setFont(
            QFont("Segoe UI", 16)
        )

        self.clock.setStyleSheet(
            """
            color: white;
            font-weight: bold;
            """
        )

        self.info.setFont(
            QFont("Consolas", 12)
        )

        self.info.setStyleSheet(
            """
            color: lime;
            """
        )

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.status
        )

        layout.addWidget(
            self.info
        )

        layout.addWidget(
            self.system_info
        )

        layout.addWidget(
            self.clock
        )

        self.setLayout(layout)

        # GLASSMORPHISM STYLE

        self.setStyleSheet(
            """
            QWidget {

                background-color:
                rgba(10, 10, 20, 220);

                border-radius: 25px;
            }

            QLabel {

                background: transparent;
                border: none;
            }
            """
        )

        # ANIMATION TIMER

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.animate_status
        )

        self.timer.start(500)

        self.glow_timer = QTimer()

        self.glow_timer.timeout.connect(
            self.animate_glow
        )

        self.glow_timer.start(50)

        self.scan_timer = QTimer()

        self.scan_timer.timeout.connect(
            self.animate_scan
        )

        self.scan_timer.start(20)

        self.core_timer = QTimer()

        self.core_timer.timeout.connect(
            self.animate_core
        )

        self.core_timer.start(30)

        self.wave_timer = QTimer()

        self.wave_timer.timeout.connect(
            self.animate_wave
        )

        self.wave_timer.start(80)

        self.system_timer = QTimer()

        self.system_timer.timeout.connect(
            self.update_system_info
        )

        self.system_timer.start(1000)

        self.dot_count = 0

        self.glow = 0

        self.glow_direction = 1

        self.scan_y = 0

        self.rotation_angle = 0

        self.wave_values = [

            random.randint(10, 60)

            for _ in range(40)
        ]

    def animate_status(self):

        dots = "." * self.dot_count

        self.status.setText(
            f"SYSTEM ONLINE {dots}"
        )

        self.dot_count = (
            self.dot_count + 1
        ) % 4

    def animate_glow(self):

        self.glow += self.glow_direction * 5

        if self.glow >= 255:

            self.glow_direction = -1

        elif self.glow <= 100:

            self.glow_direction = 1

        self.title.setStyleSheet(
            f"""
            color: rgb(0, {self.glow}, 255);
            font-weight: bold;
            """
        )

    def animate_scan(self):

        self.scan_y += 3

        if self.scan_y > self.height():

            self.scan_y = 0

        self.update()
    
    def animate_core(self):

        self.rotation_angle += 2

        if self.rotation_angle >= 360:

            self.rotation_angle = 0

        self.update()

    def animate_wave(self):

        self.wave_values = [

            random.randint(10, 60)

            for _ in range(40)
        ]

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        # ---------------- AI CORE ----------------

        center_x = self.width() // 2

        center_y = self.height() // 2

        radius = 90

        # OUTER RING

        core_pen = QPen(
            QColor(0, 255, 255, 180)
        )

        core_pen.setWidth(4)

        painter.setPen(core_pen)

        painter.drawEllipse(
            center_x - radius,
            center_y - radius,
            radius * 2,
            radius * 2
        )

        # INNER RING

        inner_radius = 60

        inner_pen = QPen(
            QColor(0, 180, 255, 180)
        )

        inner_pen.setWidth(3)

        painter.setPen(inner_pen)

        painter.drawEllipse(
            center_x - inner_radius,
            center_y - inner_radius,
            inner_radius * 2,
            inner_radius * 2
        )

        # ROTATING NODE

        angle = radians(
            self.rotation_angle
        )

        node_x = int(
            center_x + cos(angle) * radius
        )

        node_y = int(
            center_y + sin(angle) * radius
        )

        painter.setBrush(
            QColor(0, 255, 255)
        )

        painter.drawEllipse(
            node_x - 8,
            node_y - 8,
            16,
            16
        )

        # CORE TEXT

        painter.setPen(
            QColor(255, 255, 255)
        )

        painter.drawText(
            center_x - 35,
            center_y + 5,
            "TONY"
        )

        # ---------------- VOICE WAVEFORM ----------------

        wave_pen = QPen(
            QColor(0, 255, 255)
        )

        wave_pen.setWidth(3)

        painter.setPen(wave_pen)

        start_x = 80

        base_y = self.height() - 80

        spacing = 12

        for i, value in enumerate(
            self.wave_values
        ):

            x = start_x + i * spacing

            painter.drawLine(
                x,
                base_y - value,
                x,
                base_y + value
            )

        # SCAN LINE

        pen = QPen(
            QColor(0, 255, 255, 180)
        )

        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawLine(
            20,
            self.scan_y,
            self.width() - 20,
            self.scan_y
        )

        # CORNER HUD LINES

        corner_pen = QPen(
            QColor(0, 255, 255)
        )

        corner_pen.setWidth(3)

        painter.setPen(corner_pen)

        # TOP LEFT

        painter.drawLine(0, 0, 50, 0)
        painter.drawLine(0, 0, 0, 50)

        # TOP RIGHT

        painter.drawLine(
            self.width(),
            0,
            self.width() - 50,
            0
        )

        painter.drawLine(
            self.width() - 1,
            0,
            self.width() - 1,
            50
        )

        # BOTTOM LEFT

        painter.drawLine(
            0,
            self.height(),
            50,
            self.height()
        )

        painter.drawLine(
            0,
            self.height(),
            0,
            self.height() - 50
        )   

        # BOTTOM RIGHT

        painter.drawLine(
            self.width(),
            self.height(),
            self.width() - 50,
            self.height()
        )

        painter.drawLine(
            self.width() - 1,
            self.height(),
            self.width() - 1,
            self.height() - 50
        )

    def update_system_info(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        battery = psutil.sensors_battery()

        battery_percent = (
            battery.percent
            if battery
            else "N/A"
        )

        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.system_info.setText(

            f"""
    CPU Usage : {cpu}%
    RAM Usage : {ram}%
    Battery   : {battery_percent}%
            """
        )

        self.clock.setText(
            current_time
        )

# ---------------- MAIN ----------------

app = QApplication(sys.argv)

window = TonyHUD()

window.show()

sys.exit(app.exec())