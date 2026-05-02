import telebot
import os
from telebot import types

# Use your NEW token here
API_TOKEN = 'یہاں_نیا_ٹوکن_پیسٹ_کریں'
ADMIN_ID = 6996595720

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):
    if message.from_user.id == ADMIN_ID:
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add('➕ Add Source', '🔍 Filters', '📊 Status')
        bot.reply_to(message, "--- MASTER PANEL ACTIVE ---\nStatus: Online", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if message.from_user.id == ADMIN_ID:
        if message.text == '📊 Status':
            bot.reply_to(message, "✅ Bot is working perfectly!")
        else:
            bot.reply_to(message, f"Command Received: {message.text}")

print("Starting Bot...")
bot.infinity_polling()
