import requests
import telebot

BOT_TOKEN = "8021445082:AAFlQ79GYwaUaN6f79gbX21uET8o4xkchEs"

bot = telebot.TeleBot(BOT_TOKEN)

PHONE_API = "https://ajith-indian-mob-info.p.rapidapi.com/employees?mobno="

HEADERS = {
    "x-rapidapi-key": "a000af8013mshc452a6c89947c9ap12cdaejsn95dcfb5ee0c4",
    "x-rapidapi-host": "ajith-indian-mob-info.p.rapidapi.com"
}

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "🤖 Send any 10-digit number to get details")

@bot.message_handler(func=lambda m: m.text and m.text.isdigit() and len(m.text) == 10)
def lookup(msg):
    number = msg.text
    url = PHONE_API + number

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)

        if res.status_code != 200:
            bot.reply_to(msg, "⚠️ API Error")
            return

        data = res.json()

        if not data:
            bot.reply_to(msg, "❌ No data found")
            return

        text = f"📱 Number: {number}\n\n"
        for k, v in data.items():
            text += f"🔹 {k}: {v}\n"

        bot.reply_to(msg, text)

    except:
        bot.reply_to(msg, "⚠️ Error fetching data")

print("Bot running...")
bot.infinity_polling()
