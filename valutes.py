from pprint import pprint
import requests
import csv


def take_data(m=None): # возвращает словарь с курсами
    adres = 'https://www.cbr-xml-daily.ru/daily_json.js' # API центробанка
    data = requests.get(adres).json()
    if m:
        data = data['Valute'][m]
    return data

def valute_normal_name(m): # превращает введенное название валюты в ключ словаря
    m2 = m.lower().strip()
    try:
        with open('data\\names_table.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i in reader:
                for j in i:
                    if j.lower() == m2:
                        return i[0]
            else:
                return m
    except Exception:
        print('data\\names_table.csv не найден. он будет пересоздан')
        update_csv()
        with open('data\\names_table.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i in reader:
                for j in i:
                    if j.lower() == m2:
                        return i[0]
            else:
                return m

def update_csv(): # создает таблицу со списком валют и их названий в разных системах обозначений
    with open('data\\names_table.csv', 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['CharCode', 'Name', 'NumCode' ])
        data = take_data()['Valute']
        for i in data.keys():
            writer.writerow([data[i]['CharCode'], data[i]['Name'],data[i]['NumCode']])

def is_valute_name(m): # True если это название валюты и False если нет
    m2 = m.lower().strip()
    try:
        with open('data\\names_table.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i in reader:
                for j in i:
                    if j.lower() == m2:
                        return True
            else:
                return False
    except Exception:
        print('data\\names_table.csv не найден. он будет пересоздан')
        update_csv()
        with open('data\\names_table.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for i in reader:
                for j in i:
                    if j.lower() == m2:
                        return True
            else:
                return False

if __name__ == '__main__': # для отладки, можно запустить этот файл
    update_csv()
    pprint(take_data())


'''{'Date': '2025-04-19T11:30:00+03:00',
 'PreviousDate': '2025-04-18T11:30:00+03:00',
 'PreviousURL': '//www.cbr-xml-daily.ru/archive/2025/04/18/daily_json.js',
 'Timestamp': '2025-04-19T16:00:00+03:00',
 'Valute': {'AED': {'CharCode': 'AED',
                    'ID': 'R01230',
                    'Name': 'Дирхам ОАЭ',
                    'Nominal': 1,
                    'NumCode': '784',
                    'Previous': 22.3336,
                    'Value': 22.0932}}}''' # образец словаря. сокращено до 1 валюты.