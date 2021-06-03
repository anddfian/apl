import os
from time import sleep
from datetime import datetime
import csv

session_account = {}
session_vaksinasi = {}

csv_filename_accounts = "accounts.csv"
csv_filename_vaksin = "vaksin.csv"
csv_filename_vaksinasi = "vaksinasi.csv"
csv_filename_feedback = "feedback.csv"

def check_file():
    if not os.path.exists(csv_filename_accounts):
        with open(csv_filename_accounts, "w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_vaksin):
        with open(csv_filename_vaksin, "w") as csv_file:
            fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_vaksinasi):
        with open(csv_filename_vaksinasi, "w") as csv_file:
            fieldnames = ["Timestamp", "NIK", "Nama", "Suhu", "Tekanan", "Vaksin", "Nomor", "KIPI", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
    if not os.path.exists(csv_filename_feedback):
        with open(csv_filename_feedback, "w") as csv_file:
            fieldnames = ["Timestamp", "Jenis", "Nama", "Kritik", "Saran"]
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
        return auth_register()
    elif selected_menu == "2":
        return show_login()
    elif selected_menu == "0":
        return close_app()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_show_auth()

def back_to_show_auth():
    input("\nTekan 'Enter' untuk kembali...")
    return show_auth()

def timestamp_now():
    now = datetime.now()
    return "%d/%d/%d %d:%d:%d" % (now.day,now.month,now.year,now.hour,now.minute,now.second)

def auth_register():
    clear_screen()
    print("========================================================================")
    print("|                              DAFTAR AKUN                             |")
    print("========================================================================")
    print("| [1] Pasien                                                           |")
    print("| [2] Dinkes                                                           |")
    print("| [3] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Masukkan Pilihan> ")
    if selected_menu == "1":
        clear_screen()
        print("========================================================================")
        print("|                              DAFTAR AKUN                             |")
        print("========================================================================")
        print("| Info: Silakan isi Username, Password, NIK, Nama, Umur, No. HP, dan   |")
        print("|       Alamat akun anda                                               |")
        print("========================================================================")
        try:
            username = input("Username : ")
            if len(username) < 4:
                print("========================================================================")
                print("| Error: Username minimal 4 karakter!                                  |")
                print("========================================================================")
                return back_to_auth_register()
            password = input("Password : ")
            if len(password) < 8:
                print("========================================================================")
                print("| Error: Password minimal 8 karakter!                                  |")
                print("========================================================================")
                return back_to_auth_register()
            nik = int(input("NIK      : "))
            nama = input("Nama     : ")
            if len(nama) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan nama!                           |")
                print("========================================================================")
                return back_to_auth_register()
            umur = int(input("Umur     : "))
            nohp = int(input("No. HP   : "))
            alamat = input("Alamat   : ")
            if len(alamat) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan alamat!                         |")
                print("========================================================================")
                return back_to_auth_register()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_auth_register()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
        if data_found == True:
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            return back_to_auth_register()
        else:
            with open(csv_filename_accounts, mode="a") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Username": username, "Password": password, "Level": "pasien", "NIK": nik, "NIP": "", "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp_now(), "Updated": timestamp_now(), "Log": username})
            print("========================================================================")
            print("| Sukses: Akun berhasil dibuat dan disimpan!                           |")
            print("========================================================================")
            return back_to_show_login()
    elif selected_menu == "2":
        clear_screen()
        print("========================================================================")
        print("|                              DAFTAR AKUN                             |")
        print("========================================================================")
        print("| Info: Silakan isi Username, Password, NIK, NIP, Nama akun anda       |")
        print("========================================================================")
        try:
            username = input("Username : ")
            if len(username) < 4:
                print("========================================================================")
                print("| Error: Username minimal 4 karakter!                                  |")
                print("========================================================================")
                return back_to_auth_register()
            password = input("Password : ")
            if len(password) < 8:
                print("========================================================================")
                print("| Error: Password minimal 8 karakter!                                  |")
                print("========================================================================")
                return back_to_auth_register()
            nik = int(input("NIK      : "))
            nip = int(input("NIP      : "))
            nama = input("Nama     : ")
            if len(nama) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan nama                           |")
                print("========================================================================")
                return back_to_auth_register()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_auth_register()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
        if data_found == True:
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            return back_to_auth_register()
        else:
            with open(csv_filename_accounts, mode="a") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Username": username, "Password": password, "Level": "dinkes", "NIK": nik, "NIP": nip, "Nama": nama, "Umur": "", "NoHP": "", "Alamat": "", "Vaksinasi": "", "Created": timestamp_now(), "Updated": timestamp_now(), "Log": username})
            print("========================================================================")
            print("| Sukses: Akun berhasil dibuat dan disimpan!                           |")
            print("========================================================================")
            return back_to_show_login()
    elif selected_menu == "3":
        return show_auth()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_auth_register()

def back_to_auth_register():
    input("\nTekan 'Enter' untuk kembali...")
    return auth_register()

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
        return auth_login("pasien")
    elif selected_menu == "2":
        return auth_login("dinkes")
    elif selected_menu == "3":
        return auth_login("admin")
    elif selected_menu == "4":
        return forgot_password()
    elif selected_menu == "5":
        return show_auth()
    elif selected_menu == "0":
        return close_app()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_show_login()

def back_to_show_login():
    input("\nTekan 'Enter' untuk kembali...")
    return show_login()

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
                session_account["Updated"] = data_found["Updated"]
                session_account["Log"] = data_found["Log"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Pasien                           |")
                print("========================================================================")
                sleep(1.5)
                return show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                return back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            return back_to_show_login()
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
                session_account["NIP"] = data_found["NIP"]
                session_account["Nama"] = data_found["Nama"]
                session_account["Updated"] = data_found["Updated"]
                session_account["Log"] = data_found["Log"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Dinkes                           |")
                print("========================================================================")
                sleep(1.5)
                return show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                return back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            return back_to_show_login()
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
                session_account["Nama"] = data_found["Nama"]
                session_account["Updated"] = data_found["Updated"]
                session_account["Log"] = data_found["Log"]
                print("========================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Admin                            |")
                print("========================================================================")
                sleep(1.5)
                return show_menu()
            else:
                print("========================================================================")
                print("| Error: Username dan Password salah!                                  |")
                print("========================================================================")
                return back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            return back_to_show_login()

def forgot_password():
    clear_screen()
    print("========================================================================")
    print("|                             LUPA PASSWORD                            |")
    print("========================================================================")
    print("| [1] Pasien                                                           |")
    print("| [2] Dinkes                                                           |")
    print("| [3] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Masukkan Pilihan> ")
    if selected_menu == "1":
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
            return back_to_forgot_password()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        indeks = 0
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
            indeks += 1
        if data_found == True:
            data_match = False
            for data in akun:
                if data["Username"] == username and int(data["NIK"]) == nik:
                    akun[indeks]["Password"] = "vaksinasi"
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = akun[indeks]["Username"]
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
                return back_to_forgot_password()
            else:
                with open(csv_filename_accounts, mode="w") as csv_file:
                    fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for new_data in akun:
                        csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
                return back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            return back_to_forgot_password()
    elif selected_menu == "2":
        clear_screen()
        print("========================================================================")
        print("|                             LUPA PASSWORD                            |")
        print("========================================================================")
        print("| Info: Masukkan Username, NIK, dan NIP Anda                           |")
        print("========================================================================")
        try:
            username = input("Username : ")
            nik = int(input("NIK      : "))
            nip = int(input("NIP      : "))
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_forgot_password()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        indeks = 0
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
            indeks += 1
        if data_found == True:
            data_match = False
            for data in akun:
                if data["Username"] == username and int(data["NIK"]) == nik and int(data["NIP"]) == nip:
                    akun[indeks]["Password"] = "vaksinasi"
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = akun[indeks]["Username"]
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
                return back_to_forgot_password()
            else:
                with open(csv_filename_accounts, mode="w") as csv_file:
                    fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for new_data in akun:
                        csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
                return back_to_show_login()
        else:
            print("========================================================================")
            print("| Error: Data akun tidak ditemukan!                                    |")
            print("========================================================================")
            return back_to_forgot_password()

def back_to_forgot_password():
    input("\nTekan 'Enter' untuk kembali...")
    return forgot_password()

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
            return data_vaksin()
        elif selected_menu == "2":
            return data_vaksinasi()
        elif selected_menu == "3":
            return daftar_vaksinasi()
        elif selected_menu == "4":
            return riwayat_vaksinasi()
        elif selected_menu == "5":
            return tentang_aplikasi()
        elif selected_menu == "6":
            return feedback()
        elif selected_menu == "7":
            return pengaturan_akun()
        elif selected_menu == "8":
            session_account.clear()
            return show_login()
        elif selected_menu == "0":
            return close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_show_menu()
    elif session_account["Level"] == "dinkes":
        if selected_menu == "1":
            return data_vaksin()
        elif selected_menu == "2":
            return data_vaksinasi()
        elif selected_menu == "3":
            return meja_pertama()
        elif selected_menu == "4":
            return tentang_aplikasi()
        elif selected_menu == "5":
            return show_feedback()
        elif selected_menu == "6":
            return feedback()
        elif selected_menu == "7":
            return pengaturan_akun()
        elif selected_menu == "8":
            return show_login()
        elif selected_menu == "0":
            return close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_show_menu()
    elif session_account["Level"] == "admin":
        if selected_menu == "1":
            return show_account()
        elif selected_menu == "2":
            return create_account()
        elif selected_menu == "3":
            return edit_account()
        elif selected_menu == "4":
            return delete_account()
        elif selected_menu == "5":
            return sort_account()
        elif selected_menu == "6":
            return search_account()
        elif selected_menu == "7":
            return data_vaksin()
        elif selected_menu == "8":
            return data_vaksinasi()
        elif selected_menu == "9":
            return tentang_aplikasi()
        elif selected_menu == "10":
            return show_feedback()
        elif selected_menu == "11":
            return pengaturan_akun()
        elif selected_menu == "12":
            return show_login()
        elif selected_menu == "0":
            return close_app()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_show_menu()

def back_to_show_menu():
    input("\nTekan 'Enter' untuk kembali...")
    return show_menu()

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
        return back_to_show_menu()
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
                    print("| Created     :", data["Created"])
                    print("| Updated     :", data["Updated"])
                    print("| Log         :", data["Log"])
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
                fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow({"Nama": nama, "Produksi": produksi, "Penggunaan": 0, "Created": timestamp_now(), "Updated": timestamp_now(), "Log": session_account["Nama"]})
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
                print("| Created     :", data["Created"])
                print("| Updated     :", data["Updated"])
                print("| Log         :", data["Log"])
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
                    vaksin[nomor-1]["Updated"] = timestamp_now()
                    vaksin[nomor-1]["Log"] = session_account["Nama"]
                    with open(csv_filename_vaksin, mode="w") as csv_file:
                        fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for new_data in vaksin:
                            csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
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
                print("| Created     :", data["Created"])
                print("| Updated     :", data["Updated"])
                print("| Log         :", data["Log"])
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
                        fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for new_data in vaksin:
                            csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
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
            print("| [4] Created Vaksin                                                   |")
            print("| [5] Updated Vaksin                                                   |")
            print("| [6] Log Vaksin                                                       |")
            print("| [7] Kembali                                                          |")
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
                sorting = "Created"
            elif selected_menu == "5":
                sorting = "Updated"
            elif selected_menu == "6":
                sorting = "Log"
            elif selected_menu == "7":
                return data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                return back_to_data_vaksin()
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
                return data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                return back_to_data_vaksin()
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
                return data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                return back_to_data_vaksin()
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
                    elif sorting == "Created":
                        datasort.append([data["Created"], indeks])
                    elif sorting == "Updated":
                        datasort.append([data["Updated"], indeks])
                    elif sorting == "Log":
                        datasort.append([data["Log"], indeks])
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
                    vaksin.append({"Nama": old_vaksin[datasort[i][1]]["Nama"], "Produksi": old_vaksin[datasort[i][1]]["Produksi"], "Penggunaan": old_vaksin[datasort[i][1]]["Penggunaan"], "Created": old_vaksin[datasort[i][1]]["Created"], "Updated": old_vaksin[datasort[i][1]]["Updated"], "Log": old_vaksin[datasort[i][1]]["Log"]})
                with open(csv_filename_vaksin, mode="w") as csv_file:
                    fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for new_data in vaksin:
                        csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
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
            print("| [4] Created Vaksin                                                   |")
            print("| [5] Updated Vaksin                                                   |")
            print("| [6] Log Vaksin                                                       |")
            print("| [7] Kembali                                                          |")
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
                searching = "Created"
            elif selected_menu == "5":
                searching = "Updated"
            elif selected_menu == "6":
                searching = "Log"
            elif selected_menu == "7":
                return data_vaksin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                return back_to_data_vaksin()
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
                if selected_menu == "1" or selected_menu == "2" or selected_menu == "4" or selected_menu == "5" or selected_menu == "6":
                    pass
                elif selected_menu == "3":
                    metode = "Interpolation"
                elif selected_menu == "4":
                    return data_vaksin()
                else:
                    print("========================================================================")
                    print("| Error: Anda memilih menu yang salah!                                 |")
                    print("========================================================================")
                    return back_to_data_vaksin()
            else:
                if selected_menu == "1" or selected_menu == "2" or selected_menu == "4" or selected_menu == "5" or selected_menu == "6":
                    pass
                elif selected_menu == "3":
                    return data_vaksin()
                else:
                    print("========================================================================")
                    print("| Error: Anda memilih menu yang salah!                                 |")
                    print("========================================================================")
                    return back_to_data_vaksin()
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
                        return back_to_data_vaksin()
                except ValueError:
                    print("========================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                    print("========================================================================")
                    return back_to_data_vaksin()
            else:
                search = input("Data yang ingin dicari> ")
            datasort = []
            datasearch = []
            indeks = 0
            for data in vaksin:
                if searching == "Nama":
                    datasort.append([data["Nama"], indeks])
                elif searching == "Produksi":
                    datasort.append([data["Produksi"], indeks])
                elif searching == "Penggunaan":
                    datasort.append([data["Penggunaan"], indeks])
                elif searching == "Created":
                    datasort.append([data["Created"], indeks])
                elif searching == "Updated":
                    datasort.append([data["Updated"], indeks])
                elif searching == "Log":
                    datasort.append([data["Log"], indeks])
                indeks += 1
            quickSort(datasort, 0, len(datasort)-1, "Ascending")
            for i in range(len(datasort)):
                datasearch.append(datasort[i][0])
            if metode == "Linear":
                result = linearSearch(datasearch, len(datasearch), search)
            elif metode == "Binary":
                result = binarySearch(datasearch, search, 0, len(datasearch) - 1)
            elif metode == "Interpolation":
                result = interpolationSearch(datasearch, 0, len(datasearch) - 1, search)
            if result != -1:
                print("========================================================================")
                print("| Sukses: Data Vaksin ditemukan!                                       |")
                print("========================================================================")
                print("| Vaksin ke-%d" % datasort[result][1])
                print("| Nama Vaksin :", vaksin[datasort[result][1]]["Nama"])
                print("| Produksi    :", vaksin[datasort[result][1]]["Produksi"])
                print("| Penggunaan  :", vaksin[datasort[result][1]]["Penggunaan"])
                print("========================================================================")
            else:
                print("========================================================================")
                print("| Gagal: Data Vaksin tidak ditemukan!                                  |")
                print("========================================================================")
        elif selected_menu == "7":
            return show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
        return back_to_data_vaksin()

def back_to_data_vaksin():
    input("\nTekan 'Enter' untuk kembali...")
    return data_vaksin()

def data_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                        DATA VAKSINASI COVID-19                       |")
    print("========================================================================")
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    count_daftar = 0
    for data in akun:
        if data["Vaksinasi"] == "True":
            count_daftar += 1
    vaksinasi = []
    with open(csv_filename_vaksinasi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksinasi.append(row)
    print("Tangal Waktu     :", timestamp_now())
    print("Jumlah Pendaftar :", count_daftar)
    print("Jumlah Vaksinasi :", len(vaksinasi))
    print("========================================================================")
    return back_to_show_menu()

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
                akun[indeks]["Updated"] = timestamp_now()
                akun[indeks]["Log"] = session_account["Nama"]
                session_account["Vaksinasi"] = "True"
                session_account["Updated"] = timestamp_now()
                session_account["Log"] = session_account["Nama"]
                print("========================================================================")
                print("| Sukses: Data anda berhasil di daftar                                 |")
                print("========================================================================")
                break
            indeks += 1
        with open(csv_filename_accounts, mode="w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for new_data in akun:
                csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
    else:
        print("========================================================================")
        print("| Error: Data anda telah terdaftar!                                    |")
        print("========================================================================")
    return back_to_show_menu()

def meja_pertama():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                             MEJA PERTAMA                             |")
    print("========================================================================")
    try:
        nik = int(input("Masukkan NIK  : "))
        nama = input("Masukkan Nama : ")
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        input("\nTekan 'Enter' untuk melanjutkan...")
        return meja_pertama()
    akun = []
    with open(csv_filename_accounts, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = False
    for data in akun:
        if data["Level"] == "pasien":
            if int(data["NIK"]) == nik and data["Nama"] == nama and data["Vaksinasi"] == "True":
                session_vaksinasi["Nama"] = data["Nama"]
                data_found = True
                break
    vaksinasi = []
    with open(csv_filename_vaksinasi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            vaksinasi.append(row)
    count_vaksinasi = 0
    for data in vaksinasi:
        if int(data["NIK"]) == nik and data["Nama"] == nama:
            count_vaksinasi += 1
    if data_found == True:
        if count_vaksinasi == 2:
            print("========================================================================")
            print("| Error: Pasien telah di vaksin sebanyak 2x                            |")
            print("========================================================================")
        else:
            print("========================================================================")
            session_vaksinasi["Vaksinasi"] = count_vaksinasi
            session_vaksinasi["NIK"] = nik
            input("\nTekan 'Enter' untuk melanjutkan...")
            return meja_kedua()
    else:
        print("========================================================================")
        print("| Error: Data anda tidak terdaftar!                                    |")
        print("========================================================================")
    return back_to_show_menu()

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
        return meja_ketiga()
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        input("\nTekan 'Enter' untuk melanjutkan...")
        return meja_kedua()        

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
        return back_to_show_menu()
    else:
        try:
            nomor_vaksin = int(input("Pilih Vaksin yang ingin digunakan : "))
            nomor_batch_vaksin = int(input("Masukkan Nomor Batch Vaksin       : "))
            print("========================================================================")
            session_vaksinasi["Vaksin"] = vaksin[nomor_vaksin-1]["Nama"]
            session_vaksinasi["Nomor"] = nomor_batch_vaksin
            penggunaan = int(vaksin[nomor_vaksin-1]["Penggunaan"]) + 1
            vaksin[nomor_vaksin-1]["Penggunaan"] = penggunaan
            vaksin[nomor_vaksin-1]["Updated"] = timestamp_now()
            vaksin[nomor_vaksin-1]["Log"] = session_account["Nama"]
            with open(csv_filename_vaksin, mode="w") as csv_file:
                fieldnames = ["Nama", "Produksi", "Penggunaan", "Created", "Updated", "Log"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in vaksin:
                    csv_writer.writerow({"Nama": new_data["Nama"], "Produksi": new_data["Produksi"], "Penggunaan": new_data["Penggunaan"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
            input("\nTekan 'Enter' untuk melanjutkan...")
            return meja_keempat()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            input("\nTekan 'Enter' untuk melanjutkan...")
            return meja_ketiga()        

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
    return final_vaksinasi()

def final_vaksinasi():
    clear_screen()
    print("========================================================================")
    print("|                      APLIKASI VAKSINASI COVID-19                     |")
    print("========================================================================")
    print("|                            DATA VAKSINASI                            |")
    print("========================================================================")
    print("Timestamp          :", timestamp_now())
    print("NIK                :", session_vaksinasi["NIK"])
    print("Nama               :", session_vaksinasi["Nama"])
    print("Vaksinasi Ke       :", session_vaksinasi["Vaksinasi"] + 1)
    print("Suhu Tubuh         :", session_vaksinasi["Suhu"])
    print("Tekanan Darah      :", session_vaksinasi["Tekanan"])
    print("Nama Vaksin        :", session_vaksinasi["Vaksin"])
    print("Nomor Batch Vaksin :", session_vaksinasi["Nomor"])
    print("KIPI               :", session_vaksinasi["KIPI"])
    print("Log                :", session_account["Nama"])
    print("========================================================================")
    with open(csv_filename_vaksinasi, mode="a") as csv_file:
        fieldnames = ["Timestamp", "NIK", "Nama", "Suhu", "Tekanan", "Vaksin", "Nomor", "KIPI", "Log"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writerow({"Timestamp": timestamp_now(), "NIK": session_vaksinasi["NIK"], "Nama": session_vaksinasi["Nama"], "Suhu": session_vaksinasi["Suhu"], "Tekanan": session_vaksinasi["Tekanan"], "Vaksin": session_vaksinasi["Vaksin"], "Nomor": session_vaksinasi["Nomor"], "KIPI": session_vaksinasi["KIPI"], "Log": session_account["Nama"]})
    session_vaksinasi.clear()
    return back_to_show_menu()

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
                if data["NIK"] == session_account["NIK"] and data["Nama"] == session_account["Nama"]:
                    print("Vaksinasi Ke-%d" % indeks)
                    print("Timestamp          :", data["Timestamp"])
                    print("Suhu Tubuh         :", data["Suhu"])
                    print("Tekanan Darah      :", data["Tekanan"])
                    print("Nama Vaksin        :", data["Vaksin"])
                    print("Nomor Batch Vaksin :", data["Nomor"])
                    print("KIPI               :", data["KIPI"])
                    print("Log                :", data["Log"])
                print("========================================================================")
                indeks += 1
    else:
        print("========================================================================")
        print("| Error: Anda belum daftar vaksinasi!                                  |")
        print("========================================================================")
    return back_to_show_menu()

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
    return back_to_show_menu()

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
                return back_to_pengaturan_akun()
            konfirmasi_password_baru = input("Konfirmasi Password Baru : ")
            if len(konfirmasi_password_baru) < 8:
                print("========================================================================")
                print("| Error: Password Baru minimal 8 karakter!                             |")
                print("========================================================================")
                return back_to_pengaturan_akun()
            if password_baru == password_lama or konfirmasi_password_baru == password_lama:
                print("========================================================================")
                print("| Error: Password Baru tidak boleh sama dengan Password Lama           |")
                print("========================================================================")
                return back_to_pengaturan_akun()
            elif password_baru == konfirmasi_password_baru:
                indeks = 0
                for data in akun:
                    if data["Username"] == session_account["Username"]:
                        akun[indeks]["Password"] = password_baru
                        akun[indeks]["Updated"] = timestamp_now()
                        akun[indeks]["Log"] = session_account["Username"]
                        session_account["Password"] = password_baru
                        session_account["Updated"] = timestamp_now()
                        session_account["Log"] = session_account["Username"]
                        print("========================================================================")
                        print("| Sukses: Password berhasil di update!                                 |")
                        print("========================================================================")
                        break
                    indeks += 1
            else:
                print("========================================================================")
                print("| Error: Password dan Konfirmasi Password berbeda!                     |")
                print("========================================================================")
                return back_to_pengaturan_akun()
            with open(csv_filename_accounts, mode="w") as csv_file:
                fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for new_data in akun:
                    csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
            return back_to_show_menu()
        else:
            print("========================================================================")
            print("| Error: Password Lama anda salah!                                     |")
            print("========================================================================")
            return back_to_pengaturan_akun()
    elif selected_menu == "2":
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_pengaturan_akun()

def back_to_pengaturan_akun():
    input("\nTekan 'Enter' untuk kembali...")
    return pengaturan_akun()

def feedback():
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
            return feedback_developer()
        elif selected_menu == "2":
            return feedback_dinkes()
        elif selected_menu == "3":
            return show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_feedback()
    elif session_account["Level"] == "dinkes":
        if selected_menu == "1":
            return feedback_developer()
        elif selected_menu == "2":
            return show_menu()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_feedback()

def back_to_feedback():
    input("\nTekan 'Enter' untuk kembali...")
    return feedback()

def feedback_developer():
    clear_screen()
    print("========================================================================")
    print("|                           KRITIK DAN SARAN                           |")
    print("========================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Developer               |")
    print("========================================================================")
    kritik = input("Kritik : ")
    saran = input("Saran  : ")
    if len(kritik) > 0 or len(saran) > 0:
        with open(csv_filename_feedback, mode="a") as csv_file:
            fieldnames = ["Timestamp", "Jenis", "Nama", "Kritik", "Saran"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow({"Timestamp": timestamp_now(), "Jenis": "Developer", "Nama": session_account["Nama"], "Kritik": kritik, "Saran": saran})
        print("========================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                          |")
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Kritik atau saran harus diisi!                                |")
        print("========================================================================")
    return back_to_show_menu()

def feedback_dinkes():
    clear_screen()
    print("========================================================================")
    print("|                           KRITIK DAN SARAN                           |")
    print("========================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Dinkes                  |")
    print("========================================================================")
    kritik = input("Kritik : ")
    saran = input("Saran  : ")
    if len(kritik) > 0 or len(saran) > 0:
        with open(csv_filename_feedback, mode="a") as csv_file:
            fieldnames = ["Timestamp", "Jenis", "Nama", "Kritik", "Saran"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow({"Timestamp": timestamp_now(), "Jenis": "Dinkes", "Nama": session_account["Nama"], "Kritik": kritik, "Saran": saran})
        print("========================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                          |")
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Kritik atau saran harus diisi!                                |")
        print("========================================================================")
    return back_to_show_menu()

def show_feedback():
    clear_screen()
    print("========================================================================")
    if session_account["Level"] == "dinkes":
        print("|                        KRITIK DAN SARAN DINKES                       |")
    elif session_account["Level"] == "admin":
        print("|                      KRITIK DAN SARAN DEVELOPER                      |")
    print("========================================================================")
    kritik_saran = []
    with open(csv_filename_feedback, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            kritik_saran.append(row)
    data_found = False
    for data in kritik_saran:
        if session_account["Level"] == "dinkes":
            if data["Jenis"] == "Dinkes":
                print("| Timestamp :", data["Timestamp"])
                print("| Nama      :", data["Nama"])
                print("| Kritik    :", data["Kritik"])
                print("| Saran     :", data["Saran"])
                print("========================================================================")
                data_found = True
        elif session_account["Level"] == "admin":
            if data["Jenis"] == "Developer":
                print("| Timestamp :", data["Timestamp"])
                print("| Nama      :", data["Nama"])
                print("| Kritik    :", data["Kritik"])
                print("| Saran     :", data["Saran"])
                print("========================================================================")
                data_found = True
    if data_found == False:
        print("========================================================================")
        print("| Error: Tidak ada data ditemukan!                                     |")
        print("========================================================================")
    return back_to_show_menu()

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
            if data["Level"] == "admin":
                print("| Username :", data["Username"])
                print("| Password :", data["Password"])
                print("| Level    :", data["Level"])
                print("| Nama     :", data["Nama"])
                print("| Created  :", data["Created"])
                print("| Updated  :", data["Updated"])
                print("| Log      :", data["Log"])
            elif data["Level"] == "dinkes":
                print("| Username :", data["Username"])
                print("| Password :", data["Password"])
                print("| Level    :", data["Level"])
                print("| NIK      :", data["NIK"])
                print("| NIP      :", data["NIP"])
                print("| Nama     :", data["Nama"])
                print("| Created  :", data["Created"])
                print("| Updated  :", data["Updated"])
                print("| Log      :", data["Log"])
            elif data["Level"] == "pasien":
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
                print("| Updated   :", data["Updated"])
                print("| Log       :", data["Log"])
            print("========================================================================")
    else:
        print("========================================================================")
        print("| Error: Tidak ada data pengguna ditemukan!                            |")
        print("========================================================================")
    return back_to_show_menu()

def create_account():
    clear_screen()
    print("========================================================================")
    print("|                          BUAT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Pasien                                                           |")
    print("| [2] Dinkes                                                           |")
    print("| [3] Kembali                                                          |")
    print("========================================================================")
    selected_menu = input("Masukkan Pilihan> ")
    if selected_menu == "1":
        clear_screen()
        print("========================================================================")
        print("|                          BUAT AKUN PENGGUNA                          |")
        print("========================================================================")
        print("| Info: Silakan isi Username, Password, NIK, Nama, Umur, No. HP, dan   |")
        print("|       Alamat akun pengguna                                           |")
        print("========================================================================")
        try:
            username = input("Username : ")
            if len(username) < 4:
                print("========================================================================")
                print("| Error: Username minimal 4 karakter!                                  |")
                print("========================================================================")
                return back_to_create_account()
            password = input("Password : ")
            if len(password) < 8:
                print("========================================================================")
                print("| Error: Password minimal 8 karakter!                                  |")
                print("========================================================================")
                return back_to_create_account()
            nik = int(input("NIK      : "))
            nama = input("Nama     : ")
            if len(nama) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan Nama                           |")
                print("========================================================================")
                return back_to_create_account()
            umur = int(input("Umur     : "))
            nohp = int(input("No. HP   : "))
            alamat = input("Alamat   : ")
            if len(alamat) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan Alamat                         |")
                print("========================================================================")
                return back_to_create_account()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_create_account()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
        if data_found == True:
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            return back_to_create_account()
        with open(csv_filename_accounts, mode="a") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow({"Username": username, "Password": password, "Level": "pasien", "NIK": nik, "NIP": "", "Nama": nama, "Umur": umur, "NoHP": nohp, "Alamat": alamat, "Vaksinasi": "False", "Created": timestamp_now(), "Updated": timestamp_now(), "Log": username})
            print("========================================================================")
            print("| Sukses: Akun Baru berhasil dibuat dan disimpan!                      |")
            print("========================================================================")
    elif selected_menu == "2":
        clear_screen()
        print("========================================================================")
        print("|                          BUAT AKUN PENGGUNA                          |")
        print("========================================================================")
        print("| Info: Silakan isi Username, Password, NIK, NIP, Nama akun pengguna   |")
        print("========================================================================")
        try:
            username = input("Username : ")
            if len(username) < 4:
                print("========================================================================")
                print("| Error: Username minimal 4 karakter!                                  |")
                print("========================================================================")
                return back_to_create_account()
            password = input("Password : ")
            if len(password) < 8:
                print("========================================================================")
                print("| Error: Password minimal 8 karakter!                                  |")
                print("========================================================================")
                return back_to_create_account()
            nik = int(input("NIK      : "))
            nip = int(input("NIP      : "))
            nama = input("Nama     : ")
            if len(nama) < 1:
                print("========================================================================")
                print("| Error: Anda tidak dapat mengosongkan Nama                           |")
                print("========================================================================")
                return back_to_create_account()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_show_menu()
        akun = []
        with open(csv_filename_accounts, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = False
        for data in akun:
            if data["Username"] == username:
                data_found = True
                break
        if data_found == True:
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            return back_to_create_account()
        with open(csv_filename_accounts, mode="a") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writerow({"Username": username, "Password": password, "Level": "dinkes", "NIK": nik, "NIP": nip, "Nama": nama, "Umur": "", "NoHP": "", "Alamat": "", "Vaksinasi": "", "Created": timestamp_now(), "Updated": timestamp_now(), "Log": username})
            print("========================================================================")
            print("| Sukses: Akun Baru berhasil dibuat dan disimpan!                      |")
            print("========================================================================")
    elif selected_menu == "3":
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_create_account()
    return back_to_show_menu()

def back_to_create_account():
    input("\nTekan 'Enter' untuk kembali...")
    return create_account()

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
        if data["Level"] == "dinkes":
            print("| Username :", data["Username"])
            print("| Password :", data["Password"])
            print("| Level    :", data["Level"])
            print("| NIK      :", data["NIK"])
            print("| NIP      :", data["NIP"])
            print("| Nama     :", data["Nama"])
            print("| Created  :", data["Created"])
            print("| Updated  :", data["Updated"])
            print("| Log      :", data["Log"])
            print("========================================================================")
        elif data["Level"] == "pasien":
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
            print("| Updated   :", data["Updated"])
            print("| Log       :", data["Log"])
            print("========================================================================")
    username = input("Masukkan Username : ")
    if username == session_account["Username"]:
        print("========================================================================")
        print("| Error: Anda tidak dapat mengedit akun anda sendiri!                  |")
        print("========================================================================")
        return back_to_edit_account()
    else:
        data_found = False
        indeks = 0
        for data in akun:
            if data["Username"] == username and not data["Level"] == "admin":
                print("========================================================================")
                print("| Sukses: Data Akun ditemukan!                                         |")
                print("========================================================================")
                if data["Level"] == "dinkes":
                    print("| [1] Username                                                         |")
                    print("| [2] Password                                                         |")
                    print("| [3] NIK                                                              |")
                    print("| [4] NIP                                                              |")
                    print("| [5] Nama                                                             |")
                    print("| [6] Kembali                                                          |")
                elif data["Level"] == "pasien":
                    print("| [1] Username                                                         |")
                    print("| [2] Password                                                         |")
                    print("| [3] NIK                                                              |")
                    print("| [4] Nama                                                             |")
                    print("| [5] Umur                                                             |")
                    print("| [6] No HP                                                            |")
                    print("| [7] Alamat                                                           |")
                    print("| [8] Kembali                                                          |")
                print("========================================================================")
                selected_menu = input("Pilih Menu> ")
                if selected_menu == "1":
                    new_username = input("Username Baru : ")
                    if len(new_username) < 4:
                        print("========================================================================")
                        print("| Error: Username minimal 4 karakter!                                  |")
                        print("========================================================================")
                        return back_to_edit_account()
                    data_found = False
                    for data in akun:
                        if data["Username"] == new_username:
                            data_found = True
                            break
                    if data_found == True:
                        print("========================================================================")
                        print("| Error: Username tersebut telah didaftarkan!                          |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["Username"] = new_username
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "2":
                    new_password = input("Password Baru : ")
                    if len(new_password) < 8:
                        print("========================================================================")
                        print("| Error: Password minimal 8 karakter!                                  |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["Password"] = new_password
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "3":
                    try:
                        new_nik = int(input("NIK Baru : "))
                    except ValueError:
                        print("========================================================================")
                        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["NIK"] = new_nik
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "4" and data["Level"] == "dinkes":
                    try:
                        new_nip = int(input("NIP Baru : "))
                    except ValueError:
                        print("========================================================================")
                        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["NIP"] = new_nip
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "4" and data["Level"] == "pasien" or selected_menu == "5" and data["Level"] == "dinkes":
                    new_nama = input("Nama Baru : ")
                    if len(new_nama) < 1:
                        print("========================================================================")
                        print("| Error: Anda tidak dapat mengosongkan Nama                            |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["Nama"] = new_nama
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "5" and data["Level"] == "pasien":
                    try:
                        new_umur = int(input("Umur Baru : "))
                    except ValueError:
                        print("========================================================================")
                        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["Umur"] = new_umur
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "6" and data["Level"] == "pasien":
                    try:
                        new_nohp = int(input("No HP Baru : "))
                    except ValueError:
                        print("========================================================================")
                        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["NoHP"] = new_nohp
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "7" and data["Level"] == "pasien":
                    new_alamat = input("Alamat Baru : ")
                    if len(new_alamat) < 1:
                        print("========================================================================")
                        print("| Error: Anda tidak dapat mengosongkan Alamat                          |")
                        print("========================================================================")
                        return back_to_edit_account()
                    akun[indeks]["Alamat"] = new_alamat
                    akun[indeks]["Updated"] = timestamp_now()
                    akun[indeks]["Log"] = session_account["Username"]
                elif selected_menu == "8" and data["Level"] == "pasien" or selected_menu == "6" and data["Level"] == "dinkes":
                    return show_menu()
                else:
                    print("========================================================================")
                    print("| Error: Anda memilih menu yang salah!                                 |")
                    print("========================================================================")
                    return back_to_edit_account()
                print("========================================================================")
                print("| Sukses: Akun berhasil di update!                                     |")
                print("========================================================================")
                with open(csv_filename_accounts, mode="w") as csv_file:
                    fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for new_data in akun:
                        csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
                data_found = True
                break
            indeks += 1
        if data_found == False:
            print("========================================================================")
            print("| Error: Username tidak ditemukan!                                     |")
            print("========================================================================")
    return back_to_show_menu()

def back_to_edit_account():
    input("\nTekan 'Enter' untuk kembali...")
    return edit_account()

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
        if data["Level"] == "dinkes":
            print("| Username :", data["Username"])
            print("| Password :", data["Password"])
            print("| Level    :", data["Level"])
            print("| NIK      :", data["NIK"])
            print("| NIP      :", data["NIP"])
            print("| Nama     :", data["Nama"])
            print("| Created  :", data["Created"])
            print("| Updated  :", data["Updated"])
            print("| Log      :", data["Log"])
            print("========================================================================")
        elif data["Level"] == "pasien":
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
            print("| Updated   :", data["Updated"])
            print("| Log       :", data["Log"])
            print("========================================================================")
    username = input("Masukkan Username : ")
    if username == session_account["Username"]:
        print("========================================================================")
        print("| Error: Anda tidak dapat menghapus akun anda sendiri!                 |")
        print("========================================================================")
    else:
        data_found = False
        indeks = 0
        for data in akun:
            if data["Username"] == username:
                akun.remove(akun[indeks])
                data_found = True
                print("========================================================================")
                print("| Sukses: Akun berhasil di hapus!                                      |")
                print("========================================================================")
                break
            indeks += 1
        if data_found == False:
            print("========================================================================")
            print("| Error: Username tidak ditemukan!                                     |")
            print("========================================================================")
        with open(csv_filename_accounts, mode="w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for new_data in akun:
                csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
    return back_to_show_menu()

def sort_account():
    clear_screen()
    print("========================================================================")
    print("|                          URUT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1]  Username                                                        |")
    print("| [2]  Level                                                           |")
    print("| [3]  NIK                                                             |")
    print("| [4]  NIP                                                             |")
    print("| [5]  Nama                                                            |")
    print("| [6]  Umur                                                            |")
    print("| [7]  No. HP                                                          |")
    print("| [8]  Alamat                                                          |")
    print("| [9]  Vaksinasi                                                       |")
    print("| [10] Created                                                         |")
    print("| [11] Updated                                                         |")
    print("| [12] Log                                                             |")
    print("| [13] Kembali                                                         |")
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
        sorting = "NIP"
    elif selected_menu == "5":
        sorting = "Nama"
    elif selected_menu == "6":
        sorting = "Umur"
    elif selected_menu == "7":
        sorting = "NoHP"
    elif selected_menu == "8":
        sorting = "Alamat"
    elif selected_menu == "9":
        sorting = "Vaksinasi"
    elif selected_menu == "10":
        sorting = "Created"
    elif selected_menu == "11":
        sorting = "Updated"
    elif selected_menu == "12":
        sorting = "Log"
    elif selected_menu == "13":
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_sort_account()
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
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_sort_account()
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
        return sort_account()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_sort_account()
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
            elif sorting == "Updated":
                datasort.append([data["Updated"], indeks])
            elif sorting == "Log":
                datasort.append([data["Log"], indeks])
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
            akun.append({"Username": old_akun[datasort[i][1]]["Username"], "Password": old_akun[datasort[i][1]]["Password"], "Level": old_akun[datasort[i][1]]["Level"], "NIK": old_akun[datasort[i][1]]["NIK"], "NIP": old_akun[datasort[i][1]]["NIP"], "Nama": old_akun[datasort[i][1]]["Nama"], "Umur": old_akun[datasort[i][1]]["Umur"], "NoHP": old_akun[datasort[i][1]]["NoHP"], "Alamat": old_akun[datasort[i][1]]["Alamat"], "Vaksinasi": old_akun[datasort[i][1]]["Vaksinasi"], "Created": old_akun[datasort[i][1]]["Created"], "Updated": old_akun[datasort[i][1]]["Updated"], "Log": old_akun[datasort[i][1]]["Log"]})
        with open(csv_filename_accounts, mode="w") as csv_file:
            fieldnames = ["Username", "Password", "Level", "NIK", "NIP", "Nama", "Umur", "NoHP", "Alamat", "Vaksinasi", "Created", "Updated", "Log"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for new_data in akun:
                csv_writer.writerow({"Username": new_data["Username"], "Password": new_data["Password"], "Level": new_data["Level"], "NIK": new_data["NIK"], "NIP": new_data["NIP"], "Nama": new_data["Nama"], "Umur": new_data["Umur"], "NoHP": new_data["NoHP"], "Alamat": new_data["Alamat"], "Vaksinasi": new_data["Vaksinasi"], "Created": new_data["Created"], "Updated": new_data["Updated"], "Log": new_data["Log"]})
        print("========================================================================")
        print("| Sukses: Data Pengguna berhasil diurutkan                             |")
        print("========================================================================")
    return back_to_show_menu()

def back_to_sort_account():
    input("\nTekan 'Enter' untuk kembali...")
    return sort_account()

def search_account():
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1]  Username                                                        |")
    print("| [2]  Level                                                           |")
    print("| [3]  NIK                                                             |")
    print("| [4]  NIP                                                             |")
    print("| [5]  Nama                                                            |")
    print("| [6]  Umur                                                            |")
    print("| [7]  No. HP                                                          |")
    print("| [8]  Alamat                                                          |")
    print("| [9]  Vaksinasi                                                       |")
    print("| [10] Created                                                         |")
    print("| [11] Updated                                                         |")
    print("| [12] Log                                                             |")
    print("| [13] Kembali                                                         |")
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
        searching = "NIP"
    elif selected_menu == "5":
        searching = "Nama"
    elif selected_menu == "6":
        searching = "Umur"
    elif selected_menu == "7":
        searching = "NoHP"
    elif selected_menu == "8":
        searching = "Alamat"
    elif selected_menu == "9":
        searching = "Vaksinasi"
    elif selected_menu == "10":
        searching = "Created"
    elif selected_menu == "11":
        searching = "Updated"
    elif selected_menu == "12":
        searching = "Log"
    elif selected_menu == "13":
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_search_account()
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| [1] Metode Linear Search                                             |")
    print("| [2] Metode Binary Search                                             |")
    if searching == "NIK" or searching == "NIP" or searching == "Umur" or searching == "NoHP":
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
    if searching == "NIK" or searching == "NIP" or searching == "Umur" or searching == "NoHP":
        if selected_menu == "1" or selected_menu == "2":
            pass
        elif selected_menu == "3":
            metode_searching = "Interpolation"
        elif selected_menu == "4":
            return search_account()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_search_account()
    else:
        if selected_menu == "1" or selected_menu == "2":
            pass
        elif selected_menu == "3":
            return search_account()
        else:
            print("========================================================================")
            print("| Error: Anda memilih menu yang salah!                                 |")
            print("========================================================================")
            return back_to_search_account()
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
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
        return show_menu()
    else:
        print("========================================================================")
        print("| Error: Anda memilih menu yang salah!                                 |")
        print("========================================================================")
        return back_to_search_account()
    clear_screen()
    print("========================================================================")
    print("|                          CARI AKUN PENGGUNA                          |")
    print("========================================================================")
    if searching == "NIK" or searching == "NIP" or searching == "Umur" or searching == "NoHP":
        try:
            search = int(input("Data yang ingin dicari> "))
            if search < 1:
                print("========================================================================")
                print("| Gagal: Tidak dapat mencari data kurang dari 1!                       |")
                print("========================================================================")
                return back_to_search_account()
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            return back_to_search_account()
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
        elif searching == "NIP":
            datasort.append([int(data["NIP"]), indeks])
        elif searching == "Nama":
            datasort.append([data["Nama"], indeks])
        elif searching == "Umur":
            datasort.append([int(data["Umur"]), indeks])
        elif searching == "NoHP":
            datasort.append([int(data["NoHP"]), indeks])
        elif searching == "Alamat":
            datasort.append([data["Alamat"], indeks])
        elif searching == "Vaksinasi":
            datasort.append([data["Vaksinasi"], indeks])
        elif searching == "Created":
            datasort.append([data["Created"], indeks])
        elif searching == "Updated":
            datasort.append([data["Updated"], indeks])
        elif searching == "Log":
            datasort.append([data["Log"], indeks])
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
    if searching == "NIK" or searching == "NIP" or searching == "Umur" or searching == "NoHP":
        if metode_searching == "Linear":
            result = linearSearch(datasearch, len(datasearch), search)
        elif metode_searching == "Binary":
            result = binarySearch(datasearch, search, 0, len(datasearch) - 1)
        elif metode_searching == "Interpolation":
            result = interpolationSearch(datasearch, 0, len(datasearch) - 1, search)
    else:
        if metode_searching == "Linear":
            result = linearSearch(datasearch, len(datasearch), search)
        elif metode_searching == "Binary":
            result = binarySearch(datasearch, search, 0, len(datasearch) - 1)
    if result != -1:
        print("========================================================================")
        print("| Sukses: Data Pengguna ditemukan!                                     |")
        print("========================================================================")
        print("| Pengguna ke-%d" % datasort[result][1])
        if akun[datasort[result][1]]["Level"] == "admin":
            print("| Username :", akun[datasort[result][1]]["Username"])
            print("| Password :", akun[datasort[result][1]]["Password"])
            print("| Level    :", akun[datasort[result][1]]["Level"])
            print("| Nama     :", akun[datasort[result][1]]["Nama"])
            print("| Created  :", akun[datasort[result][1]]["Created"])
            print("| Updated  :", akun[datasort[result][1]]["Updated"])
            print("| Log      :", akun[datasort[result][1]]["Log"])
        elif akun[datasort[result][1]]["Level"] == "dinkes":
            print("| Username :", akun[datasort[result][1]]["Username"])
            print("| Password :", akun[datasort[result][1]]["Password"])
            print("| Level    :", akun[datasort[result][1]]["Level"])
            print("| NIK      :", akun[datasort[result][1]]["NIK"])
            print("| NIP      :", akun[datasort[result][1]]["NIP"])
            print("| Nama     :", akun[datasort[result][1]]["Nama"])
            print("| Created  :", akun[datasort[result][1]]["Created"])
            print("| Updated  :", akun[datasort[result][1]]["Updated"])
            print("| Log      :", akun[datasort[result][1]]["Log"])
        elif akun[datasort[result][1]]["Level"] == "pasien":
            print("| Username  :", akun[datasort[result][1]]["Username"])
            print("| Password  :", akun[datasort[result][1]]["Password"])
            print("| Level     :", akun[datasort[result][1]]["Level"])
            print("| NIK       :", akun[datasort[result][1]]["NIK"])
            print("| Nama      :", akun[datasort[result][1]]["Nama"])
            print("| Umur      :", akun[datasort[result][1]]["Umur"])
            print("| No HP     :", akun[datasort[result][1]]["NoHP"])
            print("| Alamat    :", akun[datasort[result][1]]["Alamat"])
            print("| Vaksinasi :", akun[datasort[result][1]]["Vaksinasi"])
            print("| Created   :", akun[datasort[result][1]]["Created"])
            print("| Updated   :", akun[datasort[result][1]]["Updated"])
            print("| Log       :", akun[datasort[result][1]]["Log"])
        print("========================================================================")
    else:
        print("========================================================================")
        print("| Gagal: Data Pengguna tidak ditemukan!                                |")
        print("========================================================================")
    return back_to_show_menu()

def back_to_search_account():
    input("\nTekan 'Enter' untuk kembali...")
    return search_account()

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
