#include <iostream>
#include <math.h>
using namespace std;

float phytagoras(float a, float b, float c) {
	if(b, c < a) {
		return sqrt(b * b + c * c);
	} else if(a, c < b)	{
		return sqrt(a * a + c * c);
	} else {
		return sqrt(a * a + b * b);
	}
}

string triplephytagoras(float a, float b, float c) {
	float st, sm;
	if(b, c < a) {
		st = a;
		sm = sqrt(b * b + c * c);
	} else if (a, c < b) {
		st = b;
		sm = sqrt(a * a + c * c);
	} else {
		st = c;
		sm = sqrt(a * a + b * b);
	}
	if(st == sm) {
		return " Merupakan Triple Phytagoras";
	} else {
		return " Bukan Triple Phytagoras";
	}
}

int main() {
	system ("Color C");
	float a, b, c;
	cout << "=====================================================================" << endl;
	cout << "|                PROGRAM MENENTUKAN TRIPEL PHYTAGORAS               |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|                          OLEH KELOMPOK 27                         |" << endl;
	cout << "=====================================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR (2009106002)                                  |" << endl;
	cout << "| RIZKI ANDRIYANTI    (2009106118)                                  |" << endl;
	cout << "| LIDYA SIMANUNGKALIT (2009106125)                                  |" << endl;
	cout << "| AL-INAYYA           (2009106127)                                  |" << endl;
	cout << "=====================================================================" << endl;
	cout << "|         PROGRAM INI DIKERJAKAN OLEH AL-INAYYA (2009106127)        |" << endl;
	cout << "=====================================================================" << endl;
	cout << "Masukkan Panjang Sisi A: ";
	cin >> a;
	cout << "Masukkan Panjang Sisi B: ";
	cin >> b;
	cout << "Masukkan Panjang Sisi C: ";
	cin >> c;
	cout << "Nilai Phytagorasnya Adalah: " << phytagoras(a, b, c) << endl;
	cout << a << ", " << b << ", Dan " << c << triplephytagoras(a, b, c) << endl;
    return 0;
}
