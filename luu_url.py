import os
import requests
import codecs


def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


def luu_file(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


def main():
    tao_thu_muc('trioc')
    luu_file('https://baomoi.com/', 2)


if __name__ == "__main__":
    main()


