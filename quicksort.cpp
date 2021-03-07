#include<iostream>
using namespace std;

void quick_sort_asc(char data[], int left, int right) {
	int i = left, j = right, temp, pivot = data[(left + right) / 2];
	while(i <= j) {
		while(data[i] < pivot) i++;
		while(data[j] > pivot) j--;
		if(i <= j) {
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
			i++;
			j--;
	    };
	};
	if(left < j) quick_sort_asc(data, left, j);
	if(i < right) quick_sort_asc(data, i, right);
}

void quick_sort_desc(char data[], int left, int right) {
	int i = left, j = right, temp, pivot = data[(left + right) / 2];
	while(i <= j) {
		while(data[i] > pivot) i++;
		while(data[j] < pivot) j--;
		if(i <= j) {
			temp = data[i];
			data[i] = data[j];
			data[j] = temp;
			i++;
			j--;
	    };
	};
	if(left < j) quick_sort_desc(data, left, j);
	if(i < right) quick_sort_desc(data, i, right);
}

int main() {
	char data[25];
	int i, n;
	cout << "=================================================" << endl;
	cout << "|    PROGRAM SORTING DENGAN METODE QUICK SORT   |" << endl;
	cout << "=================================================" << endl;
	cout << "|                OLEH KELOMPOK 7                |" << endl;
	cout << "=================================================" << endl;
	cout << "| ANDI ALFIAN BAHTIAR     (2009106002)          |" << endl;
	cout << "| EGA SULFIKA             (2009106011)          |" << endl;
	cout << "| YANUAR GIDEON SIMALANGO (2009106014)          |" << endl;
	cout << "| DUTA VIRA PRADHANA DIPA (2009106053)          |" << endl;
	cout << "| AGUSTINUS SYAMA         (2009106150)          |" << endl;
	cout << "=================================================" << endl;
	cout << "Masukkan banyak huruf: "; cin >> n;
	for(i = 0; i < n; i++) {
		cout << "Masukkan huruf [" << i << "]: "; cin >> data[i];
	}
	cout << "Huruf sebelum diurutkan:" << endl;
	for(i = 0; i < n; i++) cout << data[i] << " ";
	cout << endl;
	cout << "Hasil sorting dengan metode quick sort secara ascending:" << endl;
	quick_sort_asc(data, 0, n - 1);
	for(i = 0; i < n; i++) cout << data[i] << " ";
	cout << endl;
	cout << "Hasil sorting dengan metode quick sort secara descending:" << endl;
	quick_sort_desc(data, 0, n - 1);
	for(i = 0; i < n; i++) cout << data[i] << " ";
	return 0;
}
