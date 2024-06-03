import re
from datetime import date

txt = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."

today = date.today()

cari_tanggal = re.findall("\d{4}-\d{2}-\d{2}", txt)

for i in cari_tanggal:
    tanggal = i.split("-")

    tahun, bulan, hari = tanggal
    old_date = date(int(tahun), int(bulan), int(hari))


    selisih_hari = (today - old_date).days

    print(f"{old_date} 00:00:00 selisih {selisih_hari} hari")

