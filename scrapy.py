import requests
from bs4 import BeautifulSoup


#1 HÀM REQUESTS LINK VÀ TÌM LINK MỚI ADD VÀO
def request_url(url_text):
    l = requests.get(url_text)
    return l


#2 HÀM PHÂN TÍCH DƯỚI DẠNG BEATIFULSUOP VÀ TRẢ VỀ CÁC URL LIÊN QUAN
def phan_tich(request_result):
    link_html = BeautifulSoup(request_result.text, 'html.parser')
    list_url_lien_quan = link_html('div', class_="clearfix item")
    return list_url_lien_quan


#3 HÀM DOWNLOAD LINK
def download_link(html_text):
    file = open('file' + str() + '.html', 'w')
    file.write(html_text)
    file.close()
    pass

def ham4(list_result_phan_tich):
    for a_i in list_result_phan_tich:
        linkrq ='https://vietnamnet.vn'+ a_i.find('a')['href']
        if linkrq in s:
            continue
        else:
            s.append(linkrq)
            html = request_url(linkrq)
            download_link(html.text)

def ham5(url):
    k = request_url(url)
    h = phan_tich(k)
    ham4(h)


