import telebot
from telebot import types

# --- SETTINGS ---
API_TOKEN = '7030807085:AAEj819hZ9zYQp8S65S65yV6v-6-uE_rM_M'
ADMIN_ID = 6996595720
source_channels = []
target_group = ""
filters = []

bot = telebot.TeleBot(API_TOKEN)

# Junction Style Main Menu
@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    if message.from_user.id == ADMIN_ID:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add('➕ Add Source', '➕ Set Target', '🔍 Filters', '📊 Bot Status', '⚙️ Advanced Settings')
        bot.reply_to(message, "--- FORWARDER MASTER PANEL ---\nBot Status: RUNNING\nSelect an option to configure:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_menu_options(message):
    if message.from_user.id == ADMIN_ID:
        if message.text == '📊 Bot Status':
            bot.reply_to(message, f"✅ System: Online\n✅ Sources: {len(source_channels)}\n✅ Filters: {len(filters)}")
        elif message.text == '➕ Add Source':
            bot.reply_to(message, "Please send the Channel ID or Username of the Source.")
        elif message.text == '🔍 Filters':
            bot.reply_to(message, "Send keywords separated by commas (e.g. Binance, Code, Gift).")
        elif message.text == '➕ Set Target':
            bot.reply_to(message, "Send the ID of your group where messages should be sent.")

# Forwarding Logic with Filters
@bot.channel_post_handler(func=lambda message: True)
def forward_messages(message):
    # This part will automatically check filters and forward messages
    for word in filters:
        if word.lower() in message.text.lower():
            if target_group:
                bot.copy_message(target_group, message.chat.id, message.message_id)
            break

print("Junction Bot Logic Started...")
bot.infinity_polling()
