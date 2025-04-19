import logging

from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler

from markups import *
from valutes import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

convertation_data = {}


async def echo(update, context):  # основная функция. возвращает курс к рублю валюты
    m = valute_normal_name(update.message.text)
    try:
        data = take_data(m)
        await update.message.reply_text(f"{data['Name']} курс к рублю {data['Value']}")
    except Exception:
        await update.message.reply_text("Некорректно введена валюта. Получить справку: /help", reply_markup=standart_markup)


async def start(update, context): # функция начала
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Напиши название валюты и узнаешь ее курс к рублю🤑", reply_markup=standart_markup
    )


async def help_command(update, context): # помощь
    await update.message.reply_text("""Введите валюту, в любом формате ("USD"="Доллар США"="840"), чтобы получить ее курс к рублю
    /start начать
    /help помощь
    /all курс всех валют к рублю
    /conversation введите валюту ее количество и другую валюту чтобы рассчитать вторую в первой
    """, reply_markup=standart_markup)


async def stop(update, context): # завершение conversation
    await update.message.reply_text("Отмена конвертации", reply_markup=standart_markup)
    return ConversationHandler.END


async def convert(update, context): # перевод валют
    await update.message.reply_text("Начало конвертации. Введите /stop чтобы отменить. Введите первую валюту",
                                    reply_markup=conversation_markup)
    return 1


async def all(update, context): # справка о всех валютах
    text = []
    a = take_data()['Valute']
    for i in a.keys():
        text.append(a[i]['Name'] + f' ({a[i]["NumCode"]}, {a[i]["CharCode"]})' + ' ' + ' курс к рублю ' + str(a[i]['Value']))
    await update.message.reply_text('\n\n'.join(text), reply_markup=standart_markup)


async def response1(update, context):
    m = valute_normal_name(update.message.text)
    convertation_data[str(update.effective_user.mention_html())] = dict()
    convertation_data[str(update.effective_user.mention_html())]['v1'] = m
    if is_valute_name(m):
        await update.message.reply_text("Введите количество этой валюты", reply_markup=conversation_markup_numbers)
        return 2
    else:
        await update.message.reply_text("Неверное имя валюты",
                                        reply_markup=conversation_markup)
        return 1


async def response2(update, context):
    m = valute_normal_name(update.message.text)
    convertation_data[str(update.effective_user.mention_html())]['c1'] = m
    await update.message.reply_text("Введите вторую валюту", reply_markup=conversation_markup)
    return 3


async def response3(update, context):
    m = update.message.text
    m = valute_normal_name(m)
    convertation_data[str(update.effective_user.mention_html())]['v2'] = m
    if is_valute_name(m):
        pass
    else:
        await update.message.reply_text("Неверное имя валюты",
                                        reply_markup=conversation_markup)
        return 3
    try:
        data = take_data()['Valute']
        a = float(data[convertation_data[str(update.effective_user.mention_html())]['v1']]['Value'])
        b = float(
            convertation_data[str(update.effective_user.mention_html())]['c1'])
        c = float(
            data[convertation_data[str(update.effective_user.mention_html())]['v2']]['Value'])
        res = a * b / c
        await update.message.reply_text(
            f"{convertation_data[str(update.effective_user.mention_html())]['c1']} {convertation_data[str(update.effective_user.mention_html())]['v1']}\n"
            f" = \n{res} {convertation_data[str(update.effective_user.mention_html())]['v2']}", reply_markup=standart_markup)
    except Exception:
        await update.message.reply_text("Не удалось рассчитать")
    return ConversationHandler.END


def main():
    application = Application.builder().token('7224928959:AAG5moeq49BuT_kUGJo6C3a3_vJxEMInRlc').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("all", all))

    application.add_handler(ConversationHandler(
        entry_points=[CommandHandler('convert', convert)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, response1)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, response2)],
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, response3)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    ))

    application.add_handler(MessageHandler(filters.TEXT, echo))



    application.run_polling()


if __name__ == '__main__':
    main()
