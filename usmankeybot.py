import requests
import telebot
from flask import Flask

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram Bot Token
TELEGRAM_BOT_TOKEN = '6372898666:AAFpyXd6TWUz2YtKeuOq8bVaRKZyxVYw55I'

# Fixed URL for scraping
WEBSITE_URL = 'https://usmanbypass.top/usm83.php'

# Initialize the bot with your token
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Initialize a variable to store the scraped website's body
scraped_body = None

# Function to scrape the fixed website and store the body content
def scrape_website():
    global scraped_body
    response = requests.get(WEBSITE_URL)
    if response.status_code == 200:
        scraped_body = response.text
        # Send the website body to the Telegram bot
        bot.send_message(chat_id='-1001693818855', text=scraped_body)
    else:
        scraped_body = None

# Function to handle the usman/key/usmankey command
@bot.message_handler(func=lambda message: message.text.lower() in ['usman', 'key', 'usmankey'])
def get_website(message):
    scrape_website()  # Call the function to scrape the website
    bot.reply_to(message, scraped_body or "Failed to fetch the website body.")

# Flask app initialization
app = Flask(__name__)

# Route to show the scraped body on the web page
@app.route('/')
def show_scraped_body():
    scrape_website()  # Call the function to scrape the website
    return f"<pre>{scraped_body or 'Failed to fetch the website body.'}</pre>"
if __name__ == "__main__":
    # Start the Flask app and the Telegram bot concurrently
    import threading
    flask_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080})
    flask_thread.start()
    bot.polling()
