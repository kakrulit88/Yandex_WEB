import sys

from geocoder import *
from mapapi_pil import *


def main():
    toponym = ' '.join(sys.argv[1:])

    if toponym:
        lon, lat = get_coordinates(toponym)

        spn = '0.005,0.005'
        show_map(**{'ll': f'{lat},{lon}', 'spn': spn})

        ll, spn = get_ll_span(toponym)
        show_map(**{'ll' : f'{lat},{lon}', 'spn': spn, 'pt': ll})


if __name__ == '__main__':
    main()
