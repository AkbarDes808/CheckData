import os
from datetime import datetime, timedelta

def cek_file_hilang(direktori, tanggal_awal, tanggal_akhir):
    tanggal_awal_obj = datetime.strptime(tanggal_awal, "%Y-%m-%dT%H-%M-%S")
    tanggal_akhir_obj = datetime.strptime(tanggal_akhir, "%Y-%m-%dT%H-%M-%S")
    ada_tanggal_hilang = False

    tanggal = tanggal_awal_obj
    while tanggal <= tanggal_akhir_obj:
        nama_file = tanggal.strftime("%Y-%m-%dT%H-%M-%S") + ".mp4"

        if nama_file not in os.listdir(direktori):
            print("File hilang: {}".format(nama_file))
            ada_tanggal_hilang = True

        tanggal += timedelta(hours=1)

    if not ada_tanggal_hilang:
        print("Tidak ada tanggal yang hilang dalam rentang yang diberikan")

direktori = input("Masukkan direktori video: ")
tanggal_awal = input("Masukkan tanggal awal (format: YYYY-MM-DD): ") + "T00-00-00"
tanggal_akhir = input("Masukkan tanggal akhir (format: YYYY-MM-DD): ") + "T23-59-59"
cek_file_hilang(direktori, tanggal_awal, tanggal_akhir)

input("Press Enter to exit...")
