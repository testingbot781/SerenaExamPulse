from pyrogram import filters
from bot.config import ADMIN_ID
from bot.database import users, blocked

def register(app):

    # 🔥 Command: /status (Admin Only)
    @app.on_message(filters.command("status") & filters.user(int(ADMIN_ID)))
    async def status(_, m):
        total_users = users.count_documents({})
        blocked_users = blocked.count_documents({})
        
        await m.reply(
            f"📊 **Bot Status**\n\n"
            f"👥 Total Users: {total_users}\n"
            f"🚫 Blocked Users: {blocked_users}\n"
        )

    # 🔥 Command: /users (Admin Only)
    @app.on_message(filters.command("users") & filters.user(int(ADMIN_ID)))
    async def show_users(_, m):

        all_users = users.find({})
        msg = "👤 **Registered Users:**\n\n"

        for u in all_users:
            msg += f"• {u.get('name', 'Unknown')} (ID: {u['user_id']})\n"

        await m.reply(msg or "No users found.")
