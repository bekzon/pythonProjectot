import requests
from bs4 import BeautifulSoup

URL = 'https://www.sports.ru/la-liga/calendar/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/87.0.4280.141 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('a', class_='player')
   # print(items)

    cars = []
    for item in items:
        cars.append({
            'title': item.find('a', class_='player').get_text()
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("!")


parse()