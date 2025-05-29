import telebot
from flask import Flask, request
import os
import random

# Token del bot Telegram
TOKEN = '7557489953:AAHexfr7Rq0mXZXYcp0iP3AddMJWoSh3RcY'
bot = telebot.TeleBot(TOKEN)

# Barzellette suddivise per tema
jokes = {
    "scuola": [
        "Prof: Dimmi un verbo! Studente: Che cos’è un verbo?",
        "Cosa fa uno studente davanti al computer? Spera.",
        "La prof: 'Questa è una domanda a trabocchetto!' Lo studente: 'Allora ci salto!'."
    ],
    "lavoro": [
        "Colloquio di lavoro: 'Lei parla l'inglese?' – 'Certo, soprattutto nei pub!'",
        "Il capo: 'Sei in ritardo!' – Il dipendente: 'No, sono in modalità flessibile!'",
        "Vorrei un lavoro part-time... con stipendio full-time!"
    ],
    "svago": [
        "Sai perché il mare è blu? Perché i pesci fanno blu blu blu!",
        "Sai perché i fantasmi vanno in palestra? Per mettere massa eterea.",
        "Un cavallo entra in un bar... e il barista gli dice: 'Perché la faccia lunga?'"
    ]
}

# Comando start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
        "🎉 Ciao! Sono il tuo bot delle barzellette!\n\n"
        "Scrivimi uno di questi comandi per ricevere una barzelletta a tema:\n"
        "• /scuola\n• /lavoro\n• /svago"
    )

# Comandi tematici
@bot.message_handler(commands=['scuola', 'lavoro', 'svago'])
def send_joke_by_topic(message):
    topic = message.text.replace("/", "")
    joke = random.choice(jokes[topic])
    bot.send_message(message.chat.id, f"😂 {joke}")

# Fallback: rispondi con istruzioni
@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.reply_to(message, "Scrivimi uno di questi comandi:\n/scuola, /lavoro o /svago")

# Flask per il webhook
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Bot attivo!", 200

@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "", 200

# Avvio app
if __name__ == '__main__':
    WEBHOOK_URL = 'https://NOME-DEL-TUO-BOT.onrender.com'  # <-- sostituire con l'URL reale su Render
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
