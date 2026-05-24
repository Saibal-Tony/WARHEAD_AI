import psutil

from datetime import datetime

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import QTimer

from PyQt6.QtGui import (
    QFont
)

class SystemPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumWidth(250)

        layout = QVBoxLayout()

        self.title = QLabel(
            "SYSTEM"
        )

        self.title.setFont(
            QFont("Segoe UI", 18)
        )

        self.title.setStyleSheet(
            """
            color: cyan;
            font-weight: bold;
            """
        )

        self.info = QLabel()

        self.info.setFont(
            QFont("Consolas", 12)
        )

        self.info.setStyleSheet(
            """
            color: white;
            """
        )

        layout.addWidget(
            self.title
        )

        layout.addWidget(
            self.info
        )

        self.setLayout(layout)

        self.setStyleSheet(
            """
            background-color:
            rgba(0, 255, 255, 20);

            border:
            1px solid cyan;

            border-radius: 15px;
            """
        )

        # TIMER

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_info
        )

        self.timer.start(1000)

        self.update_info()

    def update_info(self):

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

        self.info.setText(
            f"""
CPU Usage : {cpu}%

RAM Usage : {ram}%

Battery   : {battery_percent}%

Time      : {current_time}
            """
        )