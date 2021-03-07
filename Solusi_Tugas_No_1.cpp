#include <iostream>
using namespace std;

void segitiga() {
    int a, b, c;
    cout <<"Berikan Sisi A: ";
    cin >> a;
    cout <<"Berikan Sisi B: ";
    cin >> b;
    cout <<"Berikan Sisi C: ";
    cin >> c;
    if(a < 1 || b < 1 || c < 1) {
    	cout << "Bukan Segitiga" << endl;
	} else if(a == b && a == c) {
        cout << "Segitiga Sama Sisi" << endl;
    } else if(a * a == b * b + c * c || b * b == a * a + c * c || c * c == a * a + b * b) {
    	cout << "Segitiga Siku-Siku" << endl;
	} else if(a == b && a != c || a == c && a != b || c == b && c != a) {
		cout << "Segitiga Sama Kaki" << endl;
	} else {
    	cout << "Segitiga Sembarang" << endl;
	}
}

int main()
{
	system("Color C");
	cout << "=====================================================================" << endl;
	cout << "|          PROGRAM PROSEDUR MENENTUKAN SISI SEBUAH SEGITIGA         |" << endl;
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
	segitiga();
    return 0;
}
