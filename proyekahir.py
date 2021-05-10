import os
from time import sleep
from datetime import datetime
import csv

session_account = {}
session_vaksinasi = {}

csv_filename_accounts = "accounts.csv"
csv_filename_vaksin = "vaksin.csv"
csv_filename_vaksinasi = "vaksinasi.csv"
csv_filename_kritiksaran = "kritiksaran.csv"

def check_file():
    if not os.path.exists(csv_filename_accounts):
        with open(csv_filename_accounts, "w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_vaksin):
        with open(csv_filename_vaksin, "w") as csv_file:
            fieldnames = ["Nama", "Produksi", "Penggunaan"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_vaksinasi):
        with open(csv_filename_vaksinasi, "w") as csv_file:
            fieldnames = ["Timestamp", "NIK", "Suhu", "Tekanan", "Vaksin", "Nomor", "KIPI"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_kritiksaran):
        with open(csv_filename_kritiksaran, "w") as csv_file:
            fieldnames = ["Jenis", "Nama", "Kritik", "Saran"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_auth():
    clear_screen()
    print("========================================================================")
    print("|                            SELAMAT DATANG                            |")
    print("|                                  DI                                  |")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("|                                 OLEH                                 |")
    print("|       KELOMPOK 1 - INFORMATIKA A 2020 - UNIVERSITAS MULAWARMAN       |")
    print("========================================================================")
    print("| [1] Daftar Akun                                                      |")
    print("| [2] Masuk Akun                                                       |")
    print("| [0] Keluar Aplikasi                                                  |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        auth_register()
    elif selected_menu == "2":
        show_login()
    elif selected_menu == "0":
        close_app()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_show_auth()

def back_to_show_auth():
    input("\nTekan 'Enter' untuk kembali...")
    show_auth()

def auth_register():
    clear_screen()
    print("========================================================================")
    print("|                              DAFTAR AKUN                             |")
    print("========================================================================")
    print("| Info: Silakan isi Username, Password, Kode Unik, NIK, Nama, Umur,    |")
    print("|       No. HP, dan Alamat akun anda                                   |")
    print("========================================================================")
    try:
        username = input("Username  : ")
        if len(username) < 4:
            print("========================================================================")
            print("| Error: Username minimal 4 karakter!                                  |")
            print("========================================================================")
            back_to_auth_register()
        password = input("Password  : ")
        if len(password) < 8:
            print("========================================================================")
            print("| Error: Password minimal 8 karakter!                                  |")
            print("========================================================================")
            back_to_auth_register()
        kodeunik = input("Kode Unik : ")
        nik = int(input("NIK       : "))
        nama = input("Nama      : ")
        if len(nama) < 1:
            print("========================================================================")
            print("| Error: Anda tidak dapat mengosongkan nama                           |")
            print("========================================================================")
            back_to_auth_register()
        umur = int(input("Umur      : "))
        nohp = int(input("No. HP    : "))
        alamat = input("Alamat    : ")
        if len(alamat) < 1:
            print("========================================================================")
            print("| Error: Anda tidak dapat mengosongkan alamat                         |")
            print("========================================================================")
            back_to_auth_register()
        now = datetime.now()
        timestamp = "%d/%d/%d %d:%d:%d" % (now.day,now.month,now.year,now.hour,now.minute,now.second)
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        back_to_auth_register()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = False
    for data in akun:
        if data["NIK"] == nik or data["Username"] == username:
            data_found = True
            break
    if data_found == True:
        print("========================================================================")
        print("| Error: Akun tersebut telah didaftarkan!                              |")
        print("========================================================================")
        back_to_show_auth()
    else:
        with open(csv_filename_accounts, mode="a") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if kodeunik == "admin":
                csv_writer.writerow({"Username": username, "Password": password, "Level": kodeunik, "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
            elif kodeunik == "dinkes":
                csv_writer.writerow({"Username": username, "Password": password, "Level": kodeunik, "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
            else:
                csv_writer.writerow({"Username": username, "Password": password, "Level": "pasien", "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
        print("========================================================================")
        print("| Sukses: Akun berhasil dibuat dan disimpan!                           |")
        print("========================================================================")
        back_to_show_login()

def back_to_auth_register():
    input("\nTekan 'Enter' untuk kembali...")
    auth_register()

def show_login():
    clear_screen()
    print("========================================================================")
    print("|                                 MASUK                                |")
    print("========================================================================")
    print("| [1] Pasien                                                           |")
    print("| [2] Dinkes                                                           |")
    print("| [3] Admin                                                            |")
    print("| [4] Lupa Password                                                    |")
    print("| [5] Kembali                                                          |")
    print("| [0] Keluar Aplikasi                                                  |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        auth_login("pasien")
    elif selected_menu == "2":
        auth_login("dinkes")
    elif selected_menu == "3":
        auth_login("admin")
    elif selected_menu == "4":
        forgot_password()
    elif selected_menu == "5":
        show_auth()
    elif selected_menu == "0":
        close_app()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_show_login()

def back_to_show_login():
    input("\nTekan 'Enter' untuk kembali...")
    show_login()

def auth_login(level):
    clear_screen()
    print("========================================================================")
    print("|                                 MASUK                                |")
    print("========================================================================")
    print("| Info: Masukkan Username dan Password Anda                            |")
    print("========================================================================")
    username = input("Username : ")
    password = input("Password : ")
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = []
    indeks = 0
    if level == "pasien":
        for data in akun:
            if data["Username"] == username and data["Level"] == "pasien":
                data_found = akun[indeks]
                break
            indeks += 1
        if len(data_found) > 0:
            if data_found["Password"] == password and data_found["Level"] == "pasien":
                session_account["Username"] = data_found["Username"]
                session_account["Password"] = data_found["Password"]
                session_account["Level"] = data_found["Level"]
                session_account["NIK"] = data_found["NIK"]
                session_account["Nama"] = data_found["Nama"]
                session_account["Umur"] = data_found["Umur"]
                session_account["NoHP"] = data_found["NoHP"]
                session_account["Alamat"] = data_found["Alamat"]
                session_account["Vaksinasi"] = data_found["Vaksinasi"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Pasien                           |")
                print("========================================================================")
                sleep(1.5)
                show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            back_to_show_login()
    elif level == "dinkes":
        for data in akun:
            if data["Username"] == username and data["Level"] == "dinkes":
                data_found = akun[indeks]
                break
            indeks += 1
        if len(data_found) > 0:
            if data_found["Password"] == password and data_found["Level"] == "dinkes":
                session_account["Username"] = data_found["Username"]
                session_account["Password"] = data_found["Password"]
                session_account["Level"] = data_found["Level"]
                session_account["NIK"] = data_found["NIK"]
                session_account["Nama"] = data_found["Nama"]
                session_account["Umur"] = data_found["Umur"]
                session_account["NoHP"] = data_found["NoHP"]
                session_account["Alamat"] = data_found["Alamat"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Dinkes                           |")
                print("========================================================================")
                sleep(1.5)
                show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            back_to_show_login()
    elif level == "admin":
        for data in akun:
            if data["Username"] == username and data["Level"] == "admin":
                data_found = akun[indeks]
                break
            indeks += 1
        if len(data_found) > 0:
            if data_found["Password"] == password and data_found["Level"] == "admin":
                session_account["Username"] = data_found["Username"]
                session_account["Password"] = data_found["Password"]
                session_account["Level"] = data_found["Level"]
                session_account["NIK"] = data_found["NIK"]
                session_account["Nama"] = data_found["Nama"]
                session_account["Umur"] = data_found["Umur"]
                session_account["NoHP"] = data_found["NoHP"]
                session_account["Alamat"] = data_found["Alamat"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Admin                            |")
                print("========================================================================")
                sleep(1.5)
                show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            back_to_show_login()

def forgot_password():
    clear_screen()
    print("========================================================================")
    print("|                             LUPA PASSWORD                            |")
    print("========================================================================")
    print("| Info: Masukkan Username dan NIK Anda                                 |")
    print("========================================================================")
    try:
        username = input("Username : ")
        nik = int(input("NIK      : "))
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        back_to_forgot_password()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = False
    indeks = 0
    for data in akun:
        if data["Username"] == username or data["NIK"] == nik:
            data_found = True
            break
        indeks += 1
    if data_found == True:
        data_match = False
        for data in akun:
            if data["Username"] == username and data["NIK"] == nik:
                akun[indeks]["Password"] = "vaksinasi"
                print("========================================================================")
                print("| Sukses: Password berhasil di reset! New Password : vaksinasi         |")
                print("========================================================================")
                data_match = True
                break
            indeks += 1
        if data_match == False:
            print("========================================================================")
            print("| Error: Username dan NIK salah!                                       |")
            print("========================================================================")
        else:
            with open(csv_filename_accounts, mode="w") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in akun:
                    csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
    else:
        print("========================================================================")
        print("| Error: Data akun tidak ditemukan!                                    |")
        print("========================================================================")
    back_to_show_login()

def back_to_forgot_password():
    input("\nTekan 'Enter' untuk kembali...")
    forgot_password()

def show_menu():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    if session_account["Level"] == "pasien":
        print("| Info: Anda masuk sebagai Pasien                                      |")
        print("========================================================================")
        print("| [1] Data Vaksin COVID-19                                             |")
        print("| [2] Data Vaksinasi COVID-19                                          |")
        print("| [3] Daftar Vaksinasi COVID-19                                        |")
        print("| [4] Riwayat Vaksinasi COVID-19                                       |")
        print("| [5] Tentang Aplikasi                                                 |")
        print("| [6] Kritik dan Saran                                                 |")
        print("| [7] Pengaturan Akun                                                  |")
        print("| [8] Logout                                                           |")
        print("| [0] Keluar Aplikasi                                                  |")
    elif session_account["Level"] == "dinkes":
        print("| Info: Anda masuk sebagai Dinkes                                      |")
        print("========================================================================")
        print("| [1] Data Vaksin COVID-19                                             |")
        print("| [2] Data Vaksinasi COVID-19                                          |")
        print("| [3] Proses Vaksinasi COVID-19                                        |")
        print("| [4] Tentang Aplikasi                                                 |")
        print("| [5] Lihat Daftar Kritik dan Saran                                    |")
        print("| [6] Kritik dan Saran                                                 |")
        print("| [7] Pengaturan Akun                                                  |")
        print("| [8] Logout                                                           |")
        print("| [0] Keluar Aplikasi                                                  |")
    elif session_account["Level"] == "admin":
        print("| Info: Anda masuk sebagai Admin                                       |")
        print("========================================================================")
        print("| [1]  Lihat Daftar Pengguna                                           |")
        print("| [2]  Buat Pengguna Baru                                              |")
        print("| [3]  Edit Pengguna                                                   |")
        print("| [4]  Hapus Pengguna                                                  |")
        print("| [5]  Urut Pengguna                                                   |")
        print("| [6]  Cari Pengguna                                                   |")
        print("| [7]  Data Vaksin COVID-19                                            |")
        print("| [8]  Data Vaksinasi COVID-19                                         |")
        print("| [9]  Tentang Aplikasi                                                |")
        print("| [10] Lihat Daftar Kritik dan Saran                                   |")
        print("| [11] Pengaturan Akun                                                 |")
        print("| [12] Logout                                                          |")
        print("| [0]  Keluar Aplikasi                                                 |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    if session_account["Level"] == "pasien":
        if selected_menu == "1":
            data_vaksin()
        elif selected_menu == "2":
            data_vaksinasi()
        elif selected_menu == "3":
            daftar_vaksinasi()
        elif selected_menu == "4":
            riwayat_vaksinasi()
        elif selected_menu == "5":
            tentang_aplikasi()
        elif selected_menu == "6":
            kritikdansaran()
        elif selected_menu == "7":
            pengaturan_akun()
        elif selected_menu == "8":
            session_account.clear()
            show_login()
        elif selected_menu == "0":
            close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_show_menu()
    elif session_account["Level"] == "dinkes":
        if selected_menu == "1":
            data_vaksin()
        elif selected_menu == "2":
            data_vaksinasi()
        elif selected_menu == "3":
            meja_pertama()
        elif selected_menu == "4":
            tentang_aplikasi()
        elif selected_menu == "5":
            show_kritiksaran()
        elif selected_menu == "6":
            kritikdansaran()
        elif selected_menu == "7":
            pengaturan_akun()
        elif selected_menu == "8":
            show_login()
        elif selected_menu == "0":
            close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_show_menu()
    elif session_account["Level"] == "admin":
        if selected_menu == "1":
            show_account()
        elif selected_menu == "2":
            create_account()
        elif selected_menu == "3":
            edit_account()
        elif selected_menu == "4":
            delete_account()
        elif selected_menu == "5":
            sort_account()
        elif selected_menu == "6":
            search_account()
        elif selected_menu == "7":
            data_vaksin()
        elif selected_menu == "8":
            data_vaksinasi()
        elif selected_menu == "9":
            tentang_aplikasi()
        elif selected_menu == "10":
            show_kritiksaran()
        elif selected_menu == "11":
            pengaturan_akun()
        elif selected_menu == "12":
            show_login()
        elif selected_menu == "0":
            close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_show_menu()

def back_to_show_menu():
    input("\nTekan 'Enter' untuk kembali...")
    show_menu()

def data_vaksin():
    clear_screen()
    print("========================================================================")
    print("|                         DATA VAKSIN COVID-19                         |")
    print("========================================================================")
    vaksin = []
    with open(csv_filename_vaksin, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksin.append(row)
    if session_account["Level"] == "pasien" or session_account["Level"] == "admin":
        if len(vaksin) > 0:
            indeks = 1
            for data in vaksin:
                print("| Vaksin ke-%d" % indeks)
                print("| Nama Vaksin :", data["Nama"])
                print("| Produksi    :", data["Produksi"])
                print("| Penggunaan  :", data["Penggunaan"])
                print("========================================================================")
                indeks += 1
        else:
            print("========================================================================")
            print("| Error: Tidak ada data vaksin yang tersedia!                          |")
            print("========================================================================")
    elif session_account["Level"] == "dinkes":
        print("| [1] Lihat Data Vaksin COVID-19                                       |")
        print("| [2] Tambah Data Vaksin COVID-19                                      |")
        print("| [3] Edit Vaksin COVID-19                                             |")
        print("| [4] Hapus Vaksin COVID-19                                            |")
        print("| [5] Urut Vaksin COVID-19                                             |")
        print("| [6] Cari Vaksin COVID-19                                             |")
        print("| [7] Kembali                                                          |")
        print("========================================================================")
        selected_menu = input("Pilih Menu> ")
        if selected_menu == "1":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            if len(vaksin) > 0:
                indeks = 1
                for data in vaksin:
                    print("| Vaksin ke-%d" % indeks)
                    print("| Nama Vaksin :", data["Nama"])
                    print("| Produksi    :", data["Produksi"])
                    print("| Penggunaan  :", data["Penggunaan"])
                    print("========================================================================")
                    indeks += 1
            else:
                print("========================================================================")
                print("| Error: Tidak ada data vaksin yang tersedia!                          |")
                print("========================================================================")
        elif selected_menu == "2":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            nama = input("Masukkan Nama Vaksin     : ")
            produksi = input("Masukkan Produksi Vaksin : ")
            with open(csv_filename_vaksin, mode="a") as csv_file:
                fieldnames = ["Nama", "Produksi", "Penggunaan"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Nama": nama, "Produksi": produksi, "Penggunaan": 0})
            print("========================================================================")
            print("| Sukses: Data Vaksin berhasil ditambahkan                             |")
            print("========================================================================")
        elif selected_menu == "3":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            indeks = 1
            for data in vaksin:
                print("| Vaksin ke-%d" % indeks)
                print("| Nama Vaksin :", data["Nama"])
                print("| Produksi    :", data["Produksi"])
                print("| Penggunaan  :", data["Penggunaan"])
                print("========================================================================")
                indeks += 1
            if len(vaksin) < 1:
                print("========================================================================")
                print("| Error: Tidak ada data vaksin yang tersedia!                          |")
                print("========================================================================")
            else:
                try:
                    nomor = int(input("Masukkan Nomor Vaksin    : "))
                    nama = input("Masukkan Nama Vaksin     : ")
                    produksi = input("Masukkan Produksi Vaksin : ")
                    vaksin[nomor-1]["Nama"] = nama
                    vaksin[nomor-1]["Produksi"] = produksi
                    with open(csv_filename_vaksin, mode="w") as csv_file:
                        fieldnames = ["Nama", "Produksi", "Penggunaan"]
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for new_data in vaksin:
                            csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"]})
                    print("========================================================================")
                    print("| Sukses: Data Vaksin berhasil diperbaharui                            |")
                    print("========================================================================")
                except ValueError:
                    print("========================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                    print("========================================================================")
        elif selected_menu == "4":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            indeks = 1
            for data in vaksin:
                print("| Vaksin ke-%d" % indeks)
                print("| Nama Vaksin :", data["Nama"])
                print("| Produksi    :", data["Produksi"])
                print("| Penggunaan  :", data["Penggunaan"])
                print("========================================================================")
                indeks += 1
            if len(vaksin) < 1:
                print("========================================================================")
                print("| Error: Tidak ada data vaksin yang tersedia!                          |")
                print("========================================================================")
            else:
                try:
                    nomor = int(input("Masukkan Nomor Vaksin    : "))
                    vaksin.pop(nomor-1)
                    with open(csv_filename_vaksin, mode="w") as csv_file:
                        fieldnames = ["Nama", "Produksi", "Penggunaan"]
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for new_data in vaksin:
                            csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"]})
                    print("========================================================================")
                    print("| Sukses: Data Vaksin berhasil dihapus                                 |")
                    print("========================================================================")
                except ValueError:
                    print("========================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                    print("========================================================================")
        elif selected_menu == "5":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            print("| [1] Nama Vaksin                                                      |")
            print("| [2] Produksi Vaksin                                                  |")
            print("| [3] Penggunaan Vaksin                                                |")
            print("| [4] Kembali                                                          |")
            print("========================================================================")
            sorting = ""
            selected_menu = input("Pilih Menu> ")
            if selected_menu == "1":
                sorting = "Nama"
            elif selected_menu == "2":
                sorting = "Produksi"
            elif selected_menu == "3":
                sorting = "Penggunaan"
            elif selected_menu == "4":
                data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_to_data_vaksin()
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            print("| [1] Metode Bubble Sort                                               |")
            print("| [2] Metode Selection Sort                                            |")
            print("| [3] Metode Insertion Sort                                            |")
            print("| [4] Metode Quick Sort                                                |")
            print("| [5] Metode Merge Sort                                                |")
            print("| [6] Metode Shell Sort                                                |")
            print("| [7] Kembali                                                          |")
            print("========================================================================")
            metode = ""
            selected_menu = input("Pilih Menu> ")
            if selected_menu == "1":
                metode = "Bubble"
            elif selected_menu == "2":
                metode = "Selection"
            elif selected_menu == "3":
                metode = "Insertion"
            elif selected_menu == "4":
                metode = "Quick"
            elif selected_menu == "5":
                metode = "Merge"
            elif selected_menu == "6":
                metode = "Shell"
            elif selected_menu == "7":
                data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_to_data_vaksin()
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            print("| [1] Secara Ascending                                                 |")
            print("| [2] Secara Descending                                                |")
            print("| [3] Kembali                                                          |")
            print("========================================================================")
            selected_menu = input("Pilih Menu> ")
            order = ""
            if selected_menu == "1":
                order = "Ascending"
            elif selected_menu == "2":
                order = "Descending"
            elif selected_menu == "3":
                data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_to_data_vaksin()
            if len(vaksin) < 1:
                print("========================================================================")
                print("| Error: Tidak ada data vaksin yang tersedia!                          |")
                print("========================================================================")
            else:
                datasort = []
                indeks = 0
                for data in vaksin:
                    if sorting == "Nama":
                        datasort.append([data["Nama"], indeks])
                    elif sorting == "Produksi":
                        datasort.append([data["Produksi"], indeks])
                    elif sorting == "Penggunaan":
                        datasort.append([data["Penggunaan"], indeks])
                    indeks += 1
                if metode == "Bubble":
                    bubbleSort(datasort, order)
                elif metode == "Selection":
                    selectionSort(datasort, len(datasort), order)
                elif metode == "Insertion":
                    insertionSort(datasort, order)
                elif metode == "Quick":
                    quickSort(datasort, 0, len(datasort)-1, order)
                elif metode == "Merge":
                    mergeSort(datasort, 0, len(datasort)-1, order)
                elif metode == "Shell":
                    shellSort(datasort, len(datasort), order)
                old_vaksin = vaksin.copy()
                vaksin.clear()
                for i in range(len(datasort)):
                    vaksin.append({"Nama": old_vaksin[datasort[i][1]]["Nama"], "Produksi": old_vaksin[datasort[i][1]]["Produksi"], "Penggunaan": old_vaksin[datasort[i][1]]["Penggunaan"]})
                with open(csv_filename_vaksin, mode="w") as csv_file:
                    fieldnames = ["Nama", "Produksi", "Penggunaan"]
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for new_data in vaksin:
                        csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"]})
                print("========================================================================")
                print("| Sukses: Data Vaksin berhasil diurutkan                               |")
                print("========================================================================")
        elif selected_menu == "6":
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            print("| [1] Nama Vaksin                                                      |")
            print("| [2] Produksi Vaksin                                                  |")
            print("| [3] Penggunaan Vaksin                                                |")
            print("| [4] Kembali                                                          |")
            print("========================================================================")
            searching = ""
            selected_menu = input("Pilih Menu> ")
            if selected_menu == "1":
                searching = "Nama"
            elif selected_menu == "2":
                searching = "Produksi"
            elif selected_menu == "3":
                searching = "Penggunaan"
            elif selected_menu == "4":
                data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_to_data_vaksin()
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            print("| [1] Metode Linear Search                                             |")
            print("| [2] Metode Binary Search                                             |")
            if searching == "Penggunaan":
                print("| [3] Metode Interpolation Search                                      |")
                print("| [4] Kembali                                                          |")
            else:
                print("| [3] Kembali                                                          |")
            print("========================================================================")
            metode = ""
            selected_menu = input("Pilih Menu> ")
            if selected_menu == "1":
                metode = "Linear"
            elif selected_menu == "2":
                metode = "Binary"
            if searching == "Penggunaan":
                if selected_menu == "3":
                    metode = "Interpolation"
                elif selected_menu == "4":
                    data_vaksin()
                else:
                    print("========================================================================")
                    print("| Error: Anda memilih menu yang salah!                                 |")
                    print("========================================================================")
                    back_to_data_vaksin()
            else:
                if selected_menu == "3":
                    data_vaksin()
                else:
                    print("========================================================================")
                    print("| Error: Anda memilih menu yang salah!                                 |")
                    print("========================================================================")
                    back_to_data_vaksin()
            clear_screen()
            print("========================================================================")
            print("|                         DATA VAKSIN COVID-19                         |")
            print("========================================================================")
            if searching == "Penggunaan":
                try:
                    search = int(input("Data yang ingin dicari> "))
                    if search < 1:
                        print("========================================================================")
                        print("| Gagal: Tidak dapat mencari data kurang dari 1!                       |")
                        print("========================================================================")
                        back_to_data_vaksin()
                except ValueError:
                    print("========================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                    print("========================================================================")
                    back_to_data_vaksin()
            else:
                search = input("Data yang ingin dicari> ")
            datasort = []
            datasearch = []
            indeks = 0
            for data in vaksin:
                if searching == "Nama":
                    datasort.append([data["Nama"].lower(), indeks])
                elif searching == "Produksi":
                    datasort.append([data["Produksi"].lower(), indeks])
                elif searching == "Penggunaan":
                    datasort.append([data["Penggunaan"], indeks])
                indeks += 1
            quickSort(datasort, 0, len(datasort)-1, "Ascending")
            for i in range(len(datasort)):
                datasearch.append(datasort[i][0])
            if metode == "Linear":
                result = linearSearch(datasearch, len(datasearch), search.lower())
            elif metode == "Binary":
                result = binarySearch(datasearch, search.lower(), 0, len(datasearch) - 1)
            elif metode == "Interpolation":
                result = interpolationSearch(datasearch, 0, len(datasearch) - 1, search)
            if result != -1:
                print("========================================================================")
                print("| Sukses: Data Vaksin ditemukan!                                       |")
                print("========================================================================")
                print("| Nama Vaksin :", data[datasort[result][1]]["Nama"])
                print("| Produksi    :", data[datasort[result][1]]["Produksi"])
                print("| Penggunaan  :", data[datasort[result][1]]["Penggunaan"])
                print("========================================================================")
            else:
                print("========================================================================")
                print("| Gagal: Data Vaksin tidak ditemukan!                                  |")
                print("========================================================================")
        elif selected_menu == "7":
            show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
        back_to_data_vaksin()

def back_to_data_vaksin():
    input("\nTekan 'Enter' untuk kembali...")
    data_vaksin()

def data_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                        DATA VAKSINASI COVID-19                       |")
    print("========================================================================")
    now = datetime.now()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    vaksinasi = []
    with open(csv_filename_vaksinasi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksinasi.append(row)
    count_daftar = 0
    for data in akun:
        if data["Vaksinasi"] == "True":
            count_daftar += 1
    print("Tangal Waktu     : %d/%d/%d - %d:%d:%d" % (now.day, now.month, now.year, now.hour, now.minute, now.second))
    print("Jumlah Pendaftar :", count_daftar)
    print("Jumlah Vaksinasi :", len(vaksinasi))
    print("========================================================================")
    back_to_show_menu()

def daftar_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    if session_account["Vaksinasi"] == "False":
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        indeks = 0
        for data in akun:
            if data["NIK"] == session_account["NIK"]:
                akun[indeks]["Vaksinasi"] = "True"
                session_account["Vaksinasi"] = "True"
                print("========================================================================")
                print("| Sukses: Data anda berhasil di daftar                                 |")
                print("========================================================================")
                break
            indeks += 1
        with open(csv_filename_accounts, mode="w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for new_data in akun:
                csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
    else:
        print("========================================================================")
        print("| Error: Data anda telah terdaftar!                                    |")
        print("========================================================================")
    back_to_show_menu()

def meja_pertama():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                             MEJA PERTAMA                             |")
    print("========================================================================")
    try:
        nik = int(input("Masukkan NIK : "))
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_pertama()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    vaksinasi = []
    with open(csv_filename_vaksinasi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksinasi.append(row)
    count_vaksinasi = 0
    for data in vaksinasi:
        if data["NIK"] == nik:
            count_vaksinasi += 1
    data_found = False
    for data in akun:
        if data["NIK"] == nik and data["Vaksinasi"] == "True":
            session_vaksinasi["Nama"] = data["Nama"]
            data_found = True
            break
    if data_found == True:
        if count_vaksinasi == 2:
            print("========================================================================")
            print("| Error: Anda telah di vaksin sebanyak 2x                              |")
            print("========================================================================")
        else:
            print("========================================================================")
            session_vaksinasi["Vaksinasi"] = count_vaksinasi
            session_vaksinasi["NIK"] = nik
            input("\nTekan 'Enter' untuk melanjutkan...")
            meja_kedua()
    else:
        print("========================================================================")
        print("| Error: Data anda tidak terdaftar!                                    |")
        print("========================================================================")
    back_to_show_menu()

def meja_kedua():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                              MEJA KEDUA                              |")
    print("========================================================================")
    try:
        suhu = float(input("Masukkan Suhu Tubuh    : "))
        tekanan_darah = int(input("Masukkan Tekanan Darah : "))
        print("========================================================================")
        session_vaksinasi["Suhu"] = suhu
        session_vaksinasi["Tekanan"] = tekanan_darah
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_ketiga()
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_kedua()        

def meja_ketiga():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                              MEJA KETIGA                             |")
    print("========================================================================")
    vaksin = []
    with open(csv_filename_vaksin, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksin.append(row)
    indeks = 1
    for data in vaksin:
        print("| Vaksin ke-%d" % indeks)
        print("| Nama Vaksin :", data["Nama"])
        print("| Produksi    :", data["Produksi"])
        print("| Penggunaan  :", data["Penggunaan"])
        print("========================================================================")
        indeks += 1
    if len(vaksin) < 1:
        print("========================================================================")
        print("| Error: Tidak ada data vaksin yang tersedia!                          |")
        print("========================================================================")
        back_to_show_menu()
    else:
        try:
            nomor_vaksin = int(input("Pilih Vaksin yang ingin digunakan : "))
            nomor_batch_vaksin = int(input("Masukkan Nomor Batch Vaksin       : "))
            print("========================================================================")
            session_vaksinasi["Vaksin"] = data[nomor_vaksin-1]["Nama"]
            session_vaksinasi["Nomor"] = nomor_batch_vaksin
            input("\nTekan 'Enter' untuk melanjutkan...")
            meja_keempat()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            input("\nTekan 'Enter' untuk melanjutkan...")
            meja_ketiga()        

def meja_keempat():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                             MEJA KEEMPAT                             |")
    print("========================================================================")
    kipi = input("Masukkan KIPI : ")
    print("========================================================================")
    session_vaksinasi["KIPI"] = kipi
    input("\nTekan 'Enter' untuk melanjutkan...")
    final_vaksinasi()

def final_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                            DATA VAKSINASI                            |")
    print("========================================================================")
    print("NIK                :", session_vaksinasi["NIK"])
    print("Nama               :", session_vaksinasi["Nama"])
    print("Vaksinasi Ke       :", session_vaksinasi["Vaksinasi"])
    print("Suhu Tubuh         :", session_vaksinasi["Suhu"])
    print("Tekanan Darah      :", session_vaksinasi["Tekanan"])
    print("Nama Vaksin        :", session_vaksinasi["Vaksin"])
    print("Nomor Batch Vaksin :", session_vaksinasi["Nomor"])
    print("KIPI               :", session_vaksinasi["KIPI"])
    print("========================================================================")
    now = datetime.now()
    timestamp = "%d/%d/%d %d:%d:%d" % (now.day,now.month,now.year,now.hour,now.minute,now.second)
    with open(csv_filename_vaksinasi, mode="a") as csv_file:
        fieldnames = ["Timestamp", "NIK", "Suhu", "Tekanan", "Vaksin", "Nomor", "KIPI"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({"Timestamp": timestamp, "NIK": session_vaksinasi["NIK"], "Suhu": session_vaksinasi["Suhu"], "Tekanan": session_vaksinasi["Tekanan"], "Vaksin": session_vaksinasi["Vaksin"], "Nomor": session_vaksinasi["Nomor"], "KIPI": session_vaksinasi["KIPI"]})
    session_vaksinasi.clear()
    back_to_show_menu()

def riwayat_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    vaksinasi = []
    with open(csv_filename_vaksinasi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksinasi.append(row)
    count_vaksinasi = 0
    for data in vaksinasi:
        if data["NIK"] == session_account["NIK"]:
            count_vaksinasi += 1
    if session_account["Vaksinasi"] == "True":
        if count_vaksinasi == 0:
            print("========================================================================")
            print("| Error: Anda belum di vaksin!                                         |")
            print("========================================================================")
        else:
            print("NIK                :", session_account["NIK"])
            print("Nama               :", session_account["Nama"])
            print("Vaksinasi          :", count_vaksinasi)
            print("========================================================================")
            indeks = 1
            for data in vaksinasi:
                if data["NIK"] == session_account["NIK"]:
                    print("Vaksinasi Ke-%d" % indeks)
                    print("Timestamp          :", data["Timestamp"])
                    print("Suhu Tubuh         :", data["Suhu"])
                    print("Tekanan Darah      :", data["Tekanan"])
                    print("Nama Vaksin        :", data["Vaksin"])
                    print("Nomor Batch Vaksin :", data["Nomor"])
                    print("KIPI               :", data["KIPI"])
                print("========================================================================")
                indeks += 1
    else:
        print("========================================================================")
        print("| Error: Anda belum daftar vaksinasi!                                  |")
        print("========================================================================")
    back_to_show_menu()

def close_app():
    clear_screen()
    print("========================================================================")
    print("|                            KELUAR APLIKASI                           |")
    print("========================================================================")
    print("| Info: Terima kasih telah menggunakan Aplikasi Vaksinasi COVID-19     |")
    print("========================================================================")
    sleep(3)
    exit()

def tentang_aplikasi():
    clear_screen()
    print("========================================================================")
    print("|                           TENTANG APLIKASI                           |")
    print("========================================================================")
    print("| Nama Aplikasi        : Vaksinasi COVID-19                            |")
    print("| Versi                : 1.0                                           |")
    print("| Pengembang           : Andi Alfian Bahtiar  (2009106002)             |")
    print("|                      : Muh. Fathir Fahrezah (2009106024)             |")
    print("|                      : Fathan Ghoji Adzikra (2009106044)             |")
    print("| Donasi Pengembangan  : 056301058860507 (BRI)                         |")
    print("|                      : 7995048523 (BCA)                              |")
    print("|                      : 4132282159 (Permata)                          |")
    print("|                      : 1480016496716 (Mandiri)                       |")
    print("|                      : 90020219079 (Jenius)                          |")
    print("|                      : 085346816962 (Dana/OVO/Gopay)                 |")
    print("|                                                                      |")
    print("|              Hak Cipta © 2021 Vaksinasi COVID-19                     |")
    print("========================================================================")
    back_to_show_menu()

def pengaturan_akun():
    clear_screen()
    print("========================================================================")
    print("|                            PENGATURAN AKUN                           |")
    print("========================================================================")
    print("| [1] Ganti Password                                                   |")
    print("| [2] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        clear_screen()
        print("========================================================================")
        print("|                            PENGATURAN AKUN                           |")
        print("========================================================================")
        print("| Info: Masukkan Password Lama dan ganti dengan Password Baru          |")
        print("========================================================================")
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = []
        indeks = 0
        for data in akun:
            if data["Username"] == session_account["Username"]:
                data_found = akun[indeks]
                break
            indeks += 1
        password_lama = input("Password Lama            : ")
        if data_found["Password"] == password_lama:
            password_baru = input("Password Baru            : ")
            if len(password_baru) < 8:
                print("========================================================================")
                print("| Error: Password Baru minimal 8 karakter!                             |")
                print("========================================================================")
                back_to_pengaturan_akun()
            konfirmasi_password_baru = input("Konfirmasi Password Baru : ")
            if len(konfirmasi_password_baru) < 8:
                print("========================================================================")
                print("| Error: Password Baru minimal 8 karakter!                             |")
                print("========================================================================")
                back_to_pengaturan_akun()
            if password_baru == password_lama or konfirmasi_password_baru == password_lama:
                print("========================================================================")
                print("| Error: Password Baru tidak boleh sama dengan Password Lama           |")
                print("========================================================================")
                back_to_pengaturan_akun()
            elif password_baru == konfirmasi_password_baru:
                indeks = 0
                for data in akun:
                    if data["Username"] == session_account["Username"]:
                        akun[indeks]["Password"] = password_baru
                        session_account["Password"] = password_baru
                        print("========================================================================")
                        print("| Sukses: Password berhasil di update!                                 |")
                        print("========================================================================")
                        break
                    indeks += 1
            else:
                print("========================================================================")
                print("| Error: Password dan Konfirmasi Password berbeda!                     |")
                print("========================================================================")
                back_to_pengaturan_akun()
            with open(csv_filename_accounts, mode="w") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in akun:
                    csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
            back_to_show_menu()
        else:
            print("========================================================================")
            print("| Error: Password Lama anda salah!                                     |")
            print("========================================================================")
            back_to_pengaturan_akun()
    elif selected_menu == "2":
        show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_pengaturan_akun()

def back_to_pengaturan_akun():
    input("\nTekan 'Enter' untuk kembali...")
    pengaturan_akun()

def kritikdansaran():
    clear_screen()
    print("========================================================================")
    print("|                           KRITIK DAN SARAN                           |")
    print("========================================================================")
    if session_account["Level"] == "pasien":
        print("| [1] Developer                                                        |")
        print("| [2] Dinkes                                                           |")
        print("| [3] Kembali                                                          |")
    elif session_account["Level"] == "dinkes":
        print("| [1] Developer                                                        |")
        print("| [2] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    if session_account["Level"] == "pasien":
        if selected_menu == "1":
            kritikdansaran_developer()
        elif selected_menu == "2":
            kritikdansaran_dinkes()
        elif selected_menu == "3":
            show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_kritikdansaran()
    elif session_account["Level"] == "dinkes":
        if selected_menu == "1":
            kritikdansaran_developer()
        elif selected_menu == "2":
            show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_kritikdansaran()

def back_to_kritikdansaran():
    input("\nTekan 'Enter' untuk kembali...")
    kritikdansaran()

def kritikdansaran_developer():
    clear_screen()
    print("========================================================================")
    print("|                           KRITIK DAN SARAN                           |")
    print("========================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Developer               |")
    print("========================================================================")
    kritik = input("Kritik : ")
    saran = input("Saran  : ")
    if len(kritik) > 0 or len(saran) > 0:
        if session_account["Level"] == "pasien":
            with open(csv_filename_kritiksaran, mode="a") as csv_file:
                fieldnames = ["Jenis", "Nama", "Kritik", "Saran"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Jenis": "Developer", "Nama": session_account["Nama"], "Kritik": kritik, "Saran": saran})
        elif session_account["Level"] == "dinkes":
            with open(csv_filename_kritiksaran, mode="a") as csv_file:
                fieldnames = ["Jenis", "Nama", "Kritik", "Saran"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Jenis": "Developer", "Nama": session_account["Nama"], "Kritik": kritik, "Saran": saran})
        print("========================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                          |")
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Kritik atau saran harus diisi!                                |")
        print("========================================================================")
    back_to_show_menu()

def kritikdansaran_dinkes():
    clear_screen()
    print("========================================================================")
    print("|                           KRITIK DAN SARAN                           |")
    print("========================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Dinkes                  |")
    print("========================================================================")
    kritik = input("Kritik : ")
    saran = input("Saran  : ")
    if len(kritik) > 0 or len(saran) > 0:
        if session_account["Level"] == "pasien":
            with open(csv_filename_kritiksaran, mode="a") as csv_file:
                fieldnames = ["Jenis", "Nama", "Kritik", "Saran"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Jenis": "Dinkes", "Nama": session_account["Nama"], "Kritik": kritik, "Saran": saran})
            print("========================================================================")
            print("| Sukses: Kritik dan saran berhasil disimpan!                          |")
            print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Kritik atau saran harus diisi!                                |")
        print("========================================================================")
    back_to_show_menu()

def show_kritiksaran():
    clear_screen()
    print("========================================================================")
    if session_account["Level"] == "dinkes":
        print("|                        KRITIK DAN SARAN DINKES                       |")
    elif session_account["Level"] == "admin":
        print("|                      KRITIK DAN SARAN DEVELOPER                      |")
    print("========================================================================")
    kritik_saran = []
    with open(csv_filename_kritiksaran, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            kritik_saran.append(row)
    if len(kritik_saran) > 0:
        for data in kritik_saran:
            if session_account["Level"] == "dinkes":
                if data["Jenis"] == "Dinkes":
                    print("| Nama   :", data["Nama"])
                    print("| Kritik :", data["Kritik"])
                    print("| Saran  :", data["Saran"])
            elif session_account["Level"] == "admin":
                if data["Jenis"] == "Developer":
                    print("| Nama   :", data["Nama"])
                    print("| Kritik :", data["Kritik"])
                    print("| Saran  :", data["Saran"])
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Tidak ada data ditemukan!                                     |")
        print("========================================================================")
    back_to_show_menu()

def show_account():
    clear_screen()
    print("========================================================================")
    print("|                         DAFTAR AKUN PENGGUNA                         |")
    print("========================================================================")
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    if len(akun) > 0:
        for data in akun:
            print("| Username  :", data["Username"])
            print("| Password  :", data["Password"])
            print("| Level     :", data["Level"])
            print("| NIK       :", data["NIK"])
            print("| Nama      :", data["Nama"])
            print("| Umur      :", data["Umur"])
            print("| No HP     :", data["NoHP"])
            print("| Alamat    :", data["Alamat"])
            print("| Vaksinasi :", data["Vaksinasi"])
            print("| Created   :", data["Created"])
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Tidak ada data pengguna ditemukan!                            |")
        print("========================================================================")
    back_to_show_menu()

def create_account():
    clear_screen()
    print("========================================================================")
    print("|                          BUAT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| Info: Silakan isi Username, Password, Kode Unik, NIK, Nama, Umur,    |")
    print("|       No. HP, dan Alamat akun anda                                   |")
    print("========================================================================")
    try:
        username = input("Username  : ")
        if len(username) < 4:
            print("========================================================================")
            print("| Error: Username minimal 4 karakter!                                  |")
            print("========================================================================")
            back_to_auth_register()
        password = input("Password  : ")
        if len(password) < 8:
            print("========================================================================")
            print("| Error: Password minimal 8 karakter!                                  |")
            print("========================================================================")
            back_to_auth_register()
        kodeunik = input("Kode Unik : ")
        nik = int(input("NIK       : "))
        nama = input("Nama      : ")
        if len(nama) < 1:
            print("========================================================================")
            print("| Error: Anda tidak dapat mengosongkan Nama                           |")
            print("========================================================================")
            back_to_auth_register()
        umur = int(input("Umur      : "))
        nohp = int(input("No. HP    : "))
        alamat = input("Alamat    : ")
        if len(alamat) < 1:
            print("========================================================================")
            print("| Error: Anda tidak dapat mengosongkan Alamat                         |")
            print("========================================================================")
            back_to_auth_register()
        now = datetime.now()
        timestamp = "%d/%d/%d %d:%d:%d" % (now.day,now.month,now.year,now.hour,now.minute,now.second)
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        back_to_show_menu()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = False
    for data in akun:
        if data["NIK"] == nik or data["Username"] == username:
            data_found = True
            break
    if data_found == True:
        print("========================================================================")
        print("| Error: Akun tersebut telah didaftarkan!                              |")
        print("========================================================================")
        back_to_show_menu()
    with open(csv_filename_accounts, mode="a") as csv_file:
        fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if kodeunik == "admin":
            csv_writer.writerow({"Username": username, "Password": password, "Level": kodeunik, "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
        elif kodeunik == "dinkes":
            csv_writer.writerow({"Username": username, "Password": password, "Level": kodeunik, "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
        else:
            csv_writer.writerow({"Username": username, "Password": password, "Level": "pasien", "NIK": nik, "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp})
        print("========================================================================")
        print("| Sukses: Akun Baru berhasil dibuat dan disimpan!                      |")
        print("========================================================================")
    back_to_show_menu()

def edit_account():
    clear_screen()
    print("========================================================================")
    print("|                          EDIT AKUN PENGGUNA                          |")
    print("========================================================================")
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    for data in akun:
        print("| Username  :", data["Username"])
        print("| Password  :", data["Password"])
        print("| Level     :", data["Level"])
        print("| NIK       :", data["NIK"])
        print("| Nama      :", data["Nama"])
        print("| Umur      :", data["Umur"])
        print("| No HP     :", data["NoHP"])
        print("| Alamat    :", data["Alamat"])
        print("| Vaksinasi :", data["Vaksinasi"])
        print("| Created   :", data["Created"])
        print("========================================================================")
    username = input("Masukkan Username : ")
    if username == session_account["Username"]:
        print("========================================================================")
        print("| Error: Anda tidak dapat mengedit akun anda sendiri!                  |")
        print("========================================================================")
    else:
        if data["Username"] != username:
            print("========================================================================")
            print("| Error: Username tidak ditemukan!                                     |")
            print("========================================================================")
        else:
            indeks = 0
            for data in akun:
                if data["Username"] == username:
                    print("========================================================================")
                    print("| Sukses: Data Akun ditemukan!                                         |")
                    print("========================================================================")
                    try:
                        new_username = input("Username Baru : ")
                        if len(new_username) < 4:
                            print("========================================================================")
                            print("| Error: Username minimal 4 karakter!                                  |")
                            print("========================================================================")
                            back_to_show_menu()
                        new_password = input("Password Baru : ")
                        if len(new_password) < 8:
                            print("========================================================================")
                            print("| Error: Password minimal 8 karakter!                                  |")
                            print("========================================================================")
                            back_to_show_menu()
                        new_level = input("Level Baru    : ")
                        if new_level != "admin" or new_level != "dinkes" or new_level != "pasien":
                            print("========================================================================")
                            print("| Error: Level tidak tersedia!                                         |")
                            print("========================================================================")
                            back_to_show_menu()
                        new_nik = int(input("NIK Baru      : "))
                        new_nama = input("Nama Baru     : ")
                        if len(new_nama) < 1:
                            print("========================================================================")
                            print("| Error: Anda tidak dapat mengosongkan Nama                            |")
                            print("========================================================================")
                            back_to_show_menu()
                        new_umur = int(input("Umur Baru     : "))
                        new_nohp = int(input("No HP Baru    : "))
                        new_alamat = input("Alamat Baru   : ")
                        if len(new_alamat) < 1:
                            print("========================================================================")
                            print("| Error: Anda tidak dapat mengosongkan Alamat                          |")
                            print("========================================================================")
                            back_to_show_menu()
                        new_vaksinasi = input("Vaksinasi Baru    : ")
                        if new_vaksinasi != "True" or new_vaksinasi != "False":
                            print("========================================================================")
                            print("| Error: Vaksinasi salah!                                              |")
                            print("========================================================================")
                            back_to_show_menu()
                    except ValueError:
                        print("========================================================================")
                        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                        print("========================================================================")
                        back_to_show_menu()
                    akun[indeks]["Username"] = new_username
                    akun[indeks]["Password"] = new_password
                    akun[indeks]["Level"] = new_level
                    akun[indeks]["NIK"] = new_nik
                    akun[indeks]["Nama"] = new_nama
                    akun[indeks]["Umur"] = new_umur
                    akun[indeks]["NoHP"] = new_nohp
                    akun[indeks]["Alamat"] = new_alamat
                    akun[indeks]["Vaksinasi"] = new_vaksinasi
                    print("========================================================================")
                    print("| Sukses: Akun berhasil di update!                                     |")
                    print("========================================================================")
                    break
                indeks += 1
            data_found = False
            for data in akun:
                if data["NIK"] == new_nik or data["Username"] == new_username:
                    data_found = True
                    break
            if data_found == True:
                print("========================================================================")
                print("| Error: Username atau NIK tersebut telah didaftarkan!                 |")
                print("========================================================================")
                back_to_show_menu()
            with open(csv_filename_accounts, mode="w") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in akun:
                    csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
    back_to_show_menu()

def delete_account():
    clear_screen()
    print("========================================================================")
    print("|                          HAPUS AKUN PENGGUNA                         |")
    print("========================================================================")
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    for data in akun:
        print("| Username  :", data["Username"])
        print("| Password  :", data["Password"])
        print("| Level     :", data["Level"])
        print("| NIK       :", data["NIK"])
        print("| Nama      :", data["Nama"])
        print("| Umur      :", data["Umur"])
        print("| No HP     :", data["NoHP"])
        print("| Alamat    :", data["Alamat"])
        print("| Vaksinasi :", data["Vaksinasi"])
        print("| Created   :", data["Created"])
        print("========================================================================")
    username = input("Masukkan Username : ")
    if username == session_account["Username"]:
        print("========================================================================")
        print("| Error: Anda tidak dapat menghapus akun anda sendiri!                 |")
        print("========================================================================")
    else:
        if data["Username"] != username:
            print("========================================================================")
            print("| Error: Username tidak ditemukan!                                     |")
            print("========================================================================")
        else:
            indeks = 0
            for data in akun:
                if data["Username"] == username:
                    akun.remove(akun[indeks])
                    print("========================================================================")
                    print("| Sukses: Akun berhasil di hapus!                                      |")
                    print("========================================================================")
                    break
                indeks += 1
            with open(csv_filename_accounts, mode="w") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in akun:
                    csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
    back_to_show_menu()

def sort_account():
    clear_screen()
    print("========================================================================")
    print("|                          URUT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Username                                                         |")
    print("| [2] Level                                                            |")
    print("| [3] NIK                                                              |")
    print("| [4] Nama                                                             |")
    print("| [5] Umur                                                             |")
    print("| [6] No. HP                                                           |")
    print("| [7] Alamat                                                           |")
    print("| [8] Vaksinasi                                                        |")
    print("| [9] Created                                                          |")
    print("| [10] Kembali                                                         |")
    print("========================================================================")
    sorting = ""
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        sorting = "Username"
    elif selected_menu == "2":
        sorting = "Level"
    elif selected_menu == "3":
        sorting = "NIK"
    elif selected_menu == "4":
        sorting = "Nama"
    elif selected_menu == "5":
        sorting = "Umur"
    elif selected_menu == "6":
        sorting = "NoHP"
    elif selected_menu == "7":
        sorting = "Alamat"
    elif selected_menu == "8":
        sorting = "Vaksinasi"
    elif selected_menu == "9":
        sorting = "Created"
    elif selected_menu == "10":
        show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_sort_account()
    clear_screen()
    print("========================================================================")
    print("|                          URUT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Metode Bubble Sort                                               |")
    print("| [2] Metode Selection Sort                                            |")
    print("| [3] Metode Insertion Sort                                            |")
    print("| [4] Metode Quick Sort                                                |")
    print("| [5] Metode Merge Sort                                                |")
    print("| [6] Metode Shell Sort                                                |")
    print("| [7] Kembali                                                          |")
    print("========================================================================")
    metode = ""
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        metode = "Bubble"
    elif selected_menu == "2":
        metode = "Selection"
    elif selected_menu == "3":
        metode = "Insertion"
    elif selected_menu == "4":
        metode = "Quick"
    elif selected_menu == "5":
        metode = "Merge"
    elif selected_menu == "6":
        metode = "Shell"
    elif selected_menu == "7":
        show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_sort_account()
    clear_screen()
    print("========================================================================")
    print("|                          URUT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Secara Ascending                                                 |")
    print("| [2] Secara Descending                                                |")
    print("| [3] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Pilih Menu> ")
    order = ""
    if selected_menu == "1":
        order = "Ascending"
    elif selected_menu == "2":
        order = "Descending"
    elif selected_menu == "3":
        sort_account()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_sort_account()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    if len(akun) < 1:
        print("========================================================================")
        print("| Error: Tidak ada data pengguna ditemukan!                            |")
        print("========================================================================")
    else:
        datasort = []
        indeks = 0
        for data in akun:
            if sorting == "Username":
                datasort.append([data["Username"], indeks])
            elif sorting == "Level":
                datasort.append([data["Level"], indeks])
            elif sorting == "NIK":
                datasort.append([data["NIK"], indeks])
            elif sorting == "Nama":
                datasort.append([data["Nama"], indeks])
            elif sorting == "Umur":
                datasort.append([data["Umur"], indeks])
            elif sorting == "NoHP":
                datasort.append([data["NoHP"], indeks])
            elif sorting == "Alamat":
                datasort.append([data["Alamat"], indeks])
            elif sorting == "Vaksinasi":
                datasort.append([data["Vaksinasi"], indeks])
            elif sorting == "Created":
                datasort.append([data["Created"], indeks])
            indeks += 1
        if metode == "Bubble":
            bubbleSort(datasort, order)
        elif metode == "Selection":
            selectionSort(datasort, len(datasort), order)
        elif metode == "Insertion":
            insertionSort(datasort, order)
        elif metode == "Quick":
            quickSort(datasort, 0, len(datasort)-1, order)
        elif metode == "Merge":
            mergeSort(datasort, 0, len(datasort)-1, order)
        elif metode == "Shell":
            shellSort(datasort, len(datasort), order)
        old_akun = akun.copy()
        akun.clear()
        for i in range(len(datasort)):
            akun.append({"Username": old_akun[datasort[i][1]]["Username"], "Password": old_akun[datasort[i][1]]["Password"], "Level": old_akun[datasort[i][1]]["Level"], "NIK": old_akun[datasort[i][1]]["NIK"], "Nama": old_akun[datasort[i][1]]["Nama"], "Umur": old_akun[datasort[i][1]]["Umur"], "NoHP": old_akun[datasort[i][1]]["NoHP"], "Alamat": old_akun[datasort[i][1]]["Alamat"], "Vaksinasi": old_akun[datasort[i][1]]["Vaksinasi"], "Created": old_akun[datasort[i][1]]["Created"]})
        with open(csv_filename_accounts, mode="w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for new_data in akun:
                csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"]})
        print("========================================================================")
        print("| Sukses: Data Pengguna berhasil diurutkan                             |")
        print("========================================================================")
    back_to_show_menu()

def back_to_sort_account():
    input("\nTekan 'Enter' untuk kembali...")
    sort_account()

def search_account():
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Username                                                         |")
    print("| [2] Level                                                            |")
    print("| [3] NIK                                                              |")
    print("| [4] Nama                                                             |")
    print("| [5] Umur                                                             |")
    print("| [6] No. HP                                                           |")
    print("| [7] Alamat                                                           |")
    print("| [8] Vaksinasi                                                        |")
    print("| [9] Created                                                          |")
    print("| [10] Kembali                                                         |")
    print("========================================================================")
    searching = ""
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        searching = "Username"
    elif selected_menu == "2":
        searching = "Level"
    elif selected_menu == "3":
        searching = "NIK"
    elif selected_menu == "4":
        searching = "Nama"
    elif selected_menu == "5":
        searching = "Umur"
    elif selected_menu == "6":
        searching = "NoHP"
    elif selected_menu == "7":
        searching = "Alamat"
    elif selected_menu == "8":
        searching = "Vaksinasi"
    elif selected_menu == "9":
        searching = "Created"
    elif selected_menu == "10":
        show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_search_account()
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Metode Linear Search                                             |")
    print("| [2] Metode Binary Search                                             |")
    if searching == "NIK" or searching == "Umur" or searching == "NoHP":
        print("| [3] Metode Interpolation Search                                      |")
        print("| [4] Kembali                                                          |")
    else:
        print("| [3] Kembali                                                          |")
    print("========================================================================")
    metode_searching = ""
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        metode_searching = "Linear"
    elif selected_menu == "2":
        metode_searching = "Binary"
    if searching == "NIK" or searching == "Umur" or searching == "NoHP":
        if selected_menu == "3":
            metode_searching = "Interpolation"
        elif selected_menu == "4":
            search_account()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_search_account()
    else:
        if selected_menu == "3":
            search_account()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            back_to_search_account()
    print("========================================================================")
    print("|                          URUT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Metode Bubble Sort                                               |")
    print("| [2] Metode Selection Sort                                            |")
    print("| [3] Metode Insertion Sort                                            |")
    print("| [4] Metode Quick Sort                                                |")
    print("| [5] Metode Merge Sort                                                |")
    print("| [6] Metode Shell Sort                                                |")
    print("| [7] Kembali                                                          |")
    print("========================================================================")
    metode_sorting = ""
    selected_menu = input("Pilih Menu> ")
    if selected_menu == "1":
        metode_sorting = "Bubble"
    elif selected_menu == "2":
        metode_sorting = "Selection"
    elif selected_menu == "3":
        metode_sorting = "Insertion"
    elif selected_menu == "4":
        metode_sorting = "Quick"
    elif selected_menu == "5":
        metode_sorting = "Merge"
    elif selected_menu == "6":
        metode_sorting = "Shell"
    elif selected_menu == "7":
        show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        back_to_search_account()
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    if searching == "NIK" or searching == "Umur" or searching == "NoHP":
        try:
            search = int(input("Data yang ingin dicari> "))
            if search < 1:
                print("========================================================================")
                print("| Gagal: Tidak dapat mencari data kurang dari 1!                       |")
                print("========================================================================")
                back_to_search_account()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            back_to_search_account()
    else:
        search = input("Data yang ingin dicari> ")
    datasort = []
    datasearch = []
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    indeks = 0
    for data in akun:
        if searching == "Username":
            datasort.append([data["Username"], indeks])
        elif searching == "Level":
            datasort.append([data["Level"], indeks])
        elif searching == "NIK":
            datasort.append([int(data["NIK"]), indeks])
        elif searching == "Nama":
            datasort.append([data["Nama"], indeks])
        elif searching == "Umur":
            datasort.append([int(data["Umur"]), indeks])
        elif searching == "NoHP":
            datasort.append([int(data["NoHP"]), indeks])
        elif searching == "Alamat":
            datasort.append([data["Alamat"], indeks])
        elif searching == "Vaksinasi":
            datasort.append([int(data["Vaksinasi"]), indeks])
        elif searching == "Created":
            datasort.append([data["Created"], indeks])
        indeks += 1
    if metode_sorting == "Bubble":
        bubbleSort(datasort, "Ascending")
    if metode_sorting == "Selection":
        selectionSort(datasort, len(datasort), "Ascending")
    if metode_sorting == "Insertion":
        insertionSort(datasort, "Ascending")
    if metode_sorting == "Quick":
        quickSort(datasort, 0, len(datasort)-1, "Ascending")
    if metode_sorting == "Merge":
        mergeSort(datasort, 0, len(datasort)-1, "Ascending")
    if metode_sorting == "Shell":
        shellSort(datasort, len(datasort), "Ascending")
    for i in range(len(datasort)):
        datasearch.append(datasort[i][0])
    if metode_searching == "Linear":
        result = linearSearch(datasearch, len(datasearch), search.lower())
    elif metode_searching == "Binary":
        result = binarySearch(datasearch, search.lower(), 0, len(datasearch) - 1)
    elif metode_searching == "Interpolation":
        result = interpolationSearch(datasearch, 0, len(datasearch) - 1, search)
    if result != -1:
        print("========================================================================")
        print("| Sukses: Data Pengguna ditemukan!                                     |")
        print("========================================================================")
        print("| Username  :", data[datasort[result][1]]["Username"])
        print("| Password  :", data[datasort[result][1]]["Password"])
        print("| Level     :", data[datasort[result][1]]["Level"])
        print("| NIK       :", data[datasort[result][1]]["NIK"])
        print("| Nama      :", data[datasort[result][1]]["Nama"])
        print("| Umur      :", data[datasort[result][1]]["Umur"])
        print("| No HP     :", data[datasort[result][1]]["NoHP"])
        print("| Alamat    :", data[datasort[result][1]]["Alamat"])
        print("| Vaksinasi :", data[datasort[result][1]]["Vaksinasi"])
        print("| Created   :", data[datasort[result][1]]["Created"])
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Gagal: Data Pengguna tidak ditemukan!                                |")
        print("========================================================================")
    back_to_show_menu()

def back_to_search_account():
    input("\nTekan 'Enter' untuk kembali...")
    search_account()

def bubbleSort(array, order):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if order == "Ascending":
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            elif order == "Descending":
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

def selectionSort(array, size, order):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if order == "Ascending":
                if array[i] < array[min_idx]:
                    min_idx = i
            elif order == "Descending":
                if array[i] > array[min_idx]:
                    min_idx = i
        array[step], array[min_idx] = array[min_idx],array[step]

def insertionSort(array, order):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        if order == "Ascending":
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        elif order == "Descending":
            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key

def partition(array, low, high, order):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if order == "Ascending":
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        elif order == "Descending":
            if array[j] >= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high, order):
    if low < high:
        pi = partition(array, low, high, order)
        quickSort(array, low, pi - 1, order)
        quickSort(array, pi + 1, high, order)

def merge(arr, l, m, r, order):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 :
        if order == "Ascending":
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        elif order == "Descending":
            if L[i] >= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r, order):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m, order)
        mergeSort(arr, m + 1, r, order)
        merge(arr, l, m, r, order)

def shellSort(array, n, order):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            if order == "Ascending":
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
            elif order == "Descending":
                while j >= interval and array[j - interval] < temp:
                    array[j] = array[j - interval]
                    j -= interval
            array[j] = temp
        interval //= 2

def linearSearch(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def interpolationSearch(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,hi, x)
        if arr[pos] > x:
            return interpolationSearch(arr, lo,pos - 1, x)
    return -1

if __name__ == "__main__":
    check_file()
    while True:
        try:
            show_auth()
        except KeyboardInterrupt:
            close_app()
