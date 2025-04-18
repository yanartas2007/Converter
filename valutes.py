from pprint import pprint
import requests

adres = 'https://www.cbr-xml-daily.ru/daily_json.js'
data = requests.get(adres).json()
pprint(data)
# pprint(data['Valute']['USD'])
