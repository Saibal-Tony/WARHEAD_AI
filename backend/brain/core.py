class TonyState:

    def __init__(self):

        self.listening = True

        self.gesture_mode = False

        self.owner_detected = False

        self.current_user = None

        self.last_command = None

state = TonyState()