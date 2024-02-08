import requests

spisok_cities = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

request = requests.get(
    'https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={}&format=json')

for i in spisok_cities:
    request = requests.get(
        f'https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={i}&format=json')
    spisok = request.json()
    addres = \
        spisok['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData'][
            'Address']['Components'][2]['name']

    print(addres)
