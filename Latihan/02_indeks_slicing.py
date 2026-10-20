#Input: List nilai [75, 80, 65, 90, 88, 70].
#Proses: Mengakses elemen pertama menggunakan indeks 0, elemen terakhir menggunakan indeks -1, mengambil tiga elemen awal menggunakan slicing [:3], dan mengambil elemen indeks 1 sampai 3 menggunakan [1:4].
#Output: Elemen pertama 75, elemen terakhir 70, tiga elemen awal [75, 80, 65], dan hasil slicing [80, 65, 90].

nilai = [75, 80, 65, 90, 88, 70]


print("Nilai pertama:", nilai[0])
print("Nilai terakhir:", nilai[-1])
print("Tiga elemen awal:", nilai[:3])
print("Hasil indeks 1 sampai 3:", nilai[1:4])
