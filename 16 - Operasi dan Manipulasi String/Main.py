# operasi dan manupulasi string

# 1. MENGGABUNGKAN STRING

nama_depan = "Suwes"
nama_tengah = "M"
nama_akhir = "Hafiz"

nama_panjang = nama_depan +" " + nama_tengah +" " +nama_akhir
print(nama_panjang)



# 2. MENGHITUNG PANJANG STRING
panjangString = len(nama_panjang)
print("oanjang namanya =",panjangString)



# 3. OPERATOR UNTUK STRING

# mengecek apakah ada komponen char atau string di dalam string tsb

cari = "q"
status = cari in nama_panjang
print(cari,"ada di",nama_panjang,"=",status)

cari = "M"
status = cari in nama_panjang
print(cari,"ada di",nama_panjang,"=",status)

cari = "M"
status = cari not in nama_panjang # mengecek kebalikannya menggunakan logika NOT
print(cari,"ada di",nama_panjang,"=",status)

# mengulang string
print("ha"*5)
print(3*"wk")

# indexing
print(nama_panjang)
print("index ke 0 = ",nama_panjang[0]) # index diawali dari 0
print("index ke 3 = ",nama_panjang[3])
print("index ke -1 = ",nama_panjang[-1]) # jika indexnya min, akan di ambil dari belakang/akhir
print("index ke -2 = ",nama_panjang[-2])
print("index ke [0:3] = ",nama_panjang[0:3]) # index ketiga tidak diambil, hanya pembatas
# juga bisa dengan menambahkan increment agar bisa melompat ke index selanjutnya
print("index ke [0,2,4,6,8,10] = ",nama_panjang[0:11:2]) # 2 adalah increment

# ukuran item
print("paling kecil : ", min(nama_panjang)) # menggunakan operator helper min
print("paling besar : ", max(nama_panjang)) # menggunakan operator helper max



# 4 . OPERATOR DALAM BENTUK METHOD
data = "saya kuliah pada program studi manajemen"
jumlah = data.count("a") # .count() <- method, data <- dianggap objek
# dengan method kita bisa menggunakan parameter
print("jumlah kata a di data : ", jumlah)