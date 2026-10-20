#Input: List nilai [75, 55, 80, 60, 45, 90] dengan batas kelulusan 60.
#Proses: Memeriksa setiap nilai menggunakan perulangan for. Jika nilai lebih besar atau sama dengan 60, nilai dimasukkan ke list lulus menggunakan append().
#Output: Nilai yang lulus adalah [75, 80, 60, 90] dengan jumlah mahasiswa yang lulus sebanyak 4.

nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
    if x >= 60:
        lulus.append(x)

print("Nilai yang lulus:", lulus)
print("Jumlah mahasiswa yang lulus:", len(lulus))
