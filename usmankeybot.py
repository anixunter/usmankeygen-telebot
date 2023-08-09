import requests
import telebot
from flask import Flask, request

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram Bot Token
TELEGRAM_BOT_TOKEN = '6372898666:AAFpyXd6TWUz2YtKeuOq8bVaRKZyxVYw55I'

# Fixed URL for scraping
WEBSITE_URL = 'https://usmanbypass.top/usm83.php'

WEBURL2 = 'http://dakukey076.atwebpages.com/redirectkey076.php'

# Initialize the bot with your token
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Function to scrape the usmankey website and return the body content
def scrape_website():
    response = requests.get(WEBSITE_URL)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to scrape the dakukey website and return the key content
def scrape_website2():
    response = requests.get(WEBURL2)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to handle the usman command
@bot.message_handler(func=lambda message: message.text.lower() == 'usman')
def get_website(message):
    body = scrape_website()
    if body:
        bot.send_message(message.chat.id, body)
    else:
        bot.send_message(message.chat.id, "Failed to fetch the website body.")

# Function to handle the daku command
@bot.message_handler(func=lambda message: message.text.lower() == 'daku')
def get_website(message):
    body = scrape_website2()
    if body:
        bot.send_message(message.chat.id, body)
    else:
        bot.send_message(message.chat.id, "Failed to fetch the website body.")

# Flask app initialization
app = Flask(__name__)

# Route to handle Telegram updates (webhook endpoint)
@app.route('/' + TELEGRAM_BOT_TOKEN, methods=['POST'])
def webhook_handler():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'OK'

# Set the webhook URL with your public URL where the bot is hosted
WEBHOOK_URL = 'https://usmankeybot.onrender.com/' + TELEGRAM_BOT_TOKEN
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    # Start the Flask app
    app.run(host='0.0.0.0', port=8080)
