from pyrogram import filters

def register(app):
    @app.on_message(filters.command("settings"))
    async def settings(_, m):
        await m.reply(
            "⚙️ **Settings Panel**\n\n"
            "Choose what you want to update:",
        )
