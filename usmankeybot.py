import requests
import telebot
import schedule
import time

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

# Function to handle the /get_website command
@bot.message_handler(func=lambda message: message.text.lower() in ['usman', 'key', 'usmankey'])
def get_website(message):
    body = scrape_website()
    if body:
        bot.reply_to(message, body)
    else:
        bot.reply_to(message, "Failed to fetch the website body.")

# Function to ping the server
def ping_server():
    requests.get('https://usmankeybot.onrender.com')
    print('Pinged server')

def main():
    # Start the Bot using long polling
    bot.polling()
    
    # Schedule the ping every 14 minutes
    schedule.every(14).minutes.do(ping_server)

    # Run the scheduled tasks in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
