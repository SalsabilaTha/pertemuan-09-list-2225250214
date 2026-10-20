#Input: List awal [75, 80, 65].
#Proses: Mengubah nilai indeks 1 menjadi 82 menggunakan nilai[1] = 82, menambahkan 90 dengan append(), menyisipkan 70 menggunakan insert(), dan menghapus nilai 65 menggunakan remove().
#Output: List setelah dimanipulasi menjadi [75, 70, 82, 90].

nilai = [75, 80, 65]
nilai[1] = 82
nilai.append(90)
nilai.insert(1, 70)
nilai.remove(65)
print("List setelah dimanipulasi:", nilai)