from PIL import Image
from io import BytesIO
import requests


def show_map(l='map', **params):
    api_url = 'http://static-maps.yandex.ru/1.x/'
    response = requests.get(api_url, params)

    if not response:
        raise RuntimeError(f'Bad request: {response.url}, status: {response.status_code}')

    Image.open(BytesIO(
        response.content)).show()


if __name__ == '__main__':
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = "37.530887"
    lat = "55.703118"
    delta = "0.002"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    show_map(**params)
