from PyQt6.QtWidgets import (
    QWidget,
    QTextEdit,
    QVBoxLayout,
    QLabel
)

from PyQt6.QtGui import (
    QFont
)

class ChatPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumWidth(300)

        layout = QVBoxLayout()

        title = QLabel(
            "TONY LOGS"
        )

        title.setFont(
            QFont("Segoe UI", 18)
        )

        title.setStyleSheet(
            """
            color: cyan;
            font-weight: bold;
            """
        )

        self.chat_box = QTextEdit()

        self.chat_box.setReadOnly(True)

        self.chat_box.setFont(
            QFont("Consolas", 11)
        )

        self.chat_box.setStyleSheet(
            """
            background-color:
            rgba(0, 0, 0, 180);

            color: lime;

            border:
            1px solid cyan;

            border-radius: 10px;
            """
        )

        layout.addWidget(title)

        layout.addWidget(
            self.chat_box
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

    def add_message(self, text):

        self.chat_box.append(text)