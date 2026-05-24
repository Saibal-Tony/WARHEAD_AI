class TonyState:

    def __init__(self):

        self.logs = []

        self.current_status = (
            "ONLINE"
        )

        self.is_listening = False

        self.is_speaking = False

    # ---------------- LOGS ----------------

    def add_log(self, message):

        self.logs.append(message)

        print(message)

        # LIMIT SIZE

        if len(self.logs) > 100:

            self.logs.pop(0)

# ---------------- GLOBAL ----------------

state = TonyState()