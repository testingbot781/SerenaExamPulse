from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import start, help, settings, profile, admin
from bot.scheduler import init_scheduler

app = Client(
    "SerenaExamPulse",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

# Register Handlers
start.register(app)
help.register(app)
settings.register(app)
profile.register(app)
admin.register(app)

# Start scheduler AFTER the app starts
@app.on_event("start")
async def on_start(_, __):
    init_scheduler(app)

app.run()
