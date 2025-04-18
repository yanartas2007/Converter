import logging
import requests
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from valutes import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    m = update.message.text
    try:
        data = take_data()
        await update.message.reply_text(f"{data['Valute'][m]['Name']} курс к рублю {data['Valute'][m]['Value']}")
    except Exception:
        await update.message.reply_text("Некорректно введена валюта. Получить справку: /help")

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Напиши название валюты и узнаешь ее курс к рублю",
    )


async def help_command(update, context):
    await update.message.reply_text("Введите валюту, например USD")


def main():
    application = Application.builder().token('7224928959:AAG5moeq49BuT_kUGJo6C3a3_vJxEMInRlc').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(MessageHandler(filters.TEXT, echo))

    application.run_polling()


if __name__ == '__main__':
    main()
