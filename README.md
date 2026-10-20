# Pertemuan 09 - List 

**Nama:** Salsabila Thahira
**NIM:** 2225250214
**Kelas:** 3B

## Tujuan 
Praktik ini bertujuan untuk memahami penggunaan list pada Python dan mengolah kumpulan data numerik. Materi yang dipelajari meliputi pembuatan list, indeks dan slicing, manipulasi elemen, perulangan, penghitungan statistik, fungsi, serta analisis nilai mahasiswa.

## Struktur Program 
Program pada pertemuan 09 terdiri dari dua folder utama, yaitu latihan dan praktik.

### Latihan 1 - Membuat dan Membaca List
Menyimpan lima nilai mahasiswa ke dalam list dan menghitung jumlah elemennya menggunakan `len()`.

### Latihan 2 - Indeks dan Slicing
Mengakses nilai pertama, nilai terakhir, tiga nilai awal, dan sebagian elemen list menggunakan indeks dan slicing.

### Latihan 3 - Manipulasi List
Mengubah, menambah, menyisipkan, dan menghapus elemen menggunakan assignment, `append()`, `insert()`, dan `remove()`.

### Latihan 4 - Agregasi Nilai
Menghitung total, rata-rata, nilai minimum, dan nilai maksimum menggunakan `sum()`, `len()`, `min()`, dan `max()`.

### Latihan 5 - Filter Kelulusan
Memilih nilai yang memenuhi batas kelulusan 60 dan menghitung jumlah nilai yang lulus.

### Latihan 6 - Fungsi Statistik
Membuat fungsi `rata_rata()` untuk menghitung rata-rata list serta menangani list kosong.

### Praktik - Analisis Nilai Mahasiswa
Mengolah 10 nilai mahasiswa untuk mendapatkan jumlah data, total, rata-rata, nilai minimum, nilai maksimum, daftar nilai lulus, jumlah lulus, dan jumlah belum lulus.


## Cara Menjalankan
1. Buka folder proyek melalui Visual Studio Code.
2. Pastikan Python sudah terpasang.
3. Buka menu Terminal > New Terminal.
4. Jalankan program sesuai nama file menggunakan perintah berikut.

Contoh menjalankan latihan:

```bash
python latihan/01_buat_list.py
```

Menjalankan latihan lainnya:

```bash
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
python latihan/07_perulangan_nilai.py
python latihan/08_urutkan_nilai.py
```

Menjalankan program praktik:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Test Case
<table>
<thead>
<tr>
<th>No.</th>
<th>Program</th>
<th>Data Input</th>
<th>Hasil yang Diharapkan</th>
</tr>
</thead>
<tbody>

<tr>
<td>1</td>
<td>Membuat dan Membaca List</td>
<td>[75, 80, 65, 90, 88]</td>
<td>List tampil dan banyak data = 5</td>
</tr>

<tr>
<td>2</td>
<td>Indeks dan Slicing</td>
<td>[75, 80, 65, 90, 88, 70]</td>
<td>Nilai pertama = 75, nilai terakhir = 70, tiga nilai awal = [75, 80, 65]</td>
</tr>

<tr>
<td>3</td>
<td>Manipulasi List</td>
<td>[75, 80, 65]</td>
<td>List akhir = [75, 70, 82, 90]</td>
</tr>

<tr>
<td>4</td>
<td>Agregasi Nilai</td>
<td>[75, 80, 65, 90, 88]</td>
<td>Total = 398, rata-rata = 79.60, minimum = 65, maksimum = 90</td>
</tr>

<tr>
<td>5</td>
<td>Filter Kelulusan</td>
<td>[75, 55, 80, 60, 45, 90]</td>
<td>Nilai lulus = [75, 80, 60, 90], jumlah lulus = 4</td>
</tr>

<tr>
<td>6</td>
<td>Fungsi Statistik</td>
<td>[75, 80, 65, 90, 88]</td>
<td>Rata-rata = 79.60</td>
</tr>

<tr>
<td>7</td>
<td>Perulangan Nilai</td>
<td>[75, 80, 65, 90, 88]</td>
<td>Indeks 0 sampai 4 ditampilkan beserta setiap nilai</td>
</tr>

<tr>
<td>8</td>
<td>Mengurutkan Nilai</td>
<td>[75, 80, 65, 90, 88]</td>
<td>Nilai terurut = [65, 75, 80, 88, 90]</td>
</tr>

<tr>
<td>9</td>
<td>Analisis Nilai Mahasiswa</td>
<td>[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]</td>
<td>Total = 695, rata-rata = 69.50, 7 lulus, 3 belum lulus</td>
</tr>

<tr>
<td>10</td>
<td>Fungsi Rata-rata dengan List Kosong</td>
<td>[]</td>
<td>Menghasilkan 0 tanpa pembagian dengan nol</td>
</tr>
</tbody>
</table>

## Refleksi 
Saya memahami bahwa indeks digunakan untuk mengakses elemen tertentu dalam list, dengan indeks pertama dimulai dari 0. Kesalahan yang berhasil saya perbaiki adalah penggunaan indeks yang tidak sesuai, sehingga data yang ditampilkan tidak tepat. Setelah diperbaiki, saya dapat mengambil data dari list sesuai posisi yang diinginkan.