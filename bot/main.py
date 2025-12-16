import asyncio
from pyrogram import Client, idle
from flask import Flask
from threading import Thread

from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler

# ------------------------------
# Flask mini server for Render
# ------------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Serena Exam Pulse is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=10000)

# ------------------------------
# Pyrogram bot
# ------------------------------
app = Client(
    "SerenaExamPulse",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

start.register(app)
help.register(app)
settings.register(app)
profile.register(app)
admin.register(app)

async def main():
    await app.start()
    init_scheduler(app)
    print("Bot + Scheduler started 🚀")
    await idle()
    await app.stop()

if __name__ == "__main__":
    # Start Flask server on a separate thread
    Thread(target=run_flask).start()
    
    # Start bot inside async loop
    asyncio.run(main())

