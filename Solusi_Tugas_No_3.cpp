#include<iostream>
using namespace std;

int pangkat(int a, int b)
{
	if(b == 0) {
		return 1;
	} else {
		return a * pangkat(a, b - 1);
 	}
}

int main() {
	system("Color C");
	int a, b;
	cout << "=====================================================================" << endl;
	cout << "|                      PROGRAM FUNGSI REKURSIF                      |" << endl;
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
	cout << "Masukan Bilangan: ";
	cin >> a;
	cout << "Masukan Pangkat: ";
	cin >> b;
	cout << "Hasil: " << endl;
	cout << a << "^" << b << " = " << pangkat(a, b) << endl;
	return 0;
}
