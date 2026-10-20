#Input: List nilai [75, 80, 65, 90, 88].
#Proses: Membuat fungsi rata_rata(data) untuk menghitung total nilai dibagi jumlah data. Jika list kosong, fungsi mengembalikan nilai 0 agar tidak terjadi pembagian dengan nol.
#Output: Rata-rata nilai sebesar 79,60.

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata nilai: {rata_rata(nilai):.2f}")