from telegram import ReplyKeyboardMarkup

'''Здесь приведены виды клавиатур'''

standart_markup = ReplyKeyboardMarkup([['/start', '/help'], ['/all', '/convert'],  # стандартный
                                       ['USD', 'EUR']], one_time_keyboard=True)

conversation_markup = ReplyKeyboardMarkup([['/stop', '/stop'], ['USD', 'EUR']],
                                          one_time_keyboard=True)  # перевод валют - валюты
conversation_markup_numbers = ReplyKeyboardMarkup([['/stop', '1'], ['1000', '100000']],
                                                  one_time_keyboard=True)  # перевод валют - число
