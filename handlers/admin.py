from pyrogram import filters
from bot.config import ADMIN_ID
from bot.database import db

def register(app):
    @app.on_message(filters.command("status") & filters.user(ADMIN_ID))
    async def status(_, m):
        users = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        await m.reply(f"📊 Bot Status\n\n👥 Total Users: {users}")
