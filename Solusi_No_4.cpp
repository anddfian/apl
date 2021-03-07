#include <iostream>
using namespace std;
 
struct KTM
{
    long int nim;
    string nama;
    string ttl;
    string jenis_kelamin;
    string prodi;
    string agama;
    string status_perkawinan;
    string pekerjaan;
    string kewarganegaraan;
    string berlaku;
};
 
int main()
{
	system("Color C");
	cout << "=====================================================================" << endl;
	cout << "|                    PROGRAM MENGGUNAKAN POINTER                    |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|                          OLEH KELOMPOK 27                         |" << endl;
	cout << "=====================================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR (2009106002)                                  |" << endl;
	cout << "| RIZKI ANDRIYANTI    (2009106118)                                  |" << endl;
	cout << "| LIDYA SIMANUNGKALIT (2009106125)                                  |" << endl;
	cout << "| AL-INAYYA           (2009106127)                                  |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|    PROGRAM INI DIKERJAKAN OLEH LIDYA SIMANUNGKALIT (2009106125)   |" << endl;
	cout << "=====================================================================" << endl;
    struct KTM *identitas, kartu;
    kartu.nim = 2009106125;
    kartu.nama = "LIDYA";
    kartu.ttl = "MEDAN, 05 - 01 - 2003";
    kartu.jenis_kelamin = "WANITA";
    kartu.prodi = "INFORMATIKA (FAKULTAS TEKNIK)";
    kartu.agama = "KRISTEN";
    kartu.status_perkawinan = "BELUM KAWIN";
    kartu.pekerjaan = "MAHASISWA";
    kartu.kewarganegaraan = "WNI";
    kartu.berlaku = "21 - 01 - 2023";
    identitas = &kartu; 
    cout << " Nomor Induk Mahasiswa\t\t: " << identitas->nim << endl;
    cout << " Nama\t\t\t\t: " << identitas->nama << endl;
    cout << " Tempat / Tanggal Lahir\t\t: " << identitas->ttl << endl;
    cout << " Jenis Kelamin\t\t\t: " << identitas->jenis_kelamin << endl;
    cout << " Prodi\t\t\t\t: " << identitas->prodi << endl;
    cout << " Agama\t\t\t\t: " << identitas->agama << endl;
    cout << " Status Perkawinan\t\t: " << identitas->status_perkawinan << endl;
    cout << " Pekerjaan\t\t\t: " << identitas->pekerjaan << endl;
    cout << " Kewarganegaraan\t\t: " << identitas->kewarganegaraan << endl;
    cout << " Berlaku Hingga\t\t\t: " << identitas->berlaku << endl;
	return 0;
}
