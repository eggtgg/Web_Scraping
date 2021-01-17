import requests
from bs4 import BeautifulSoup


def sua_url_goc(url_goc):
    if url_goc[-1] == '/':
        url_goc = url_goc[0: -1]
        return url_goc
    else:
        return url_goc


def tim_url_lien_quan(url_goc):
    url_tim_duoc = set()
    link = requests.get(url_goc)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    results = link_soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        if (a[0] == '/'):
            url_lien_quan = f'{url_goc}{a}'
            url_tim_duoc.add(url_lien_quan)
        else:
            if a[0] == 'h':
                url_tim_duoc.add(a)
            else:
                continue
    return url_tim_duoc






def main():
    url_tim_duoc = tim_url_lien_quan('https://baomoi.com')
    for i in url_tim_duoc:
        print(i)


if __name__ == '__main__':
    main()

