import logging

from telegram.ext import Application, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token('7224928959:AAG5moeq49BuT_kUGJo6C3a3_vJxEMInRlc').build()

    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
