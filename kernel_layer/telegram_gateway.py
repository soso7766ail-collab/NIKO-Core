import telebot
import os

class NikoCloud:
    def __init__(self):
        # هنا يجب وضع الـ Token الخاص بـ Bot التلجرام الذي ستنشئه
        self.token = "YOUR_BOT_TOKEN_HERE"
        self.bot = telebot.TeleBot(self.token)

    def send_alert(self, message):
        chat_id = "YOUR_CHAT_ID_HERE"
        self.bot.send_message(chat_id, f"⚠️ تنبيه من Niko:\n{message}")

    def send_intruder_photo(self, photo_path):
        chat_id = "YOUR_CHAT_ID_HERE"
        with open(photo_path, 'rb') as photo:
            self.bot.send_photo(chat_id, photo, caption="📸 تم رصد متطفل!")
