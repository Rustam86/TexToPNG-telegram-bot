from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os, requests
from mytoken import TOKEN

def latex_to_png(code, file):
    response = requests.get('http://latex.codecogs.com/png.latex?\dpi{300} \large %s' % code)
    with open(file, 'wb') as f:
    	f.write(response.content)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Hello stranger!")

def echo(bot, update):
	latex_to_png(r'{}'.format(update.message.text), 'image.png')
	bot.send_photo(chat_id=update.message.chat_id, photo=open('image.png', 'rb'))

def main():
	updater = Updater(token=TOKEN)
	dispatcher = updater.dispatcher

	start_handler = CommandHandler('start', start)
	echo_handler = MessageHandler(Filters.text, echo)

	dispatcher.add_handler(start_handler)
	dispatcher.add_handler(echo_handler)

	updater.start_polling()
if __name__ == '__main__':
	main()