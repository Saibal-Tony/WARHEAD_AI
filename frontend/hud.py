import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt6.QtCore import (
    Qt,
    QTimer
)

from widgets.ai_core import (
    AICore
)

from widgets.system_panel import (
    SystemPanel
)

from widgets.chat_panel import (
    ChatPanel
)

import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from backend.brain.state import (
    state
)

class TonyHUD(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "TONY OS"
        )

        self.setGeometry(
            100,
            100,
            1200,
            700
        )

        self.setStyleSheet(
            """
            background-color:
            rgb(5, 10, 20);
            """
        )

        main_layout = QHBoxLayout()

        # ---------------- LEFT CHAT ----------------

        self.chat_panel = ChatPanel()

        main_layout.addWidget(
            self.chat_panel
        )

        # ---------------- CENTER CORE ----------------

        center_layout = QVBoxLayout()

        center_layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.ai_core = AICore()

        center_layout.addWidget(
            self.ai_core
        )

        main_layout.addLayout(
            center_layout
        )

        # ---------------- RIGHT SYSTEM ----------------

        self.system_panel = SystemPanel()

        main_layout.addWidget(
            self.system_panel
        )

        self.setLayout(
            main_layout
        )

        # TEST LOGS

        self.chat_panel.add_message(
            "TONY initialized..."
        )

        self.chat_panel.add_message(
            "Vision system online"
        )

        self.chat_panel.add_message(
            "Memory engine connected"
        )

        self.chat_timer = QTimer()

        self.chat_timer.timeout.connect(
            self.update_logs
        )

        self.chat_timer.start(500)

        self.last_log_count = 0

    def update_logs(self):

        logs = state.logs

        if len(logs) > self.last_log_count:

            new_logs = logs[
                self.last_log_count:
            ]

            for log in new_logs:

                self.chat_panel.add_message(
                    log
                )

            self.last_log_count = len(logs)

# ---------------- MAIN ----------------

app = QApplication(sys.argv)

window = TonyHUD()

window.show()

sys.exit(app.exec())