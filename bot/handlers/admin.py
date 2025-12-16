from pyrogram import filters
from bot.config import ADMIN_ID
from bot.database import db

def register(app):

    @app.on_message(filters.command("status") & filters.user(ADMIN_ID))
    async def status(_, m):
        total = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        blocked = db.execute("SELECT COUNT(*) FROM blocked").fetchone()[0]
        await m.reply(f"📊 **Bot Status**\n\n👥 Total Users: {total}\n🚫 Blocked: {blocked}")

    @app.on_message(filters.command("users") & filters.user(ADMIN_ID))
    async def users(_, m):
        users = db.execute("SELECT user_id FROM users").fetchall()
        msg = "👤 **Registered Users:**\n\n"
        msg += "\n".join([str(u[0]) for u in users])
        await m.reply(msg)
