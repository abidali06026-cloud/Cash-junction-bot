import telebot
from telebot import types

# --- CONFIGURATION ---
API_TOKEN = 'YOUR_BOT_TOKEN'
ADMIN_ID = YOUR_TELEGRAM_ID
# ---------------------

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    if message.from_user.id == ADMIN_ID:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('➕ Add Source')
        btn2 = types.KeyboardButton('🔍 Filter Settings')
        btn3 = types.KeyboardButton('📊 Bot Status')
        btn4 = types.KeyboardButton('⚙️ Advanced Tools')
        markup.add(btn1, btn2, btn3, btn4)
        bot.reply_to(message, "Junction System Active. Settings are now inside Telegram.", reply_markup=markup)
    else:
        bot.reply_to(message, "Only Admin can control this bot.")

@bot.message_handler(func=lambda message: True)
def handle_admin_commands(message):
    if message.from_user.id == ADMIN_ID:
        if message.text == '📊 Bot Status':
            bot.reply_to(message, "✅ System: Running 24/7\n✅ Mode: Auto-Pilot")
        elif message.text == '🔍 Filter Settings':
            bot.reply_to(message, "Configure keywords here (e.g., Binance, Code)")
    pass

print("Bot is starting...")
bot.infinity_polling()
