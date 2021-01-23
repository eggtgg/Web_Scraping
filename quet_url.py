# Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re


# Hàm sửa URL xuất phát
# Truyền vào URL xuất phát
# Trả về URL xuất phát chuẩn để gửi lệnh Requests không bị lỗi
def sua_url_goc(url_goc):
    if url_goc[-1] == '/':
        url_goc = url_goc[0: -1]
        return url_goc
    else:
        return url_goc


# Hàm tìm kiếm các URL liên quan để tải xuống
# Truyền vào URL cần được quét, và URL xuất phát
# Kết quả trả về là tập hợp các URL tìm được
def tim_url_lien_quan(url, url_goc):
    url_tim_duoc = set()
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    results = link_soup('a', attrs={'href': True})
    for i in results:
        a = i['href']
        mau = f'^{url_goc}[^?#]*$'
        mau2 = '^/[^?#]*$'
        if re.match(mau, a):
            url_tim_duoc.add(a)
        else:
            if re.match(mau2, a):
                url_lien_quan = f'{url_goc}{a}'
                url_tim_duoc.add(url_lien_quan)
    return url_tim_duoc


# Tăng số lượng URL trong tập hợp lên
# Cần truyền vào một set gồm các phần tử cần được duyệt, và URL xuất phát
# Kết quả trả về tập hợp các URL có số phần tử đạt yêu cầu
def them_va_duyet_hang_cho(hang_cho, url_goc):
    history = hang_cho
    while (len(hang_cho) > 0) and (len(history) < 500):
        url_tim_duoc = tim_url_lien_quan(hang_cho.pop(), url_goc)
        hang_cho = hang_cho | (url_tim_duoc - history)
        history = history | url_tim_duoc
    return history


def main():
    url_tim_duoc = tim_url_lien_quan('https://vietnamnet.vn', 'https://vietnamnet.vn')
    history = them_va_duyet_hang_cho(url_tim_duoc)
    for i in history:
        print(i)


if __name__ == '__main__':
    main()
