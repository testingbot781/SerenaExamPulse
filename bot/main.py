import subprocess
from flask import Flask
from threading import Thread

# -----------------------------
# Flask server for Render
# -----------------------------
app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "Serena Exam Pulse is running (Web Service Mode)."

def run_flask():
    app_flask.run(host="0.0.0.0", port=10000)


# -----------------------------
# Pyrogram bot as SUBPROCESS
# -----------------------------
def run_pyrogram():
    # This will start your bot in a SEPARATE OS PROCESS
    subprocess.Popen(
        ["python", "-m", "bot.worker"],  # worker.py file will run Pyrogram bot
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


# -----------------------------
# Start both services
# -----------------------------
if __name__ == "__main__":
    # Start Flask (Render requirement)
    Thread(target=run_flask, daemon=True).start()

    # Start Pyrogram bot (Separate process — very important)
    Thread(target=run_pyrogram, daemon=True).start()

    # Keep main process alive forever
    while True:
        pass

