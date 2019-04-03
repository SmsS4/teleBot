from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sys
import threading

targetId = "shjuxudb"

def echo(bot, update):
	print("echo")
	print(targetId)
	if update.message is not None :
		ID = update.message.chat_id
		print(update.message.from_user.username)
		if update.message.from_user.username == targetId:
			bot.forward_message(chat_id=ID, from_chat_id=ID, message_id = update.message.message_id)
	if update.edited_message is not None :
		ID = update.edited_message.chat_id
		if update.edited_message.from_user.username == targetId:
			bot.send_message(chat_id=ID, text="Mahdavi edit kard ye chizi ro be in chiz :")
			bot.forward_message(chat_id=ID, from_chat_id=ID, message_id = update.edited_message.message_id)

print("bot starting...")
updater = Updater(token = '739734320:AAEk4U5cEZGxQ-I9f7E9VfgyaZdMRzq9XlM')

ADMIN = "SadeghShobeiri"
def shutdown():
	print("HEY")
	print("HOOY")
	updater.is_idle	= False;
	updater.stop();
	print("WOOW")
	sys.exit(2)

def stp(bot, update):
	threading.Thread(target=shutdown).start()

print("updater construced")

stop_handler = CommandHandler("stp", stp)
updater.dispatcher.add_handler(stop_handler)

echo_handler = MessageHandler(Filters.all,echo, edited_updates=True)
updater.dispatcher.add_handler(echo_handler)
print("text handler added")

updater.start_polling()
print("bot start polling...")
updater.idle()
print("bot exiting...")
