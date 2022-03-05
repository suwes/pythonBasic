## python memiliki beberapa tipe data
# tipe data yang ada di python = integer, float, string, boolean dan tipr data khusus

# integer
# integer ada tipe data angka satuan
print("====INTEGER====")
data_int = 10
print("nilai int = ",data_int)
print("tipe data =",type(data_int))

# float
# float adalah tipe data yang memiliki koma
print("====FLOAT====")
data_float = 1.5
print("nilai float = ",data_float)
print("tipe data =",type(data_float))

# string
# string adalah tipe data berupa kumpulan karakter
print("====STRING====")
data_str = "halo ini string"
print("nilai string = ",data_str)
print("tipe data =",type(data_str))

# boolean
# boolean adalah tipe data berupa true/false
print("====BOOLEAN====")
data_bool = True
print("nilai string = ",data_bool)
print("tipe data =",type(data_bool))


## tipe data khusus

# tipe data kompleks
# biasanya digunakan dalam perhitungan matematika

data_complexs = complex(1,5) # 5 akan otomatis dianggap bilangan imajiner
print("nilai complex = ",data_complexs)
print("tipe data =",type(data_complexs))

# tipe data dari bahasa c
# biasanya digunakan jika kita merasa perlu menggunakan tope data lain
# yang tidak ada di python

from ctypes import c_double # kita memanggil library ctypes
# di c ada long short char byte double
# dan menggunakan salah satu tipe data nya yaitu double
data_c_double = c_double(10.5)
print("nilai double = ",data_c_double)
print("tipe data =",type(data_c_double))
