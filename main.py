import quet_url
import luu_url


def main():
    url_goc = input('Nhập link khởi đầu: ')
    url_goc = quet_url.sua_url_goc(url_goc)
    url_tim_duoc = quet_url.tim_url_lien_quan(url_goc, url_goc)
    waiting_line = url_tim_duoc
    history = quet_url.them_va_duyet_hang_cho(waiting_line)

    luu_url.tao_thu_muc('html_file_viet_nam_net_3')

    for (stt, url_con) in enumerate(history):
        luu_url.luu_file(url_con, stt)
        print(f'{stt} {url_con}')



if __name__ == '__main__':
    main()