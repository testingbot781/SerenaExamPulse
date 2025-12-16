import asyncio
from pyrogram import Client, idle
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

async def main():
    await app.start()          # Pyrogram start
    init_scheduler(app)         # Scheduler start (SAFE)
    print("Bot & Scheduler Started Successfully")
    await idle()                # Keep running
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
