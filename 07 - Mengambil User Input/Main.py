# mengambil user input

# syntax dasar
# data yang dimasukan pasti bertipe string

data = input("masukan data = ")

print("data = ", data, " tipe = ", type(data))


# jika kita ingin mengabil integer atau float, maka
# harus kita casting terlebih dahulu
data_angka_int = int(input("masukan data angka = "))

print("data = ", data_angka_int, " tipe = ", type(data_angka_int))

data_angka_float = float(input("masukan data angka = "))

print("data = ", data_angka_float, " tipe = ", type(data_angka_float))


# untuk mengambil data boolean
# kita harus mengkasting lagi input yang dimasukan kedlam integer
# karena kalo string udah pasti true
data_bool = bool(int(input("masukan nilai boolean = ")))

print("data = ", data_bool, " tipe = ", type(data_bool))