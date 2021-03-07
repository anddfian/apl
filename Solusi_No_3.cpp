#include <iostream>
using namespace std;

int main() {
	system("Color C");
	int i, j, k, uk_1, uk_2, uk_3;
	float jumlah_nilai, jumlah_elemen, nilai_rata_rata;
	cout << "=====================================================================" << endl;
	cout << "| PROGRAM MENAMPILKAN ARRAY MULTIDIMENSI DAN NILAI RATA-RATA ELEMEN |" << endl;
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
	cout << "Masukkan Jumlah Elemen Array Dimensi Pertama: ";
	cin >> uk_1;
	cout << "Masukkan Jumlah Elemen Aray Dimensi Kedua: ";
	cin >> uk_2;
	cout << "Masukkan Jumlah Elemen Array Dimensi Ketiga: ";
	cin >> uk_3;
	float matriks[uk_1][uk_2][uk_3];
	for(i = 0; i < uk_1; i++) {
		for(j = 0; j < uk_2; j++) {
			for(k = 0; k < uk_3; k++) {
		 		cout << "Masukkan Elemen Array [" << i << "][" << j << "][" << k << "] : ";
				cin >> matriks[i][j][k];
			}
		}
	}
	for(i = 0; i < uk_1; i++) {
		for(j = 0; j < uk_2; j++) {
			for(k = 0; k < uk_3; k++) {
		  		cout << matriks[i][j][k] << " ";
		  		jumlah_nilai += matriks[i][j][k];
		  		jumlah_elemen++;
			}
			cout << endl;
		}
		cout << endl;
	}
	nilai_rata_rata = jumlah_nilai / jumlah_elemen;
	cout << "Rata-Rata Element Yang Ada Didalamnya: " << nilai_rata_rata << endl;
	return 0;
}
