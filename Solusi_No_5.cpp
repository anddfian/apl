#include<iostream>
using namespace std;

int main() {
	system("Color C");
	int baris, batas, segitiga_atas, segitiga_bawah;
	cout << "=====================================================================" << endl;
	cout << "|        PROGRAM MENAMPILKAN MATRIKS SEGITIGA ATAS DAN BAWAH        |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|                          OLEH KELOMPOK 27                         |" << endl;
	cout << "=====================================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR (2009106002)                                  |" << endl;
	cout << "| RIZKI ANDRIYANTI    (2009106118)                                  |" << endl;
	cout << "| LIDYA SIMANUNGKALIT (2009106125)                                  |" << endl;
	cout << "| AL-INAYYA           (2009106127)                                  |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|     PROGRAM INI DIKERJAKAN OLEH RIZKI ANDRIYANTI (2009106118)     |" << endl;
	cout << "=====================================================================" << endl;
	cout << "Jumlah Baris: ";
	cin >> baris;
	cout << "Angka Batas: ";
	cin >> batas;
	cout << "Angka Segitiga Atas: ";
	cin >> segitiga_atas;
	cout << "Angka Segitiga Bawah: ";
	cin >> segitiga_bawah;
	for(int i = 0; i < baris; i++) {
		for(int j = 0; j < baris; j++) {
			if(i == j) {
				cout << batas << " ";
			} else if (i <= j) {
				cout << segitiga_atas << " ";
			} else {
				cout << segitiga_bawah << " ";
			}
		}
		cout << endl;
	} 
	return 0;
}
