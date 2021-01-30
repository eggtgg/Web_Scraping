import quet_url
import luu_url


def main():
    url_goc = input('Nhập link khởi đầu: ')
    so_luong_trang = int(input('nhập số lượng trang: '))
    url_goc = quet_url.sua_url_goc(url_goc)
    waiting_line = quet_url.tim_url_lien_quan(url_goc, url_goc)
    history = quet_url.them_va_duyet_hang_cho(waiting_line, url_goc, so_luong_trang)

    luu_url.tao_thu_muc(input('Nhập tên thư mục lưu file: '))
    luu_url.luu_tat_ca_file(history, so_luong_trang)


if __name__ == '__main__':
    main()
