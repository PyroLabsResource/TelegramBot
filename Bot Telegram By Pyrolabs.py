from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup, InlineKeyboardButton

app = Client(
	"", #Inserisci il nome dell'app, seguendo le istruzioni su Readme.txt
	api_id="", #Inserisci il tuo api_id, seguendo le istruzioni su Readme.txt
	api_hash="", #Inserisci il tuo api_hash, seguendo le istruzioni su Readme.txt    
    bot_token="" #Inserisci il bot tokens, prendendolo da @BotFather
	)
app.set_parse_mode="HTML"

#Comandi

@app.on_message(filters.private & filters.command("start"))
def start(client, message):

	keyboard = InlineKeyboardMarkup([
		[InlineKeyboardButton(text="๐ฃ Canale Telegram", url="https://t.me/PyroLabs), InlineKeyboardButton(text="๐ค Robot Ufficiale Telegram", url="https://t.me/PyroLabsRobot)]
	])

	message.reply_text(f"๐  <b>Modifica col messaggio che vuoi</b> ๐ \n\n๐ฃ Modifica col messaggio che vuoi" + 
	"\n\n๐ซ Modifica col messaggio che vuoi" +
	"\nModifica col messaggio che vuoi</b>\n\nโ <b>Versione Bot</b> ยป <u>Versione Che vuoi</u>", reply_markup=keyboard)
    
app.run()