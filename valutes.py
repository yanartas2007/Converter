from pprint import pprint
import requests


def take_data(m=None):
    adres = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(adres).json()
    if m:
        data = data['Valute'][m]
    return data

if __name__ == '__main__':
    pprint(take_data())