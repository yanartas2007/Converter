from pprint import pprint
import requests


def take_data():
    adres = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(adres).json()
    return data