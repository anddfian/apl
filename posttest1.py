import os

nim = [2, 0, 0, 9, 1, 0, 6, 0, 0, 2]
new_nim = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    clear_screen()
    print("========== APLIKASI LIST ==========")
    print("[1] Lihat Data List")
    print("[2] Menambahkan Data List")
    print("[3] Menghapus Data List")
    print("[4] Mengupdate Data List")
    print("[5] Mengurutkan Data List")
    print("[6] Mencari Min dan Max Data List")
    print("[7] Menghitung Banyak Data List")
    print("[8] Membalikkan Urutan List")
    print("[9] Mencari Data List")
    print("[10] Menyalin Data List")
    print("[0] Exit")
    print("-----------------------------------")
    selected_menu = input("Pilih menu> ")
    if(selected_menu == "1"):
        clear_screen()
        print("========== DATA LIST ==========")
        print(nim)
        back_to_show_menu()
    elif(selected_menu == "2"):
        clear_screen()
        print("========== TAMBAH DATA LIST ==========")
        print("[1] Menggunakan Metode Append")
        print("[2] Menggunakan Metode Extend")
        print("[3] Menggunakan Metode Insert")
        print("[4] Back")
        print("[0] Exit")
        print("-----------------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            add_list_append()
        elif(selected_menu == "2"):
            add_list_extend()
        elif(selected_menu == "3"):
            add_list_insert()
        elif(selected_menu == "4"):
            show_menu()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_show_menu()
    elif(selected_menu == "3"):
        clear_screen()
        print("========== HAPUS DATA LIST ==========")
        print("[1] Menggunakan Metode Remove")
        print("[2] Menggunakan Metode Pop")
        print("[3] Menggunakan Metode Clear")
        print("[4] Back")
        print("[0] Exit")
        print("-----------------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            delete_list_remove()
        elif(selected_menu == "2"):
            delete_list_pop()
        elif(selected_menu == "3"):
            delete_list_clear()
        elif(selected_menu == "4"):
            show_menu()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_show_menu()
    elif(selected_menu == "4"):
        update_list()
    elif(selected_menu == "5"):
        clear_screen()
        print("========== SORT DATA LIST ==========")
        print("[1] Secara Ascending")
        print("[2] Secara Descending")
        print("[3] Back")
        print("[0] Exit")
        print("-----------------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            sort_list_asc()
        elif(selected_menu == "2"):
            sort_list_desc()
        elif(selected_menu == "3"):
            show_menu()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_show_menu()
    elif(selected_menu == "6"):
        min_max_list()
    elif(selected_menu == "7"):
        clear_screen()
        print("========== TOTAL DATA LIST ==========")
        print("[1] Jumlah data")
        print("[2] Jumlah suatu data")
        print("[3] Total data")
        print("[0] Exit")
        print("-----------------------------------")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            total_list_len()
        elif(selected_menu == "2"):
            total_list_count()
        elif(selected_menu == "3"):
            total_list_sum()
        elif(selected_menu == "0"):
            exit()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_show_menu()
    elif(selected_menu == "8"):
        reverse_list()
    elif(selected_menu == "9"):
        index_list()
    elif(selected_menu == "10"):
        copy_list()
    elif(selected_menu == "0"):
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_show_menu()

def back_to_show_menu():
    input("\nTekan 'Enter' untuk kembali ke menu utama...")
    show_menu()

def add_list_append():
    clear_screen()
    print("========== TAMBAH DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        new_data = int(input("Masukkan data yang ingin ditambahkan: "))
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        add_list_append()
    nim.append(new_data)
    print("Data", new_data, "berhasil ditambahkan!")
    print("List saat ini:", nim)
    back_to_show_menu()

def add_list_extend():
    clear_screen()
    print("========== TAMBAH DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        new_list = []
        n = int(input("Masukkan jumlah data list baru yang ingin ditambahkan: "))
        while n > 0:
            new_element = int(input("Masukkan elemen yang ingin ditambahkan pada list baru: "))
            new_list.append(new_element)
            n -= 1 
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        add_list_extend()
    nim.extend(new_list)
    print("List", new_list, "berhasil ditambahkan!")
    print("List saat ini:", nim)
    back_to_show_menu()

def add_list_insert():
    clear_screen()
    print("========== TAMBAH DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        index = int(input("Masukkan indeks data yang ingin ditambahkan: "))
        new_data = int(input("Masukkan data yang ingin ditambahkan: "))
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        add_list_insert()
    nim.insert(index, new_data)
    print("Data", new_data, "pada indeks" + index + "berhasil ditambahkan!")
    print("List saat ini:", nim)
    back_to_show_menu()

def delete_list_remove():
    clear_screen()
    print("========== HAPUS DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        datat = int(input("Masukkan data yang ingin dihapus: "))
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        delete_list_remove()
    try:
        nim.remove(datat)
        print("Data", datat, "berhasil dihapus!")
    except(ValueError):
        print("Data", datat, "gagal dihapus karena tidak ada di list!")
    print("List saat ini:", nim)
    back_to_show_menu()

def delete_list_pop():
    clear_screen()
    print("========== HAPUS DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        index = int(input("Masukkan indeks data yang ingin dihapus: "))
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        delete_list_pop()
    nim.pop(index)
    print("Data pada indeks", index, "berhasil dihapus!")
    print("List saat ini:", nim)
    back_to_show_menu()

def delete_list_clear():
    clear_screen()
    print("========== HAPUS DATA LIST ==========")
    print("List saat ini:", nim)
    nim.clear()
    print("Semua data pada list berhasil dihapus!")
    print("List saat ini:", nim)
    back_to_show_menu()

def update_list():
    clear_screen()
    print("========== UPDATE DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        index = int(input("Masukkan indeks data yang ingin diperbaharui: "))
        new_data = int(input("Masukkan data yang ingin diperbaharui: "))
    except(TypeError):
        print("Hanya boleh masukkan data angka!")
        input("Tekan 'Enter' untuk melanjutkan...")
        update_list()
    nim[index] = new_data
    print("Data", new_data, "pada indeks" + index + "berhasil diperbaharui!")
    print("List saat ini:", nim)
    back_to_show_menu()

def sort_list_asc():
    clear_screen()
    print("========== SORT DATA LIST ==========")
    print("List saat ini:", nim)
    nim.sort()
    print("Data pada list berhasil diurutkan secara ascending.")
    print("List saat ini:", nim)
    back_to_show_menu()

def sort_list_desc():
    clear_screen()
    print("========== SORT DATA LIST ==========")
    print("List saat ini:", nim)
    nim.sort(reverse=True)
    print("Data pada list berhasil diurutkan secara descending.")
    print("List saat ini:", nim)
    back_to_show_menu()

def min_max_list():
    clear_screen()
    print("========== MIN MAX DATA LIST ==========")
    nim_min = nim[0]
    nim_max = nim[0]
    for i in nim:
        if(nim_min > i):
            nim_min = i
        elif(nim_max < i):
            nim_max = i
    print("List saat ini:", nim)
    print("Min data:", nim_min)
    print("Max data:", nim_max)
    back_to_show_menu()

def total_list_len():
    clear_screen()
    print("========== TOTAL DATA LIST ==========")
    print("List saat ini:", nim)
    print("Jumlah data pada list:", len(nim))
    back_to_show_menu()    

def total_list_count():
    clear_screen()
    print("========== TOTAL DATA LIST ==========")
    print("List saat ini:", nim)
    count = int(input("Masukkan data yang ingin dijumlah: "))
    print("Jumlah data", count, "pada list:", nim.count(count))
    back_to_show_menu()    

def total_list_sum():
    clear_screen()
    print("========== TOTAL DATA LIST ==========")
    sum_nim = 0
    for i in nim:
        sum_nim += i
    print("List saat ini:", nim)
    print("Total data pada list:", sum_nim)
    back_to_show_menu()    

def reverse_list():
    clear_screen()
    print("========== REVERSE DATA LIST ==========")
    print("List saat ini:", nim)
    nim.reverse()
    print("Urutan data pada list berhasil dibalikkan.")
    print("List saat ini:", nim)
    back_to_show_menu()

def index_list():
    clear_screen()
    print("========== INDEX DATA LIST ==========")
    print("List saat ini:", nim)
    try:
        element = int(input("Masukkan data yang ingin dicari: "))
        print("Data", element, "berada pada indeks", nim.index(element))
    except(ValueError):
        print("Data", element, "tidak ada di dalam list")
    back_to_show_menu()

def copy_list():
    clear_screen()
    print("========== COPY DATA LIST ==========")
    print("List saat ini:", nim)
    new_nim = nim.copy()
    print("List nim berhasil di copy ke new_nim")
    print("List new_nim saat ini:", new_nim)
    back_to_show_menu()

if __name__ == "__main__":
    while True:
        show_menu()
