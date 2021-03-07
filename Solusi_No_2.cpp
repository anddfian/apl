#include<iostream>
using namespace std;

int main() {
	system("Color C");
	float matriks[2][2], matriks_invers[2][2], det;
	int i, j;
	cout << "=====================================================================" << endl;
	cout << "|           PROGRAM MENGHITUNG INVERS MATRIKS BERORDO 2x2           |" << endl;
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
	for(i = 0; i < 2; i++) {
		for(j = 0; j < 2; j++) {
	 		cout << "Masukkan Elemen Matriks [" << i << "," << j << "] : ";
			cin >> matriks[i][j];
		}
	}
	cout << "Matriks 2x2:" << endl;
	for(i = 0; i < 2; i++) {
		for(j = 0; j < 2; j++) {
			cout << matriks[i][j] << " ";
		}
		cout << endl;
	}
	det = matriks[0][0] * matriks[1][1] - matriks[1][0] * matriks[0][1];
	cout << "Determinan = " << det << endl;
	matriks_invers[0][0] = matriks[1][1];
	matriks_invers[0][1] = matriks[0][1] * -1;
	matriks_invers[1][0] = matriks[1][0] * -1;
	matriks_invers[1][1] = matriks[0][0];
	cout << "Invers Matriks 2x2: " << endl;
	for(i = 0; i < 2; i++) {
		for(j = 0; j < 2; j++) {
			printf("%0.2f ", (matriks_invers[i][j] / det));
		}
		cout << endl;
	}
	return 0;
}
