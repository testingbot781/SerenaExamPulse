from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Serena Channel", url="https://t.me/serenaunzipbot")],
        [InlineKeyboardButton("👤 Owner Contact", url="https://t.me/technicalserena")]
    ])

def exam_apply_button(link):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📝 Apply Now", url=link)]
    ])
