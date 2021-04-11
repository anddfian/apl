import os

vaksinasi = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("| [1] Daftar Vaksinasi COVID-19           |")
    print("| [2] Proses Vaksinasi COVID-19           |")
    print("| [3] Data Vaksinasi COVID-19             |")
    print("| [0] Keluar Aplikasi                     |")
    print("===========================================")
    selected_menu = str(input("Pilih menu> "))
    if(selected_menu == "1"):
        daftar_vaksinasi()
    elif(selected_menu == "2"):
        meja_pertama()
    elif(selected_menu == "3"):
        data_vaksinasi()
    elif(selected_menu == "0"):
        exit()
    else:
        print("===========================================")
        print("| Error: Anda memilih menu yang salah!    |")
        print("===========================================")
        back_to_show_menu()

def back_to_show_menu():
    input("\nTekan 'Enter' untuk kembali...")
    show_menu()

def query_daftar(nik, nama):
    for i in range(len(vaksinasi)):
        if(vaksinasi[i][1] == nik and vaksinasi[i][2] == nama):
            return True
    return False

def query_meja_pertama(eticket, nik):
    for i in range(len(vaksinasi)):
        if(vaksinasi[i][0] == eticket and vaksinasi[i][1] == nik):
            return vaksinasi[i][3]
    return -1

def query_indeks(nik):
    for i in range(len(vaksinasi)):
        if(vaksinasi[i][1] == nik):
            return i
    return -1

def query_data(nik, nama):
    for i in range(len(vaksinasi)):
        if(vaksinasi[i][1] == nik and vaksinasi[i][2] == nama):
            return i
    return -1

def insert_daftar(nik, nama):
    nomor = len(vaksinasi)+1
    vaksinasi.append([nomor, nik, nama, 0])
    return nomor

def insert_meja_kedua(indeks, tahap, suhu, tekanan_darah):
    if(tahap == 0):
        vaksinasi[indeks] += [[suhu], [tekanan_darah]]
    else:
        vaksinasi[indeks][4] += [suhu]
        vaksinasi[indeks][5] += [tekanan_darah]
    return True

def insert_meja_ketiga(indeks, tahap, nama_vaksin, nomor_batch_vaksin):
    if(tahap == 0):
        vaksinasi[indeks] += [[nama_vaksin], [nomor_batch_vaksin]]
    else:
        vaksinasi[indeks][6] += [nama_vaksin]
        vaksinasi[indeks][7] += [nomor_batch_vaksin]
    return True

def insert_meja_keempat(indeks, tahap, kipi):
    vaksinasi[indeks][3] += 1
    if(tahap == 0):
        vaksinasi[indeks] += [[kipi]]
    else:
        vaksinasi[indeks][8] += [kipi]
    return True

def daftar_vaksinasi():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    nik = int(input("Masukkan NIK           : "))
    nama = str(input("Masukkan Nama          : "))
    status = query_daftar(nik, nama)
    if(status == True):
        print("===========================================")
        print("| Error: Data anda telah terdaftar!       |")
        print("===========================================")
    else:
        status = insert_daftar(nik, nama)
        if(status != -1):
            print("Nomor Tiket Elektronik :", status)
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
    eticket = int(input("Masukkan E-Ticket : "))
    status = query_meja_pertama(eticket, nik)
    if(status >= 0 and status < 2):
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
    indeks = query_indeks(nik)
    status = insert_meja_kedua(indeks, tahap, suhu, tekanan_darah)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_ketiga(indeks, tahap)

def meja_ketiga(indeks, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|               MEJA KETIGA               |")
    print("===========================================")
    nama_vaksin = str(input("Masukkan Nama Vaksin        : "))
    nomor_batch_vaksin = int(input("Masukkan Nomor Batch Vaksin : "))
    status = insert_meja_ketiga(indeks, tahap, nama_vaksin, nomor_batch_vaksin)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        meja_keempat(indeks, tahap)

def meja_keempat(indeks, tahap):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|               MEJA KEEMPAT              |")
    print("===========================================")
    kipi = str(input("Masukkan KIPI : "))
    status = insert_meja_keempat(indeks, tahap, kipi)
    if(status == True):
        input("\nTekan 'Enter' untuk melanjutkan...")
        final_vaksinasi(indeks)

def final_vaksinasi(indeks):
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    print("|              DATA VAKSINASI             |")
    print("===========================================")
    print("E-Ticket           :", vaksinasi[indeks][0])
    print("NIK                :", vaksinasi[indeks][1])
    print("Nama               :", vaksinasi[indeks][2])
    print("Vaksinasi Ke       :", vaksinasi[indeks][3])
    print("Suhu Tubuh         :", vaksinasi[indeks][4])
    print("Tekanan Darah      :", vaksinasi[indeks][5])
    print("Nama Vaksin        :", vaksinasi[indeks][6])
    print("Nomor Batch Vaksin :", vaksinasi[indeks][7])
    print("KIPI               :", vaksinasi[indeks][8])
    back_to_show_menu()

def data_vaksinasi():
    clear_screen()
    print("===========================================")
    print("|       APLIKASI VAKSINASI COVID-19       |")
    print("===========================================")
    nik = int(input("Masukkan NIK  : "))
    nama = str(input("Masukkan Nama : "))
    indeks = query_data(nik, nama)
    if(indeks != -1):
        if(vaksinasi[indeks][3] == 0):
            print("===========================================")
            print("| Error: Anda belum di vaksin!            |")
            print("===========================================")
        else:
            print("===========================================")
            print("E-Ticket           :", vaksinasi[indeks][0])
            print("NIK                :", vaksinasi[indeks][1])
            print("Nama               :", vaksinasi[indeks][2])
            print("Vaksinasi Ke       :", vaksinasi[indeks][3])
            print("Suhu Tubuh         :", vaksinasi[indeks][4])
            print("Tekanan Darah      :", vaksinasi[indeks][5])
            print("Nama Vaksin        :", vaksinasi[indeks][6])
            print("Nomor Batch Vaksin :", vaksinasi[indeks][7])
            print("KIPI               :", vaksinasi[indeks][8])
    else:
        print("===========================================")
        print("| Error: Data anda tidak terdaftar!       |")
        print("===========================================")
    back_to_show_menu()

if __name__ == "__main__":
    while True:
        show_menu()
