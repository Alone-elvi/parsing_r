import requests
import ssl
from bs4 import BeautifulSoup


def get_html(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('span', class_='ui-icon-seek-end"')


def main():
    # https://tsouz.belgiss.by/
    pass


if __name__ == '__main__':
    main()
