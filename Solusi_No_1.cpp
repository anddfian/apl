#include <iostream>
using namespace std;

int main() {
	system("Color C");
	int i, j, row, column;
	float jumlah_nilai, jumlah_elemen, nilai_terkecil, nilai_terbesar, nilai_rata_rata;
	cout << "=====================================================================" << endl;
	cout << "| PROGRAM MENAMPILKAN NILAI MIN, MAX, RATA-RATA DALAM SUATU MATRIKS |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|                          OLEH KELOMPOK 27                         |" << endl;
	cout << "=====================================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR (2009106002)                                  |" << endl;
	cout << "| RIZKI ANDRIYANTI    (2009106118)                                  |" << endl;
	cout << "| LIDYA SIMANUNGKALIT (2009106125)                                  |" << endl;
	cout << "| AL-INAYYA           (2009106127)                                  |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|    PROGRAM INI DIKERJAKAN OLEH ANDI ALFIAN BAHTIAR (2009106002)   |" << endl;
	cout << "=====================================================================" << endl;
	cout << "Masukkan Jumlah Baris Matriks: ";
	cin >> row;
	cout << "Masukkan Jumlah Kolom Matriks: ";
	cin >> column;
	float matriks[row][column];
	for(i = 0; i < row; i++) {
		for(j = 0; j < column; j++) {
	 		cout << "Masukkan Elemen Matriks [" << i << "," << j << "] : ";
			cin >> matriks[i][j];
		}
	}
	nilai_terkecil, nilai_terkecil = matriks[0][0];
	for(i = 0; i < row; i++) {
		for(j = 0; j < column; j++) { 
	  		cout << matriks[i][j] << " ";
	  		jumlah_nilai += matriks[i][j];
	  		jumlah_elemen++;
			if(nilai_terkecil > matriks[i][j]) {
				nilai_terkecil = matriks[i][j];
			}
			if(nilai_terbesar < matriks[i][j]) {
				nilai_terbesar = matriks[i][j];
			}
		}
		cout << endl;
	}
	nilai_rata_rata = jumlah_nilai / jumlah_elemen;
	cout << "Nilai Mix Dalam Matriks: " << nilai_terkecil << endl;
	cout << "Nilai Max Dalam Matriks: " << nilai_terbesar << endl;
	cout << "Rata-Rata Dalam Matriks: " << nilai_rata_rata << endl;
	return 0;
}
