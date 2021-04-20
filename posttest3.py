import os
import datetime
import time

database = {
    "Vaksinasi": {
        "Tanggal": (20, 4, 2021),
        "Daftar": [],
        "Data": []
    },
    "Vaksin": [
        {'Nama': 'Sinovac', 'Produksi': 'Sinovac Biotech', 'Nomor': []},
        {'Nama': 'Merah Putih', 'Produksi': 'PT Bio Farma', 'Nomor': []},
    ],
    "Account": {
        6408120804020002: {
            "Username": "anddfian",
            "Password": "anddfian",
            "Level": "user",
            "Nama": "Andi Alfian Bahtiar",
            "Umur": 19,
            "NoHP": "085346816962",
            "Alamat": "Gg. Simpati",
            "Alamat2": "Singa Geweh",
            "Created": (20, 4, 2021, 10, 00, 00),
            "Vaksinasi": 0,
            "Riwayat": {}
            },
        6400000508640000: {
            "Username": "terawan",
            "Password": "terawan",
            "Level": "dinkes",
            "Nama": "Terawan Agus Putranto",
            "Umur": 56,
            "NoHP": "080000000000",
            "Alamat": "Indonesia",
            "Alamat2": "Indonesia",
            "Created": (14, 1, 2021, 10, 00, 00),
            "Vaksinasi": 0,
            "Riwayat": {}
            }
    }
}
session_akun = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_auth():
    clear_screen()
    print("=====================================================================")
    print("|                            SELAMAT DATANG                         |")
    print("|                                  DI                               |")
    print("|                     APLIKASI VAKSINASI COVID-19                   |")
    print("|                                 OLEH                              |")
    print("|       ANDI ALFIAN BAHTIAR - 2009106002 - INFORMATIKA A 2020       |")
    print("=====================================================================")
    print("| [1] Daftar Akun                                                   |")
    print("| [2] Masuk Akun                                                    |")
    print("| [0] Keluar Aplikasi                                               |")
    print("=====================================================================")
    selected_login = str(input("Masukkan Pilihan> "))
    if(selected_login == "1"):
        auth_register()
    elif(selected_login == "2"):
        show_login()
    elif(selected_login == "0"):
        close_app()
    else:
        print("=====================================================================")
        print("| Error: Pilihan salah!                                             |")
        print("=====================================================================")
        back_to_auth()

def auth_register():
    clear_screen()
    print("========================================================================")
    print("|                              DAFTAR AKUN                             |")
    print("========================================================================")
    print("| [1] Isi Biodata                                                      |")
    print("| [2] Kembali                                                          |")
    print("========================================================================")
    selected_register = str(input("Masukkan Pilihan> "))
    if(selected_register == "1"):
        clear_screen()
        print("========================================================================")
        print("|                              DAFTAR AKUN                             |")
        print("========================================================================")
        print("| Info: Silakan isi NIK, Nama, Umur, No. HP, Alamat, Kelurahan / Desa, |")
        print("|       Username, Password, dan Kode Unik akun anda                    |")
        print("========================================================================")
        nik = int(input("NIK              : "))
        nama = str(input("Nama             : "))
        umur = int(input("Umur             : "))
        nohp = int(input("No. HP/WA        : "))
        alamat = str(input("Alamat           : "))
        alamat2 = str(input("Kelurahan / Desa : "))
        username = str(input("Username         : "))
        password = str(input("Password         : "))
        kodeunik = str(input("Kode Unik        : "))
        if nik in database["Account"]:
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            back_to_auth()
        database["Account"][nik] = {}
        database["Account"][nik]["Username"] = username
        database["Account"][nik]["Password"] = password
        if(kodeunik == "dinkes"):
            database["Account"][nik]["Level"] = "dinkes"
        else:
            database["Account"][nik]["Level"] = "user"
        database["Account"][nik]["Nama"] = nama
        database["Account"][nik]["Umur"] = umur
        database["Account"][nik]["NoHP"] = nohp
        database["Account"][nik]["Alamat"] = alamat
        database["Account"][nik]["Alamat2"] = alamat2
        now = datetime.datetime.now()
        database["Account"][nik]["Created"] = (now.day, now.month, now.year, now.hour, now.minute, now.second)
        database["Account"][nik]["Vaksinasi"] = 0
        database["Account"][nik]["Riwayat"] = {}
        print("========================================================================")
        print("| Sukses: Akun berhasil dibuat dan disimpan!                           |")
        print("========================================================================")
        back_to_login()
    elif(selected_register == "2"):
        show_auth()
    else:
        print("========================================================================")
        print("| Error: Pilihan salah!                                                |")
        print("========================================================================")
        back_to_auth_register()

def back_to_auth():
    input("\nTekan Enter untuk kembali...")
    show_auth()

def back_to_auth_register():
    input("\nTekan Enter untuk kembali...")
    auth_register()

def show_login():
    clear_screen()
    print("======================================================================")
    print("|                                LOGIN                               |")
    print("======================================================================")
    print("| [1] Guest                                                          |")
    print("| [2] User                                                           |")
    print("| [3] Dinkes                                                         |")
    print("| [4] Kembali                                                        |")
    print("| [0] Keluar Aplikasi                                                |")
    print("======================================================================")
    selected_login = str(input("Masukkan Pilihan> "))
    if(selected_login == "1"):
        session_akun.insert(0, "guest")
        print("======================================================================")
        print("| Sukses: Anda akan dialihkan ke menu Guest                          |")
        print("======================================================================")
        time.sleep(1.5)
        show_menu()
    elif(selected_login == "2"):
        auth_login("user")
    elif(selected_login == "3"):
        auth_login("dinkes")
    elif(selected_login == "4"):
        show_auth()
    elif(selected_login == "0"):
        close_app()
    else:
        print("======================================================================")
        print("| Error: Pilihan salah!                                              |")
        print("======================================================================")
        back_to_login()

def query_account_login(username, password, level):
    for nik in database["Account"]:
        if(database["Account"][nik]["Username"] == username and database["Account"][nik]["Level"] == level):
            if(database["Account"][nik]["Password"] == password):
                session_akun.insert(0, database["Account"][nik]["Level"])
                session_akun.insert(1, database["Account"][nik]['Username'])
                session_akun.insert(2, database["Account"][nik]['Password'])
                session_akun.insert(3, database["Account"][nik]['Nama'])
                session_akun.insert(4, nik)
                session_akun.insert(5, database["Account"][nik]['Umur'])
                session_akun.insert(6, database["Account"][nik]['NoHP'])
                session_akun.insert(7, database["Account"][nik]['Alamat'])
                session_akun.insert(8, database["Account"][nik]['Alamat2'])
                return "Success"
            else:
                return "Failed"
    return "Not Found"

def auth_login(level):
    clear_screen()
    print("======================================================================")
    print("|               Aplikasi Deteksi Mandiri Dini COVID-19               |")
    print("======================================================================")
    print("| Info: Masukkan Username dan Password Anda                          |")
    print("======================================================================")
    username = str(input("Username : "))
    password = str(input("Password : "))
    status = query_account_login(username, password, level)
    if(status == "Success"):
        if(session_akun[0] == "user"):
            print("======================================================================")
            print("| Sukses: Anda akan dialihkan ke menu User                           |")
            print("======================================================================")
        elif(session_akun[0] == "dinkes"):
            print("======================================================================")
            print("| Sukses: Anda akan dialihkan ke menu Dinkes                         |")
            print("======================================================================")
        time.sleep(1.5)
        show_menu()
    elif(status == "Failed"):
        print("======================================================================")
        print("| Error: Username dan Password salah!                                |")
        print("======================================================================")
        back_to_login()
    elif(status == "Not Found"):
        print("======================================================================")
        print("| Error: Data akun tidak ditemukan!                                  |")
        print("======================================================================")
        back_to_login()

def back_to_login():
    input("\nTekan Enter untuk kembali...")
    show_login()

def show_menu():
    clear_screen()
    print("======================================================================")
    print("|                     APLIKASI VAKSINASI COVID-19                    |")
    print("======================================================================")
    if(session_akun[0] == "guest"):
        print("| Info: Anda masuk sebagai Guest                                     |")
        print("======================================================================")
        print("| [1] Data Vaksin COVID-19                                           |")
        print("| [2] Data Vaksinasi COVID-19                                        |")
        print("| [3] Logout                                                         |")
        print("| [0] Keluar Aplikasi                                                |")
    elif(session_akun[0] == "user"):
        print("| Info: Anda masuk sebagai User                                      |")
        print("======================================================================")
        print("| [1] Data Vaksin COVID-19                                           |")
        print("| [2] Data Vaksinasi COVID-19                                        |")
        print("| [3] Daftar Vaksinasi COVID-19                                      |")
        print("| [4] Riwayat Vaksinasi COVID-19                                     |")
        print("| [5] Logout                                                         |")
        print("| [0] Keluar Aplikasi                                                |")
    elif(session_akun[0] == "dinkes"):
        print("| Info: Anda masuk sebagai Dinkes                                    |")
        print("======================================================================")
        print("| [1] Data Vaksin COVID-19                                           |")
        print("| [2] Data Vaksinasi COVID-19                                        |")
        print("| [3] Proses Vaksinasi COVID-19                                      |")
        print("| [4] Logout                                                         |")
        print("| [0] Keluar Aplikasi                                                |")
    print("======================================================================")
    selected_menu = str(input("Pilih menu> "))
    if(session_akun[0] == "guest"):
        if(selected_menu == "1"):
            data_vaksin()
        elif(selected_menu == "2"):
            data_vaksinasi()
        elif(selected_menu == "3"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_show_menu()
    elif(session_akun[0] == "user"):
        if(selected_menu == "1"):
            data_vaksin()
        elif(selected_menu == "2"):
            data_vaksinasi()
        elif(selected_menu == "3"):
            daftar_vaksinasi()
        elif(selected_menu == "4"):
            riwayat_vaksinasi()
        elif(selected_menu == "5"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_show_menu()
    elif(session_akun[0] == "dinkes"):
        if(selected_menu == "1"):
            data_vaksin()
        elif(selected_menu == "2"):
            data_vaksinasi()
        elif(selected_menu == "3"):
            meja_pertama()
        elif(selected_menu == "4"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_show_menu()

def data_vaksin():
    clear_screen()
    print("=======================================================")
    print("|                 DATA VAKSIN COVID-19                |")
    print("=======================================================")
    indeks = 1
    for i in range(len(database["Vaksin"])):
        print("Vaksin ke-", indeks)
        print("Nama Vaksin :", database["Vaksin"][i]["Nama"])
        print("Produksi    :", database["Vaksin"][i]["Produksi"])
        print("Penggunaan  :", len(database["Vaksin"][i]["Nomor"]))
        print("=======================================================")
        indeks += 1
    if(len(database["Vaksin"]) < 1):
        print("=======================================================")
        print("| Error: Tidak ada data vaksin yang tersedia          |")
        print("=======================================================")
    if(session_akun[0] == "dinkes"):
        print("| [1] Tambah Data Vaksin COVID-19                     |")
        print("| [2] Perbaharui Vaksin COVID-19                      |")
        print("| [3] Hapus Vaksin COVID-19                           |")
        print("| [4] Kembali                                         |")
        print("=======================================================")
        selected_menu = str(input("Pilih menu> "))
        if(selected_menu == "1"):
            nama = str(input("Masukkan Nama Vaksin     : "))
            produksi = str(input("Masukkan Produksi Vaksin : "))
            database["Vaksin"].append({"Nama": nama, "Produksi": produksi, "Nomor": []})
            print("=======================================================")
            print("| Sukses: Data Vaksin berhasil ditambahkan            |")
            print("=======================================================")
        elif(selected_menu == "2"):
            if(len(database["Vaksin"]) < 1):
                print("=======================================================")
                print("| Error: Tidak ada data vaksin yang tersedia          |")
                print("=======================================================")
            else:
                nomor = int(input("Masukkan Nomor Vaksin    : "))
                nama = str(input("Masukkan Nama Vaksin     : "))
                produksi = str(input("Masukkan Produksi Vaksin : "))
                database["Vaksin"][nomor-1]["Nama"] = nama
                database["Vaksin"][nomor-1]["Produksi"] = produksi
                print("=======================================================")
                print("| Sukses: Data Vaksin berhasil diperbaharui           |")
                print("=======================================================")
        elif(selected_menu == "3"):
            if(len(database["Vaksin"]) < 1):
                print("=======================================================")
                print("| Error: Tidak ada data vaksin yang tersedia          |")
                print("=======================================================")
            else:
                nomor = int(input("Masukkan Nomor Vaksin    : "))
                database["Vaksin"].pop(nomor-1)
                print("=======================================================")
                print("| Sukses: Data Vaksin berhasil dihapus                |")
                print("=======================================================")
        elif(selected_menu == "4"):
            show_menu()
        else:
            print("=======================================================")
            print("| Error: Anda memilih menu yang salah!                |")
            print("=======================================================")
        back_to_data_vaksin()
    back_to_show_menu()

def data_vaksinasi():
    clear_screen()
    print("=======================================================")
    print("|                DATA VAKSINASI COVID-19              |")
    print("=======================================================")
    print("Tanggal          : %d/%d/%d" % (database["Vaksinasi"]["Tanggal"][0], database["Vaksinasi"]["Tanggal"][1], database["Vaksinasi"]["Tanggal"][2]))
    print("Jumlah Pendaftar :", len(database["Vaksinasi"]["Daftar"]))
    print("Jumlah Vaksinasi :", len(database["Vaksinasi"]["Data"]))
    print("=======================================================")
    back_to_show_menu()

def back_to_show_menu():
    input("\nTekan 'Enter' untuk kembali...")
    show_menu()

def back_to_data_vaksin():
    input("\nTekan 'Enter' untuk kembali...")
    data_vaksin()

def close_app():
    clear_screen()
    print("=========================================================================")
    print("|                            KELUAR APLIKASI                            |")
    print("=========================================================================")
    print("| Info: Terima kasih telah menggunakan Aplikasi Vaksinasi COVID-19      |")
    print("=========================================================================")
    time.sleep(3)
    exit()

def query_daftar(nik):
    for i in database["Vaksinasi"]["Daftar"]:
        if(i == nik):
            return True
    return False

def insert_daftar(nik):
    database["Vaksinasi"]["Daftar"].append(nik)
    del database["Vaksinasi"]["Tanggal"]
    now = datetime.datetime.now()
    database["Vaksinasi"]["Tanggal"] = (now.day, now.month, now.year)
    return True

def query_meja_pertama(nik):
    for i in database["Vaksinasi"]["Daftar"]:
        if(i == nik):
            return database["Account"][nik]["Vaksinasi"]
    return -1

def insert_meja_kedua(nik, tahap, suhu, tekanan_darah):
    database["Account"][nik]["Riwayat"][tahap+1] = {}
    database["Account"][nik]["Riwayat"][tahap+1]["Suhu"] = suhu
    database["Account"][nik]["Riwayat"][tahap+1]["Tekanan"] = tekanan_darah
    return True

def insert_meja_ketiga(nik, tahap, indeks, nomor_batch_vaksin):
    database["Vaksin"][indeks-1]["Nomor"].append(nomor_batch_vaksin)
    database["Account"][nik]["Riwayat"][tahap+1]["NamaVaksin"] = database["Vaksin"][indeks-1]["Nama"]
    database["Account"][nik]["Riwayat"][tahap+1]["NomorBatch"] = nomor_batch_vaksin
    return True

def insert_meja_keempat(nik, tahap, kipi):
    database["Account"][nik]["Riwayat"][tahap+1]["KIPI"] = kipi
    database["Account"][nik]["Vaksinasi"] += 1
    return True

def daftar_vaksinasi():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    status = query_daftar(session_akun[4])
    if(status == True):
        print("===========================================")
        print("| Error: Data anda telah terdaftar!       |")
        print("===========================================")
    else:
        status = insert_daftar(session_akun[4])
        if(status == True):
            print("===========================================")
            print("| Sukses: Data anda berhasil di daftar    |")
            print("===========================================")
    back_to_show_menu()

def meja_pertama():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|               MEJA PERTAMA              |")
    print("===========================================")
    nik = int(input("Masukkan NIK      : "))
    status = query_meja_pertama(nik)
    if(status >= 0 and status < 3):
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_kedua(nik, status)
    elif(status == 2):
        print("===========================================")
        print("| Error: Anda telah di vaksin sebanyak 2x |")
        print("===========================================")
        back_to_show_menu()
    else:
        print("===========================================")
        print("| Error: Data anda tidak terdaftar!       |")
        print("===========================================")
    back_to_show_menu()

def meja_kedua(nik, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|                MEJA KEDUA               |")
    print("===========================================")
    suhu =  int(input("Masukkan Suhu Tubuh    : "))
    tekanan_darah = int(input("Masukkan Tekanan Darah : "))
    status = insert_meja_kedua(nik, tahap, suhu, tekanan_darah)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_ketiga(nik, tahap)

def meja_ketiga(nik, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|               MEJA KETIGA               |")
    print("===========================================")
    indeks = 1
    for i in range(len(database["Vaksin"])):
        print("Vaksin ke-", indeks)
        print("Nama Vaksin :", database["Vaksin"][i]["Nama"])
        print("Produksi    :", database["Vaksin"][i]["Produksi"])
        print("Penggunaan  :", len(database["Vaksin"][i]["Nomor"]))
        print("===========================================")
        indeks += 1
    nomor_vaksin = int(input("Pilih Vaksin yang ingin digunakan : "))
    nomor_batch_vaksin = int(input("Masukkan Nomor Batch Vaksin       : "))
    status = insert_meja_ketiga(nik, tahap, nomor_vaksin, nomor_batch_vaksin)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_keempat(nik, tahap)

def meja_keempat(nik, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|               MEJA KEEMPAT              |")
    print("===========================================")
    kipi = str(input("Masukkan KIPI : "))
    status = insert_meja_keempat(nik, tahap, kipi)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        final_vaksinasi(nik, tahap)

def final_vaksinasi(nik, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|              DATA VAKSINASI             |")
    print("===========================================")
    print("NIK                :", nik)
    print("Nama               :", database["Account"][nik]["Nama"])
    print("Vaksinasi Ke       :", database["Account"][nik]["Vaksinasi"])
    print("Suhu Tubuh         :", database["Account"][nik]["Riwayat"][tahap+1]["Suhu"])
    print("Tekanan Darah      :", database["Account"][nik]["Riwayat"][tahap+1]["Tekanan"])
    print("Nama Vaksin        :", database["Account"][nik]["Riwayat"][tahap+1]["NamaVaksin"])
    print("Nomor Batch Vaksin :", database["Account"][nik]["Riwayat"][tahap+1]["NomorBatch"])
    print("KIPI               :", database["Account"][nik]["Riwayat"][tahap+1]["KIPI"])
    database["Vaksinasi"]["Data"].append(nik)
    back_to_show_menu()

def riwayat_vaksinasi():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    indeks = query_daftar(session_akun[4])
    if(indeks == True):
        if(database["Account"][session_akun[4]]["Vaksinasi"] == 0):
            print("===========================================")
            print("| Error: Anda belum di vaksin!            |")
            print("===========================================")
        else:
            print("NIK                :", session_akun[4])
            print("Nama               :", database["Account"][session_akun[4]]["Nama"])
            print("Vaksinasi          :", database["Account"][session_akun[4]]["Vaksinasi"])
            print("===========================================")
            for i in database["Account"][session_akun[4]]["Riwayat"]:
                print("Vaksinasi Ke       :", i)
                print("Suhu Tubuh         :", database["Account"][session_akun[4]]["Riwayat"][i]["Suhu"])
                print("Tekanan Darah      :", database["Account"][session_akun[4]]["Riwayat"][i]["Tekanan"])
                print("Nama Vaksin        :", database["Account"][session_akun[4]]["Riwayat"][i]["NamaVaksin"])
                print("Nomor Batch Vaksin :", database["Account"][session_akun[4]]["Riwayat"][i]["NomorBatch"])
                print("KIPI               :", database["Account"][session_akun[4]]["Riwayat"][i]["KIPI"])
            print("===========================================")
    else:
        print("===========================================")
        print("| Error: Data anda tidak terdaftar!       |")
        print("===========================================")
    back_to_show_menu()

if __name__ == "__main__":
    while True:
        show_auth()
