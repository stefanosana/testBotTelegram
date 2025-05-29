import telebot
import random

TOKEN = '7517732337:AAFTMh4j2x_6yg6rxrIDKNBSSkDw4wFB_Ow'
bot = telebot.TeleBot(TOKEN)

jokes = {
    "scuola": [
        "Prof: Dimmi un verbo! Studente: Che cos’è un verbo?",
        "La prof: 'Questa è una domanda a trabocchetto!' Lo studente: 'Allora ci salto!'"
    ],
    "lavoro": [
        "Colloquio di lavoro: 'Lei parla l'inglese?' – 'Certo, soprattutto nei pub!'",
        "Vorrei un lavoro part-time... con stipendio full-time!"
    ],
    "svago": [
        "Sai perché i fantasmi vanno in palestra? Per mettere massa eterea.",
        "Un cavallo entra in un bar... e il barista gli dice: 'Perché la faccia lunga?'"
    ]
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "🎉 Ciao! Scrivi uno di questi comandi per ricevere una barzelletta:\n"
        "/scuola\n/lavoro\n/svago"
    )

@bot.message_handler(commands=['scuola', 'lavoro', 'svago'])
def send_joke(message):
    topic = message.text[1:]  # rimuove lo slash /
    bot.send_message(message.chat.id, f"😂 {random.choice(jokes[topic])}")

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.reply_to(message, "Scrivi /scuola, /lavoro o /svago per una barzelletta a tema!")

if __name__ == "__main__":
    bot.polling(non_stop=True)
