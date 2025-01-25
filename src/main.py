import telebot
import time
import schedule


with open('token.txt') as file:
    fls = [line.split('=') for line in file]
    TOKEN = [line[1] for line in fls for col in line if col == 'BOT_TOKEN'][0]

bot = telebot.TeleBot(TOKEN)

user_chat_ids = []


# /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Welcome to your journey to become a better-hydrated being!")
    if message.chat.id not in user_chat_ids:
        user_chat_ids.append(message.chat.id)
        bot.reply_to(message, "You will now receive water drinking reminders!")
    else:
        bot.reply_to(message, "You are already subscribed to water reminders!")


# /video
@bot.message_handler(commands=['video'])
def send_video(message):
    bot.reply_to(message,
                 "https://www.youtube.com/watch?v=qfgaGcjp1tE")


# /reminder
clock = ["08", "11", "13", "15", "17", "19", "21", "23", "00"]


def send_reminder():
    for chat_id in user_chat_ids:
        bot.send_message(chat_id, "Time to drink water! Stay hydrated 💧")


for hour in clock:
    hr = hour + ":03"
    schedule.every().day.at(hr, "America/Sao_Paulo").do(send_reminder)


bot.infinity_polling()

while True:
    schedule.run_pending()
    time.sleep(1)
