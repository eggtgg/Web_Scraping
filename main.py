import requests
from bs4 import BeautifulSoup
import quet_url


def main():
    waiting_line = set()
    history = set()
    url = input('Nhập link khởi đầu: ')
    url = quet_url.sua_url_goc(url)
    url_tim_duoc = quet_url.tim_url_lien_quan(url)
    waiting_line = waiting_line | url_tim_duoc
    history = history | url_tim_duoc
    while (waiting_line != set()) and (len(history) <= 1000):
        url = waiting_line.pop()
        url_tim_duoc = quet_url.tim_url_lien_quan(url)
        waiting_line = waiting_line | (url_tim_duoc - history)
        history = history | url_tim_duoc
    print(len(waiting_line))
    print(len(history))


if __name__ == '__main__':
    main()