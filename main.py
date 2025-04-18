import logging
import requests
from telegram.ext import Application, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    adres = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(adres).json()
    a = update.message.text
    s = str(data['Valute'][a]['Name']+str(data['Valute'][a]['Value']))
    try:
        await update.message.reply_text(s)
    except Exception:
        await update.message.reply_text('напишите название валюты чтобы получить справку. Например:\nUSD, MDL, NZD')


def main():
    application = Application.builder().token('7224928959:AAG5moeq49BuT_kUGJo6C3a3_vJxEMInRlc').build()

    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
