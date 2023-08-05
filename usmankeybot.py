import requests
import telebot

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram Bot Token
TELEGRAM_BOT_TOKEN = '6372898666:AAFpyXd6TWUz2YtKeuOq8bVaRKZyxVYw55I'

# Fixed URL for scraping
WEBSITE_URL = 'https://usmanbypass.top/usm83.php'

# Initialize the bot with your token
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Function to scrape the fixed website and return the body content
def scrape_website():
    response = requests.get(WEBSITE_URL)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to handle the usman/key/usmankey command
@bot.message_handler(func=lambda message: message.text.lower() in ['usman', 'key', 'usmankey'])
def get_website(message):
    body = scrape_website()
    if body:
        bot.reply_to(message, body)
    else:
        bot.reply_to(message, "Failed to fetch the website body.")

def main():
    # Start the Bot using long polling
    bot.polling()

if __name__ == "__main__":
    main()
