# Input: Data nilai mahasiswa
# Proses: Mengolah data nilai
# Output: Menampilkan ringkasan analisis

def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    hasil = []

    for nilai in data:
        if nilai >= batas:
            hasil.append(nilai)

    return hasil

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
banyak_data = len(nilai)
total = sum(nilai)
minimum = min(nilai) if banyak_data > 0 else 0
maksimum = max(nilai) if banyak_data > 0 else 0
rata = rata_rata(nilai)

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
belum_lulus = banyak_data - jumlah_lulus

print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {banyak_data}")
print(f"Total nilai      : {total}")
print(f"Rata-rata        : {rata:.2f}")
print(f"Nilai minimum    : {minimum}")
print(f"Nilai maksimum   : {maksimum}")
print(f"Batas kelulusan  : 60")
print(f"Daftar nilai lulus: {lulus}")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Belum lulus      : {belum_lulus}")


