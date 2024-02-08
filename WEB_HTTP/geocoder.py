import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(adrees):
    request_url = 'http://geocode-maps.yandex.ru/1.x/'

    geocoder_params = {
        'apikey': API_KEY,
        'geocode': adrees,
        'format': 'json'
    }
    response = requests.get(request_url, params=geocoder_params)

    if response:
        json_response = response.json()
    else:
        raise RuntimeError(f'Bad request: {response.url}, status: {response.status_code}')

    features = json_response['response']['GeoObjectCollection']['featureMember']
    return features[0]['GeoObject'] if features else None


def get_coordinates(addres):
    toponym = geocode(addres)

    if not toponym:
        return None, None

    toponym_coords = toponym['Point']['pos']
    lon, lat = toponym_coords.split()
    return float(lon), float(lat)


def get_ll_span(adress):
    toponym = geocode(adress)
    if not toponym:
        return None, None

    toponym_coords = toponym['Point']['pos']

    lon, lat = toponym_coords.split()

    ll = ','.join(toponym_coords)

    envelope = toponym['boundedBy']['Envelope']

    left, bot = envelope['lowerCorner'].split()
    right, top = envelope['upperCorner'].split()

    dx = abs(float(left) - float(right)) / 2
    dy = abs(float(top) - float(bot)) / 2

    span = f'{dx},{dy}'
    return span, ll


if __name__ == '__main__':
    print(geocode('САРАнск'))