# pip install pyTelegramBotAPI
import telebot

import os
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

MY_NAME = "Дарина"          # ← имя, на которое реагируем
REPEAT_COUNT = True       # True = повторяет столько раз, сколько упомянули

@bot.message_handler(func=lambda m: m.chat.type in ["group", "supergroup"])
def mention_handler(message):
    if not message.text:
        return
        
    text = message.text.lower()
    name_lower = MY_NAME.lower()
    
    count = text.count(name_lower)
    
    if count == 0:
        return
        
    if REPEAT_COUNT:
        reply = (MY_NAME + " ") * count
    else:
        reply = MY_NAME
        
    # Убираем лишний пробел в конце и можно добавить эмоцию
    reply = reply.strip() + "‼️"
    
    bot.reply_to(message, reply)

bot.polling(none_stop=True)