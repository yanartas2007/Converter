from pprint import pprint
import requests


def take_data(m=None): # возвращает словарь с курсами от центробанка
    adres = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(adres).json()
    if m:
        data = data['Valute'][m]
    return data

def valute_normal_name(m):
    '''позже будет реализовано, чтобы превращать запросы любого формата в название валюты. Например:
    "      НовоЗЕландСКий ДоЛЛар    " -> "NZD"'''
    pass

if __name__ == '__main__': # для отладки, можно запустить этот файл и посмотреть пример словаря
    pprint(take_data())