import requests

countriesdict = {'AUD': 'австралия',
                 'AZN': 'азербайджан',
                 'GBP': 'великобритания',
                 'AMD': 'армения',
                 'BYN': 'белоруссия',
                 'BGN': 'болгария',
                 'BRL': 'бразилия',
                 'HUF': 'венгрия',
                 'VND': 'вьетнам',
                 'HKD': 'гонконг',
                 'GEL': 'грузия',
                 'DKK': 'дания',
                 'AED': 'оаэ',
                 'USD': 'сша',
                 'EGP': 'египет',
                 'INR': 'индия',
                 'IDR': 'индонезия',
                 'KZT': 'казахстан',
                 'CAD': 'канада',
                 'QAR': 'катар',
                 'KGS': 'киргизия',
                 'CNY': 'китай',
                 'MDL': 'молдавия',
                 'NZD': 'новозеландия',
                 'NOK': 'норвегия',
                 'PLN': 'польша',
                 'RON': 'румыния',
                 'SGD': 'сингапур',
                 'TJS': 'таджикистан',
                 'THB': 'таиланд',
                 'TRY': 'турция',
                 'TMT': 'туркмения',
                 'UZS': 'узбекистан',
                 'UAH': 'украина',
                 'CZK': 'чехия',
                 'SEK': 'швеция',
                 'CHF': 'швейцария',
                 'RSD': 'сербия',
                 'ZAR': 'юар',
                 'KRW': 'южная корея',
                 'JPY': 'япония',
                 } # у XDR нет страны; EUR считает островом, или не находит


def address(country):
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'
    geocode = country
    # Готовим запрос.
    geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]

        d = list(map(float, toponym['boundedBy']['Envelope']['upperCorner'].split()))
        d2 = list(map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split()))
        d[0] -= d2[0]
        d[1] -= d2[1]
        d = list(map(str, d))

        toponym_coodrinates = toponym["Point"]["pos"]

        return ','.join(toponym_coodrinates.split(' ')), ','.join(d)


def picture(address, spn):
    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={address}&spn={spn}'
    # Готовим запрос.

    map_request = f"{server_address}{ll_spn}&apikey={api_key}"

    return map_request
