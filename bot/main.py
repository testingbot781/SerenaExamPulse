import subprocess
import sys
import os
from flask import Flask
from threading import Thread

# -----------------------------
# Flask server (Render requirement)
# -----------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Serena Exam Pulse bot is running (Web Service Mode)."

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)


# -----------------------------
# Pyrogram bot as subprocess
# -----------------------------
def run_pyrogram():
    print(">>> Starting Pyrogram subprocess...")

    project_root = os.path.dirname(os.path.abspath(__file__))

    subprocess.Popen(
        [
            sys.executable,   # correct Python interpreter
            "-m",
            "bot.worker"
        ],
        cwd=os.path.dirname(project_root),  # ensures module path correct
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(">>> Pyrogram subprocess launched ✔")


# -----------------------------
# Start Both Services
# -----------------------------
if __name__ == "__main__":
    # Start Flask
    Thread(target=run_flask, daemon=True).start()

    # Start Bot
    Thread(target=run_pyrogram, daemon=True).start()

    # Keep main process alive
    while True:
        pass
