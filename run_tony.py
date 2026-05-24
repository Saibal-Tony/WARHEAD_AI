import threading
import subprocess
import sys

# CURRENT VENV PYTHON

PYTHON = sys.executable

# ---------------- BACKEND ----------------

def run_backend():

    subprocess.run(
        [
            PYTHON,
            "backend/main.py"
        ]
    )

# ---------------- FRONTEND ----------------

def run_frontend():

    subprocess.run(
        [
            PYTHON,
            "frontend/hud.py"
        ]
    )

# ---------------- THREADS ----------------

backend_thread = threading.Thread(
    target=run_backend
)

frontend_thread = threading.Thread(
    target=run_frontend
)

backend_thread.start()

frontend_thread.start()

backend_thread.join()

frontend_thread.join()