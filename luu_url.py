# Các thư viện cần thiết
import os
import requests
import codecs


# Hàm Tạo thư mục và chuyển đến thư mục đó
def tao_thu_muc(name):
    os.mkdir(name)
    os.chdir(name)


# Hàm Lưu file
def luu_file(url, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(requests.get(url).text)
    file.close()


def luu_tat_ca_file(history):
    for (stt, url_con) in enumerate(history):
        luu_file(url_con, stt)
        print(f'{stt} {url_con}')


def main():
    tao_thu_muc('trioc')
    luu_file('https://baomoi.com/', 2)


if __name__ == "__main__":
    main()