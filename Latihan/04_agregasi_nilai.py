#Input: List nilai [75, 80, 65, 90, 88].
#Proses: Menghitung total menggunakan sum(), rata-rata menggunakan sum()/len(), nilai terkecil menggunakan min(), dan nilai terbesar menggunakan max().
#Output: Total nilai 398, rata-rata 79,60, nilai minimum 65, dan nilai maksimum 90.

nilai = [75, 80, 65, 90, 88]
total_nilai = sum(nilai)
rata_rata = total_nilai / len(nilai)
minimum = min(nilai)
maksimum = max(nilai)

print(f"Total nilai: {total_nilai}")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Nilai minimum: {minimum}")
print(f"Nilai maksimum: {maksimum}")