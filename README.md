# Tentang
- Mata Kuliah: Algoritma Pemrograman Lanjut
- Kelas: Informatika A 2020
- Dosen Pembimbing: Awang Harsa K, M. Kom & Ir. Novianti Puspitasari, M. Eng
- Bahasa Pemrograman: Python / C++

# Algoritma Sorting dengan metode Quick Sort
1.	Tulis “Masukkan banyak huruf: “
2.	Masukkan n
3.	i ← 0
4.	Jika i < n maka kerjakan baris 5, jika tidak maka kerjakan baris 8
5.	i ← i + 1
6.	Tulis “Masukkan huruf [“ i “]: “
7.	Masukkan data[i] dan kerjakan baris 4
8.	Tulis “Huruf sebelum diurutkan:”
9.	i ← 0
10.	Jika i < n maka kerjakan baris 11, jika tidak maka kerjakan baris 13
11.	i ← i + 1
12.	Tulis data[i] “ ” dan kerjakan baris 10
13.	Tulis “Hasil sorting dengan metode quick sort secara ascending:”
14.	left ← 0
15.	right ← n - 1
16.	i ← left
17.	j ← right
18.	pivot ← data[(left + right) / 2]
19.	Selama i <= j maka kerjakan baris 20, jika tidak maka kerjakan baris 30
20.	Selama data[i] < pivot maka kerjakan baris 21, jika tidak maka kerjakan baris 22
21.	i ← i + 1 dan kerjakan baris 20
22.	Selama data[j] > pivot maka kerjakan baris 23, jika tidak maka kerjakan baris 24
23.	j ← j – 1 dan kerjakan baris 22
24.	Jika i <= j maka kerjakan baris 25, jika tidak maka kerjakan baris 19
25.	temp ← data[i]
26.	data[i] ← data[j]
27.	data[j] ← temp
28.	i ← i + 1
29.	j ← j - 1 dan kerjakan baris 19
30.	Jika left < j maka kerjakan baris 31, jika tidak maka kerjakan baris 32
31.	right ← j dan kerjakan baris 16
32.	Jika i < right maka kerjakan baris 33, jika tidak maka kerjakan baris 34
33.	left ← i dan kerjakan baris 16
34.	i ← 0
35.	Jika i < n maka kerjakan baris 36, jika tidak maka kerjakan baris 38
36.	i ← i + 1
37.	Tulis data[i] “ “ dan kerjakan baris 35
38.	Tulis “Hasil sorting metode dengan quick sort secara descending:”
39.	left ← 0
40.	right ← n - 1
41.	i ← left
42.	j ← right
43.	pivot ← data[(left + right) / 2]
44.	Selama i <= j maka kerjakan baris 45, jika tidak maka kerjakan baris 55
45.	Selama data[i] > pivot maka kerjakan baris 46, jika tidak maka kerjakan baris 47
46.	i ← i + 1 dan kerjakan baris 45
47.	Selama data[j] < pivot maka kerjakan baris 48, jika tidak maka kerjakan baris 49
48.	j ← j – 1 dan kerjakan baris 47
49.	Jika i <= j maka kerjakan baris 50, jika tidak maka kerjakan baris 44
50.	temp ← data[i]
51.	data[i] ← data[j]
52.	data[j] ← temp
53.	i ← i + 1
54.	j ← j - 1 dan kerjakan baris 44
55.	Jika left < j maka kerjakan baris 56, jika tidak maka kerjakan baris 57
56.	right ← j dan kerjakan baris 41
57.	Jika i < right maka kerjakan baris 58, jika tidak maka kerjakan baris 59
58.	left ← i dan kerjakan baris 41
59.	i ← 0
60.	Jika i < n maka kerjakan baris 61
61.	i ← i + 1
62.	Tulis data[i] “ ” dan kerjakan baris 60

# Algoritma Searching dengan metode Interpolation
1.	Tulis “Masukkan jumlah huruf: “
2.	Masukkan n
3.	i ← 0
4.	Jika i < n maka kerjakan baris 5, jika tidak maka kerjakan baris 8
5.	i ← i + 1
6.	Tulis “Masukkan Data [“ i “]: “
7.	Masukkan data[i] dan kerjakan baris 4
8.	i ← 0
9.	Jika i < n maka kerjakan baris 10, jika tidak maka kerjakan baris 12
10.	i ← i + 1
11.	Tulis data[i] dan kerjakan baris 9
12.	Tulis “Huruf yang dicari: “
13.	Masukkan kunci
14.	low ← 0
15.	high ← n - 1
16.	Selama low <= high maka kerjakan baris 17, jika tidak maka kerjakan baris 21
17.	posisi ← (((kunci - data[low]) / (data[high] - data[low])) * (high - low) + low)
18.	Jika data[posisi] < kunci maka kerjakan baris 19, jika lagi data[posisi] == kunci maka kerjakan baris 21
19.	low ← posisi + 1 dan kerjakan baris 16
20.	index ← posisi dan kerjakan baris 22
21.	index ← -1
22.	Jika index != -1 maka kerjakan baris 23, jika tidak maka kerjakan baris 24
23.	Tulis “Huruf ” kunci “ pada posisi indeks ke-“ index
24.	Tulis “Huruf ” kunci “ tidak ditemukan.”
