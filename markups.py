from telegram import ReplyKeyboardMarkup

standart_markup = ReplyKeyboardMarkup([['/start', '/help'], ['/all', '/convert'],
                                       ['USD', 'EUR']], one_time_keyboard=True)

conversation_markup = ReplyKeyboardMarkup([['/stop', '/stop'], ['USD', 'EUR']], one_time_keyboard=True)
conversation_markup_numbers = ReplyKeyboardMarkup([['/stop', '1'], ['1000', '100000']], one_time_keyboard=True)
