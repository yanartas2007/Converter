from telegram import ReplyKeyboardMarkup

markup = ReplyKeyboardMarkup([['/start', '/help'], ['/all', 'SEK'],
                  ['USD', 'EUR']], one_time_keyboard=True)