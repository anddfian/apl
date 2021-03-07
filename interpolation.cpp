#include<iostream>
using namespace std;

int interpolation(char data[], char kunci, int low, int high) {
	while(low <= high) {
		int posisi = (((kunci - data[low]) / (data[high] - data[low])) * (high - low) + low);
		if(data[posisi] < kunci) {
			low = posisi + 1;
		} else if(data[posisi] == kunci) {
			return posisi;
		}
	}
	return -1;
}

int main() {
	char data[25], kunci;
	int i, n;
	cout << "=================================================" << endl;
	cout << "| PROGRAM SEARCHING DENGAN METODE INTERPOLATION |" << endl;
	cout << "=================================================" << endl;
	cout << "|                OLEH KELOMPOK 7                |" << endl;
	cout << "=================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR     (2009106002)          |" << endl;
	cout << "| EGA SULFIKA             (2009106011)          |" << endl;
	cout << "| YANUAR GIDEON SIMALANGO (2009106014)          |" << endl;
	cout << "| DUTA VIRA PRADHANA DIPA (2009106053)          |" << endl;
	cout << "| AGUSTINUS SYAMA         (2009106150)          |" << endl;
	cout << "=================================================" << endl;
	cout << "Masukkan jumlah huruf: "; cin >> n;
	for(i = 0; i < n; i++) {
		cout << "Masukkan huruf [" << i << "]: "; cin >> data[i];
	}
	cout << "Huruf yang telah dimasukkan: " << endl;
	for(i = 0; i < n; i++) cout << data[i] << " ";
	cout << endl;
	cout << "Huruf yang dicari: "; cin >> kunci;
	int index = interpolation(data, kunci, 0, n - 1);
	if(index != -1) cout << "Huruf " << kunci << " pada posisi indeks ke-" << index;
	else cout << "Huruf " << kunci << " tidak ditemukan";
	return 0;
}
