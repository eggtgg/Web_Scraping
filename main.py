import quet_url
import luu_url


def main():
    url_goc = input('Nhập link khởi đầu: ')
    url_goc = quet_url.sua_url_goc(url_goc)
    url_tim_duoc = quet_url.tim_url_lien_quan(url_goc, url_goc)
    waiting_line = url_tim_duoc
    history = quet_url.them_va_duyet_hang_cho(waiting_line, url_goc)

    luu_url.tao_thu_muc('vnexpress')
    luu_url.luu_tat_ca_file(history)


if __name__ == '__main__':
    main()
